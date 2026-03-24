---
layout: null
title: "Life"
permalink: /life/
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Life | Lily Tan</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    *,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
    html{scroll-behavior:auto}
    body{font-family:'Inter',system-ui,sans-serif;background:#faf8ff;color:#1e1b4b;overflow-x:hidden}

    /* Progress bar */
    #progress{position:fixed;top:0;left:0;height:2px;z-index:9999;
      background:linear-gradient(90deg,#7c3aed,#f75092);width:0%;pointer-events:none}

    /* Top bar */
    .topbar{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;justify-content:space-between;align-items:center;
      padding:1.5rem 3rem;background:rgba(250,248,255,.8);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
      border-bottom:1px solid rgba(124,58,237,.06);pointer-events:none}
    .topbar a{color:#1e1b4b;text-decoration:none;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;
      pointer-events:auto;transition:color .3s}
    .topbar a:hover{color:#7c3aed}
    .topbar__logo{font-size:.85rem;font-weight:700;letter-spacing:.05em}
    .topbar__logo span{background:linear-gradient(135deg,#7c3aed,#f75092);-webkit-background-clip:text;-webkit-text-fill-color:transparent}

    /* Section counter */
    .counter{position:fixed;right:3rem;bottom:3rem;z-index:100;font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;
      color:rgba(124,58,237,.35);pointer-events:none}
    .counter span{color:#7c3aed;font-weight:600;font-size:1rem}

    /* Right dots */
    .dots{position:fixed;right:2.5rem;top:50%;transform:translateY(-50%);z-index:100;display:flex;flex-direction:column;gap:1.2rem}
    .dots__item{width:6px;height:6px;border-radius:50%;background:rgba(124,58,237,.2);cursor:pointer;transition:all .4s;position:relative}
    .dots__item.active{background:#7c3aed;transform:scale(1.6)}
    .dots__item::after{content:attr(data-label);position:absolute;right:18px;top:50%;transform:translateY(-50%);font-size:.6rem;
      letter-spacing:.1em;text-transform:uppercase;white-space:nowrap;opacity:0;transition:opacity .3s;color:#7c3aed}
    .dots__item:hover::after{opacity:1}

    /* ===== SECTIONS ===== */
    .scene{position:relative;z-index:1;width:100%;min-height:100vh;display:flex;align-items:center;justify-content:center}
    .scene__content{position:relative;max-width:1100px;width:100%;padding:4rem 3rem}

    /* ===== HERO with 3D particle canvas ===== */
    .scene--hero{height:100vh;text-align:center;flex-direction:column;
      background:linear-gradient(160deg,#f5f3ff 0%,#fdf2f8 40%,#ede9fe 100%);position:relative;overflow:hidden}
    #c{position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none}
    .hero-content{position:relative;z-index:2}
    .hero__title{font-family:'Playfair Display',serif;font-size:clamp(3rem,8vw,6.5rem);font-weight:400;letter-spacing:-.03em;line-height:1.05;
      color:#1e1b4b;opacity:0;transform:translateY(30px);transition:opacity 1s ease,transform 1s ease}
    .hero__title em{font-style:italic;background:linear-gradient(135deg,#7c3aed,#f75092);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
    .hero__sub{margin-top:1.5rem;font-size:.9rem;font-weight:300;color:rgba(30,27,75,.4);letter-spacing:.05em;
      opacity:0;transform:translateY(20px);transition:opacity 1s ease .3s,transform 1s ease .3s}
    .hero__scroll{position:absolute;bottom:3rem;left:50%;transform:translateX(-50%);font-size:.65rem;letter-spacing:.2em;
      text-transform:uppercase;color:rgba(124,58,237,.3);opacity:0;transition:opacity 1s ease .6s;z-index:2}
    .hero__scroll::after{content:'';display:block;width:1px;height:40px;background:linear-gradient(rgba(124,58,237,.3),transparent);margin:.8rem auto 0}
    .scene--hero.in-view .hero__title,.scene--hero.in-view .hero__sub,.scene--hero.in-view .hero__scroll{opacity:1;transform:translateY(0)}
    .scene--hero.in-view .hero__scroll{transform:translateX(-50%)}

    /* ===== Story sections — light backgrounds ===== */
    .scene--light{background:#faf8ff}
    .scene--soft{background:linear-gradient(160deg,#f5f3ff,#fdf2f8)}
    .scene--white{background:#fff}

    .story{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
    .story--reverse{direction:rtl}
    .story--reverse>*{direction:ltr}
    .story--center{grid-template-columns:1fr;text-align:center;justify-items:center}

    .story__label{font-size:.65rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;
      background:linear-gradient(135deg,#7c3aed,#f75092);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:1.2rem}
    .story__title{font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:400;line-height:1.15;
      letter-spacing:-.02em;margin-bottom:1rem;color:#1e1b4b}
    .story__title em{font-style:italic;color:#7c3aed}
    .story__divider{width:40px;height:2px;background:linear-gradient(90deg,#7c3aed,#f75092);margin:1.5rem 0;border-radius:1px}
    .story--center .story__divider{margin:1.5rem auto}
    .story__text{font-size:.92rem;font-weight:300;line-height:1.85;color:rgba(30,27,75,.5);max-width:400px}
    .story--center .story__text{max-width:480px;margin:0 auto}

    /* Photo containers */
    .photos{display:flex;gap:1.5rem;perspective:800px}
    .photo{
      width:260px;height:340px;border-radius:12px;overflow:hidden;
      border:1px solid rgba(124,58,237,.08);
      background:linear-gradient(135deg,#f5f3ff,#fdf2f8);
      display:flex;align-items:center;justify-content:center;flex-shrink:0;
      box-shadow:0 8px 40px rgba(124,58,237,.08);
      transition:transform .6s cubic-bezier(.4,0,.2,1),box-shadow .6s ease;will-change:transform}
    .photo:hover{transform:scale(1.04) rotateY(-2deg)!important;box-shadow:0 16px 60px rgba(124,58,237,.18)}
    .photo--wide{width:100%;max-width:420px;height:260px}
    .photos .photo:nth-child(1){transform:translateZ(30px) rotateY(3deg)}
    .photos .photo:nth-child(2){transform:translateZ(-20px) rotateY(-3deg);margin-top:3rem}
    .photo img{width:100%;height:100%;object-fit:cover}
    .photo__empty{color:rgba(124,58,237,.2);font-size:.72rem;text-align:center;display:flex;flex-direction:column;align-items:center;gap:.5rem}
    [data-speed]{will-change:transform}

    /* Reveal animation */
    .reveal-item{opacity:0;transform:translateY(40px);transition:opacity .8s cubic-bezier(.4,0,.2,1),transform .8s cubic-bezier(.4,0,.2,1)}
    .in-view .reveal-item{opacity:1;transform:translateY(0)}
    .in-view .reveal-item:nth-child(2){transition-delay:.15s}

    /* Ending */
    .scene--ending{background:linear-gradient(160deg,#ede9fe,#fdf2f8,#f5f3ff);text-align:center;flex-direction:column}
    .scene--ending .story__title{font-size:clamp(1.8rem,4vw,3rem)}
    .ending__btn{display:inline-block;margin-top:1.5rem;padding:.7rem 2rem;border-radius:30px;font-size:.78rem;font-weight:600;
      letter-spacing:.08em;text-decoration:none;color:#fff;
      background:linear-gradient(135deg,#7c3aed,#f75092);
      box-shadow:0 4px 20px rgba(124,58,237,.25);transition:all .3s}
    .ending__btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(124,58,237,.4)}

    /* Mobile */
    @media(max-width:768px){
      .topbar{padding:1.2rem 1.5rem}
      .story{grid-template-columns:1fr;gap:2rem}
      .story--reverse{direction:ltr}
      .photos{flex-direction:column;align-items:center}
      .photos .photo:nth-child(2){margin-top:0}
      .photo{width:220px!important;height:280px!important}
      .dots{right:1rem}
      .counter{right:1.5rem;bottom:1.5rem}
      .scene__content{padding:3rem 1.5rem}
    }
  </style>
</head>
<body>

<div id="progress"></div>

<nav class="topbar">
  <a href="/">&larr; Home</a>
  <a href="/" class="topbar__logo">LILY <span>TAN</span></a>
  <a href="/cv/">CV &rarr;</a>
</nav>

<div class="counter"><span id="secNum">01</span> / 05</div>

<div class="dots" id="dots">
  <div class="dots__item active" data-label="Intro" data-idx="0"></div>
  <div class="dots__item" data-label="Pets" data-idx="1"></div>
  <div class="dots__item" data-label="Flowers" data-idx="2"></div>
  <div class="dots__item" data-label="Travel" data-idx="3"></div>
  <div class="dots__item" data-label="End" data-idx="4"></div>
</div>

<!-- ===== 0: Hero — with 3D particle ribbons ===== -->
<section class="scene scene--hero" data-idx="0">
  <canvas id="c"></canvas>
  <div class="hero-content">
    <div class="hero__title">Beyond the<br><em>Research</em></div>
    <div class="hero__sub">A personal story told through light, space, and memory</div>
  </div>
  <div class="hero__scroll">Scroll to begin</div>
</section>

<!-- 1: Pet Lover -->
<section class="scene scene--white" data-idx="1">
  <div class="scene__content">
    <div class="story">
      <div class="reveal-item" data-speed="0.8">
        <div class="story__label">01 &mdash; Pet Lover</div>
        <div class="story__title">My Furry<br><em>Companions</em></div>
        <div class="story__divider"></div>
        <div class="story__text">They don't care about publications or deadlines. They remind me what unconditional love looks like, every single day.</div>
      </div>
      <div class="reveal-item" data-speed="1.3">
        <div class="photos">
          <div class="photo" data-speed="1.5" data-tilt="3">
            <div class="photo__empty">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              Add photo
            </div>
          </div>
          <div class="photo" data-speed="0.6" data-tilt="-4">
            <div class="photo__empty">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              Add photo
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 2: Florist -->
<section class="scene scene--soft" data-idx="2">
  <div class="scene__content">
    <div class="story story--reverse">
      <div class="reveal-item" data-speed="0.7">
        <div class="story__label">02 &mdash; Florist</div>
        <div class="story__title">Blooming<br>with <em>Flowers</em></div>
        <div class="story__divider"></div>
        <div class="story__text">Arranging flowers is my meditation. Each bouquet is a small design challenge — color, form, balance. It is research for the soul.</div>
      </div>
      <div class="reveal-item" data-speed="1.2">
        <div class="photos">
          <div class="photo" data-speed="1.6" data-tilt="-3">
            <div class="photo__empty">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              Add photo
            </div>
          </div>
          <div class="photo" data-speed="0.5" data-tilt="5">
            <div class="photo__empty">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              Add photo
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 3: Travel & Grow -->
<section class="scene scene--white" data-idx="3">
  <div class="scene__content">
    <div class="story">
      <div class="reveal-item" data-speed="0.9">
        <div class="story__label">03 &mdash; Travel &amp; Grow</div>
        <div class="story__title">Exploring<br>the <em>World</em></div>
        <div class="story__divider"></div>
        <div class="story__text">Travel broadens the mind and feeds the soul. Every new place brings fresh perspectives that find their way back into my work and thinking.</div>
      </div>
      <div class="reveal-item" data-speed="1.4">
        <div class="photo photo--wide" data-speed="1.3" data-tilt="-2">
          <div class="photo__empty">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
            Add photo
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 6: Ending -->
<section class="scene scene--ending" data-idx="4">
  <div class="scene__content" style="text-align:center">
    <div class="reveal-item">
      <div class="story__title">The Story<br><em>Continues</em>...</div>
      <div class="story__text" style="max-width:450px;margin:0 auto">Thank you for taking a moment to know me beyond the publications.</div>
      <a href="/" class="ending__btn">Back to Home &rarr;</a>
    </div>
  </div>
</section>

<!-- ===== ENGINE ===== -->
<script>
(function(){
  /* ===== Three.js — ONLY in hero section ===== */
  var canvas = document.getElementById('c');
  var heroSection = document.querySelector('.scene--hero');
  var W = heroSection.offsetWidth, H = heroSection.offsetHeight;

  var renderer = new THREE.WebGLRenderer({canvas:canvas, antialias:true, alpha:true});
  renderer.setSize(W, H);
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setClearColor(0x000000, 0); // transparent

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(60, W/H, 0.1, 100);
  camera.position.set(0, 0, 15);

  // Lights
  scene.add(new THREE.AmbientLight(0xffffff, 0.4));
  var ptLight = new THREE.PointLight(0xffffff, 0.8, 40);
  ptLight.position.set(5, 5, 10);
  scene.add(ptLight);

  /* ===== Simple noise function ===== */
  function noise(x,y,z){
    var n=x*12.9898+y*78.233+z*37.719;
    n=Math.sin(n)*43758.5453;
    return n-Math.floor(n);
  }
  function smoothNoise(x,y,z){
    return (Math.sin(x*1.1+y*0.7)*0.5+Math.sin(y*1.3+z*0.9)*0.3+Math.sin(z*0.8+x*1.5)*0.2);
  }

  /* ===== Flowing Particle Ribbons ===== */
  var ribbonCurves = [
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(-22,2,0), new THREE.Vector3(-12,6,-2), new THREE.Vector3(-4,0,-4),
      new THREE.Vector3(4,-4,-3), new THREE.Vector3(12,2,-1), new THREE.Vector3(20,5,0), new THREE.Vector3(28,0,1)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(-20,-5,1), new THREE.Vector3(-10,-1,-1), new THREE.Vector3(0,4,-3),
      new THREE.Vector3(8,-2,-4), new THREE.Vector3(16,1,-2), new THREE.Vector3(24,-3,0), new THREE.Vector3(30,2,1)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(-24,0,-1), new THREE.Vector3(-14,5,-3), new THREE.Vector3(-6,-3,-5),
      new THREE.Vector3(2,6,-4), new THREE.Vector3(10,-1,-2), new THREE.Vector3(18,3,-1), new THREE.Vector3(26,-2,0)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(-18,-7,2), new THREE.Vector3(-8,3,0), new THREE.Vector3(2,-5,-2),
      new THREE.Vector3(10,4,-4), new THREE.Vector3(16,-3,-3), new THREE.Vector3(22,1,-1), new THREE.Vector3(28,-4,0)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(-21,7,-1), new THREE.Vector3(-11,-4,-2), new THREE.Vector3(-1,5,-4),
      new THREE.Vector3(7,-6,-3), new THREE.Vector3(15,4,-2), new THREE.Vector3(23,-1,0), new THREE.Vector3(29,3,1)
    ], false, 'catmullrom', 0.3)
  ];

  var ribbons = [];
  var PER_RIBBON = 2000;
  var ribbonColors = [0x7c3aed, 0xf75092, 0x9f50d3, 0xa78bfa, 0xf9a8d4];

  ribbonCurves.forEach(function(curve, ri){
    var geo = new THREE.BufferGeometry();
    var pos = new Float32Array(PER_RIBBON * 3);
    var sizes = new Float32Array(PER_RIBBON);

    // Each particle has: its own t-position on curve, speed, spread offset
    var particleData = [];
    for(var i = 0; i < PER_RIBBON; i++){
      var t = Math.random(); // random start position along curve
      var speed = 0.02 + Math.random() * 0.04; // varying flow speeds
      var spreadR = 0.05 + Math.random() * 0.4; // distance from center
      var spreadAngle = Math.random() * Math.PI * 2;
      var sz = 0.04 + Math.random() * Math.random() * 0.25; // few big, many small
      sizes[i] = sz;
      particleData.push({ t:t, speed:speed, spreadR:spreadR, spreadAngle:spreadAngle, noiseOffset: Math.random()*100 });

      var pt = curve.getPointAt(t);
      pos[i*3] = pt.x; pos[i*3+1] = pt.y; pos[i*3+2] = pt.z;
    }

    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('size', new THREE.BufferAttribute(sizes, 1));

    var points = new THREE.Points(geo, new THREE.PointsMaterial({
      color: ribbonColors[ri],
      size: 0.12,
      transparent: true,
      opacity: 0.75,
      sizeAttenuation: true
    }));
    scene.add(points);
    ribbons.push({ points:points, geo:geo, curve:curve, data:particleData,
      baseSpeed: 0.015 + ri * 0.005 });
  });

  /* ===== Scroll & Parallax ===== */
  var sections = document.querySelectorAll('.scene');
  var totalH, scrollProg = 0;
  var heroH = heroSection.offsetHeight;

  function measure(){
    totalH = document.documentElement.scrollHeight - window.innerHeight;
    heroH = heroSection.offsetHeight;
  }
  measure();

  window.addEventListener('resize', function(){
    W = heroSection.offsetWidth; H = heroSection.offsetHeight;
    camera.aspect = W/H; camera.updateProjectionMatrix();
    renderer.setSize(W, H);
    measure();
  });

  window.addEventListener('scroll', function(){
    scrollProg = totalH > 0 ? window.pageYOffset / totalH : 0;
    var scrollY = window.pageYOffset;

    // Parallax for photos
    var parallaxEls = document.querySelectorAll('[data-speed]');
    parallaxEls.forEach(function(el){
      var speed = parseFloat(el.getAttribute('data-speed'));
      var tilt = parseFloat(el.getAttribute('data-tilt')) || 0;
      var rect = el.getBoundingClientRect();
      var center = rect.top + rect.height/2;
      var offset = (center - window.innerHeight/2) * (speed - 1) * 0.3;
      var rotY = tilt * Math.sin(scrollY * 0.002);
      el.style.transform = 'translateY('+offset+'px) rotateY('+rotY+'deg)';
    });
  }, {passive:true});

  /* ===== Intersection Observer ===== */
  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if(e.isIntersecting) e.target.classList.add('in-view'); });
  }, {threshold:0.25});
  sections.forEach(function(s){ observer.observe(s); });

  /* ===== UI refs ===== */
  var dots = document.querySelectorAll('.dots__item');
  var secNum = document.getElementById('secNum');
  var progBar = document.getElementById('progress');

  /* ===== Mouse tracking for speed boost ===== */
  var mouse = {x:0, y:0, speed:0, prevX:0, prevY:0, isOver:false};

  heroSection.addEventListener('mousemove', function(e){
    var dx = e.clientX - mouse.prevX;
    var dy = e.clientY - mouse.prevY;
    mouse.speed = Math.min(Math.sqrt(dx*dx + dy*dy), 80); // cap
    mouse.prevX = e.clientX;
    mouse.prevY = e.clientY;
    // Normalized -1 to 1
    mouse.x = (e.clientX / W) * 2 - 1;
    mouse.y = -((e.clientY / H) * 2 - 1);
    mouse.isOver = true;
  });
  heroSection.addEventListener('mouseleave', function(){ mouse.isOver = false; });

  /* ===== Render — only animates hero particles ===== */
  var clock = new THREE.Clock();
  var smoothMouseSpeed = 0;

  function render(){
    requestAnimationFrame(render);
    var el = clock.getElapsedTime();
    var scrollY = window.pageYOffset;

    // Smooth mouse speed (decays when not moving)
    var targetSpeed = mouse.isOver ? mouse.speed : 0;
    smoothMouseSpeed += (targetSpeed - smoothMouseSpeed) * 0.08;
    mouse.speed *= 0.9; // decay between moves

    // Speed multiplier: 1x base, up to 4x when mouse moves fast
    var speedMult = 1 + smoothMouseSpeed * 0.04;

    // Scroll-driven rotation of entire scene in hero
    var heroProgress = Math.min(1, scrollY / heroH);
    scene.rotation.y = heroProgress * 0.4 + mouse.x * 0.05;
    scene.position.y = heroProgress * 3;

    // Animate ribbons — particles FLOW along curves like water
    for(var ri = 0; ri < ribbons.length; ri++){
      var rb = ribbons[ri];
      var positions = rb.geo.attributes.position.array;
      var curve = rb.curve;

      for(var i = 0; i < PER_RIBBON; i++){
        var pd = rb.data[i];

        // Advance particle along curve (actual flowing!)
        pd.t += pd.speed * speedMult * 0.016;
        if(pd.t > 1) pd.t -= 1;

        var t = pd.t;
        var pt = curve.getPointAt(t);
        var tangent = curve.getTangentAt(t);

        // Perpendicular spread with organic noise
        var perpX = -tangent.y, perpY = tangent.x;
        var n1 = smoothNoise(t*5+pd.noiseOffset, el*0.3+ri, ri*7);
        var n2 = smoothNoise(t*4+pd.noiseOffset+50, el*0.25, ri*3+20);
        var dSpread = pd.spreadR * (0.7 + n1*0.5);

        positions[i*3]   = pt.x + perpX*dSpread*Math.cos(pd.spreadAngle+el*0.2+n1*0.5) + n2*0.15;
        positions[i*3+1] = pt.y + perpY*dSpread*Math.sin(pd.spreadAngle+el*0.15) + n1*0.12;
        positions[i*3+2] = pt.z + Math.sin(t*8+el*0.3+pd.noiseOffset)*0.15*pd.spreadR;
      }
      rb.geo.attributes.position.needsUpdate = true;
    }

    // Fade particles as user scrolls past hero
    var fadeOut = Math.max(0, 1 - heroProgress * 1.5);
    ribbons.forEach(function(rb){ rb.points.material.opacity = 0.7 * fadeOut; });

    // UI updates
    var idx = Math.min(Math.floor(scrollProg * sections.length), sections.length - 1);
    secNum.textContent = ('0' + (idx+1)).slice(-2);
    progBar.style.width = (scrollProg * 100) + '%';
    dots.forEach(function(d,i){ d.classList.toggle('active', i === idx); });

    renderer.render(scene, camera);
  }
  render();

  /* ===== Dots nav ===== */
  dots.forEach(function(d){
    d.addEventListener('click', function(){
      sections[parseInt(d.getAttribute('data-idx'))].scrollIntoView({behavior:'smooth'});
    });
  });
})();
</script>
</body>
</html>
