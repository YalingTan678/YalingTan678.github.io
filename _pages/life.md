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
    body{font-family:'Inter',system-ui,sans-serif;background:#000;color:#fff;overflow-x:hidden}

    /* 3D canvas — fixed behind everything */
    #c{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0}

    /* Film grain */
    .grain{position:fixed;inset:0;z-index:9998;pointer-events:none;opacity:0.035;
      background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
      background-size:128px}

    /* Progress bar */
    #progress{position:fixed;top:0;left:0;height:2px;z-index:9999;background:#fff;width:0%;pointer-events:none}

    /* Top bar */
    .topbar{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;justify-content:space-between;align-items:center;
      padding:1.8rem 3rem;mix-blend-mode:difference;pointer-events:none}
    .topbar a{color:#fff;text-decoration:none;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;
      pointer-events:auto;transition:opacity .3s}
    .topbar a:hover{opacity:.5}
    .topbar__logo{font-size:.85rem;font-weight:700;letter-spacing:.05em}

    /* Section counter */
    .counter{position:fixed;right:3rem;bottom:3rem;z-index:100;font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;
      color:rgba(255,255,255,.4);mix-blend-mode:difference;pointer-events:none}
    .counter span{color:#fff;font-weight:600;font-size:1rem}

    /* Right dots */
    .dots{position:fixed;right:2.5rem;top:50%;transform:translateY(-50%);z-index:100;display:flex;flex-direction:column;gap:1.2rem;mix-blend-mode:difference}
    .dots__item{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.25);cursor:pointer;transition:all .4s;position:relative}
    .dots__item.active{background:#fff;transform:scale(1.6)}
    .dots__item::after{content:attr(data-label);position:absolute;right:18px;top:50%;transform:translateY(-50%);font-size:.6rem;
      letter-spacing:.1em;text-transform:uppercase;white-space:nowrap;opacity:0;transition:opacity .3s;color:rgba(255,255,255,.5)}
    .dots__item:hover::after{opacity:1}

    /* ===== SCROLLABLE SECTIONS ===== */
    .scene{position:relative;z-index:1;width:100%;min-height:100vh;display:flex;align-items:center;justify-content:center}

    /* Transparent background so 3D shows through */
    .scene__content{
      position:relative;max-width:1100px;width:100%;padding:4rem 3rem;
    }

    /* Hero */
    .scene--hero{height:100vh;text-align:center;flex-direction:column}
    .hero__title{font-family:'Playfair Display',serif;font-size:clamp(3rem,8vw,7rem);font-weight:400;letter-spacing:-.03em;line-height:1.05;
      opacity:0;transform:translateY(30px);transition:opacity 1s ease,transform 1s ease}
    .hero__title em{font-style:italic}
    .hero__sub{margin-top:1.5rem;font-size:.85rem;font-weight:300;color:rgba(255,255,255,.35);letter-spacing:.05em;
      opacity:0;transform:translateY(20px);transition:opacity 1s ease .3s,transform 1s ease .3s}
    .hero__scroll{position:absolute;bottom:3rem;left:50%;transform:translateX(-50%);font-size:.65rem;letter-spacing:.2em;
      text-transform:uppercase;color:rgba(255,255,255,.3);opacity:0;transition:opacity 1s ease .6s}
    .hero__scroll::after{content:'';display:block;width:1px;height:40px;background:linear-gradient(rgba(255,255,255,.3),transparent);margin:.8rem auto 0}
    .scene--hero.in-view .hero__title,
    .scene--hero.in-view .hero__sub,
    .scene--hero.in-view .hero__scroll{opacity:1;transform:translateY(0) translateX(0)}
    .scene--hero.in-view .hero__scroll{transform:translateX(-50%)}

    /* Story sections */
    .story{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
    .story--reverse{direction:rtl}
    .story--reverse>*{direction:ltr}
    .story--center{grid-template-columns:1fr;text-align:center;justify-items:center}

    .story__label{font-size:.65rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.35);margin-bottom:1.2rem}
    .story__title{font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3.5rem);font-weight:400;line-height:1.15;letter-spacing:-.02em;margin-bottom:1rem}
    .story__title em{font-style:italic}
    .story__divider{width:40px;height:1px;background:rgba(255,255,255,.2);margin:1.5rem 0}
    .story--center .story__divider{margin:1.5rem auto}
    .story__text{font-size:.92rem;font-weight:300;line-height:1.85;color:rgba(255,255,255,.5);max-width:400px}
    .story--center .story__text{max-width:480px;margin:0 auto}

    /* Photo containers — 3D parallax floating */
    .photos{display:flex;gap:1.5rem;perspective:800px}
    .photos--single{display:block}
    .photo{
      width:260px;height:340px;border-radius:8px;overflow:hidden;
      border:1px solid rgba(255,255,255,.1);
      background:rgba(255,255,255,.04);
      display:flex;align-items:center;justify-content:center;flex-shrink:0;
      box-shadow:0 8px 40px rgba(0,0,0,.4);
      transition:transform .6s cubic-bezier(.4,0,.2,1),box-shadow .6s ease;
      will-change:transform;
    }
    .photo:hover{transform:scale(1.04) rotateY(-2deg)!important;box-shadow:0 16px 60px rgba(124,58,237,.25)}
    .photo--wide{width:100%;max-width:420px;height:260px}
    /* Staggered depth: front and back layers */
    .photos .photo:nth-child(1){transform:translateZ(30px) rotateY(3deg)}
    .photos .photo:nth-child(2){transform:translateZ(-20px) rotateY(-3deg);margin-top:3rem}
    .photo img{width:100%;height:100%;object-fit:cover}
    .photo__empty{color:rgba(255,255,255,.15);font-size:.72rem;text-align:center;display:flex;flex-direction:column;align-items:center;gap:.5rem}
    /* Parallax data attributes for JS */
    [data-speed]{will-change:transform}

    /* Reveal animation */
    .reveal-item{opacity:0;transform:translateY(40px);transition:opacity .8s cubic-bezier(.4,0,.2,1),transform .8s cubic-bezier(.4,0,.2,1)}
    .in-view .reveal-item{opacity:1;transform:translateY(0)}
    .in-view .reveal-item:nth-child(2){transition-delay:.15s}

    /* Ending */
    .scene--ending{text-align:center;flex-direction:column}
    .scene--ending .story__title{font-size:clamp(1.8rem,4vw,3rem)}
    .ending__btn{display:inline-block;margin-top:1.5rem;padding:.7rem 2rem;border:1px solid rgba(255,255,255,.2);
      border-radius:30px;color:#fff;text-decoration:none;font-size:.78rem;font-weight:500;letter-spacing:.08em;transition:all .3s}
    .ending__btn:hover{background:#fff;color:#000}

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

<div class="grain"></div>
<div id="progress"></div>
<canvas id="c"></canvas>

<nav class="topbar">
  <a href="/">&larr; Home</a>
  <a href="/" class="topbar__logo">LILY TAN</a>
  <a href="/cv/">CV &rarr;</a>
</nav>

<div class="counter"><span id="secNum">01</span> / 06</div>

<div class="dots" id="dots">
  <div class="dots__item active" data-label="Intro" data-idx="0"></div>
  <div class="dots__item" data-label="Origin" data-idx="1"></div>
  <div class="dots__item" data-label="Journey" data-idx="2"></div>
  <div class="dots__item" data-label="Explore" data-idx="3"></div>
  <div class="dots__item" data-label="Connect" data-idx="4"></div>
  <div class="dots__item" data-label="Moments" data-idx="5"></div>
</div>

<!-- ===== REAL SCROLLABLE CONTENT ===== -->

<!-- 0: Hero -->
<section class="scene scene--hero" data-idx="0">
  <div class="hero__title">Beyond the<br><em>Research</em></div>
  <div class="hero__sub">A personal story told through light, space, and memory</div>
  <div class="hero__scroll">Scroll to begin</div>
</section>

<!-- 1: Origin -->
<section class="scene" data-idx="1">
  <div class="scene__content">
    <div class="story">
      <div class="reveal-item" data-speed="0.8">
        <div class="story__label">01 &mdash; Origin</div>
        <div class="story__title">Where It<br>All <em>Began</em></div>
        <div class="story__divider"></div>
        <div class="story__text">Every story has a beginning. Mine starts with curiosity, family, and the places that first made me wonder about the world.</div>
      </div>
      <div class="reveal-item" data-speed="1.3">
        <div class="photo" data-speed="1.5" data-tilt="3">
          <div class="photo__empty">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
            Add photo
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 2: Journey -->
<section class="scene" data-idx="2">
  <div class="scene__content">
    <div class="story story--reverse">
      <div class="reveal-item" data-speed="0.7">
        <div class="story__label">02 &mdash; Journey</div>
        <div class="story__title">The Academic<br><em>Path</em></div>
        <div class="story__divider"></div>
        <div class="story__text">From classrooms to conferences, from late-night coding to early-morning writing. The path of a researcher is never straight, but always meaningful.</div>
      </div>
      <div class="reveal-item" data-speed="1.2">
        <div class="photos">
          <div class="photo" data-speed="1.6" data-tilt="-4">
            <div class="photo__empty">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              Add photo
            </div>
          </div>
          <div class="photo" data-speed="0.6" data-tilt="5">
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

<!-- 3: Explore -->
<section class="scene" data-idx="3">
  <div class="scene__content">
    <div class="story">
      <div class="reveal-item" data-speed="0.9">
        <div class="story__label">03 &mdash; Explore</div>
        <div class="story__title">Exploring<br>the <em>World</em></div>
        <div class="story__divider"></div>
        <div class="story__text">Travel broadens the mind and feeds the soul. Every new place brings fresh perspectives that find their way back into my work.</div>
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

<!-- 4: Connect -->
<section class="scene" data-idx="4">
  <div class="scene__content">
    <div class="story story--reverse">
      <div class="reveal-item" data-speed="0.75">
        <div class="story__label">04 &mdash; Connect</div>
        <div class="story__title">People &amp;<br><em>Connection</em></div>
        <div class="story__divider"></div>
        <div class="story__text">The mentors who guided me, the friends who supported me, and the communities that inspired me. Research is never a solo endeavor.</div>
      </div>
      <div class="reveal-item" data-speed="1.3">
        <div class="photos">
          <div class="photo" data-speed="1.7" data-tilt="4">
            <div class="photo__empty">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              Add photo
            </div>
          </div>
          <div class="photo" data-speed="0.5" data-tilt="-5">
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

<!-- 5: Moments -->
<section class="scene" data-idx="5">
  <div class="scene__content">
    <div class="story story--center">
      <div class="reveal-item">
        <div class="story__label">05 &mdash; Moments</div>
        <div class="story__title">Little<br><em>Moments</em></div>
        <div class="story__divider"></div>
        <div class="story__text">A perfect cup of coffee, a sunset walk, a book that changed everything. The small things that make life extraordinary.</div>
      </div>
    </div>
  </div>
</section>

<!-- 6: Ending -->
<section class="scene scene--ending" data-idx="6">
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
  /* ===== Three.js ===== */
  var W = window.innerWidth, H = window.innerHeight;
  var renderer = new THREE.WebGLRenderer({canvas:document.getElementById('c'), antialias:true});
  renderer.setSize(W, H);
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setClearColor(0x050505);

  var scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x050505, 0.06);

  var camera = new THREE.PerspectiveCamera(60, W/H, 0.1, 100);
  camera.position.set(0, 0, 20);

  // Lights
  scene.add(new THREE.AmbientLight(0xffffff, 0.3));
  var ptLight = new THREE.PointLight(0xffffff, 1.2, 50);
  ptLight.position.set(0, 5, 15);
  scene.add(ptLight);

  /* ===== Flowing Particle Ribbons ===== */
  // Define multiple ribbon curves that flow through the 3D space
  var ribbonCurves = [
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(-15,2,5), new THREE.Vector3(-5,4,0), new THREE.Vector3(0,1,-5),
      new THREE.Vector3(8,-2,-10), new THREE.Vector3(15,0,-18), new THREE.Vector3(5,3,-25),
      new THREE.Vector3(-10,1,-32), new THREE.Vector3(0,-1,-40)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(12,-3,8), new THREE.Vector3(4,-1,2), new THREE.Vector3(-3,2,-3),
      new THREE.Vector3(-10,0,-8), new THREE.Vector3(-5,-3,-15), new THREE.Vector3(8,1,-22),
      new THREE.Vector3(12,-2,-30), new THREE.Vector3(0,2,-38)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(-8,-4,6), new THREE.Vector3(2,-2,1), new THREE.Vector3(6,3,-4),
      new THREE.Vector3(-2,5,-10), new THREE.Vector3(-8,-1,-16), new THREE.Vector3(3,-3,-24),
      new THREE.Vector3(-5,4,-30), new THREE.Vector3(2,0,-38)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(5,5,7), new THREE.Vector3(-2,3,2), new THREE.Vector3(-7,-1,-4),
      new THREE.Vector3(3,-4,-9), new THREE.Vector3(10,2,-14), new THREE.Vector3(-3,5,-20),
      new THREE.Vector3(-8,-2,-28), new THREE.Vector3(4,1,-36)
    ], false, 'catmullrom', 0.3),
    new THREE.CatmullRomCurve3([
      new THREE.Vector3(0,-5,9), new THREE.Vector3(7,0,3), new THREE.Vector3(-4,4,-2),
      new THREE.Vector3(-12,-2,-8), new THREE.Vector3(2,3,-13), new THREE.Vector3(8,-4,-20),
      new THREE.Vector3(-6,0,-27), new THREE.Vector3(-2,-3,-35)
    ], false, 'catmullrom', 0.3)
  ];

  // Create particle systems for each ribbon
  var ribbons = [];
  var PARTICLES_PER_RIBBON = 1200;

  ribbonCurves.forEach(function(curve, ri) {
    var geo = new THREE.BufferGeometry();
    var positions = new Float32Array(PARTICLES_PER_RIBBON * 3);
    var basePositions = new Float32Array(PARTICLES_PER_RIBBON * 3); // store original positions
    var sizes = new Float32Array(PARTICLES_PER_RIBBON);
    var opacities = new Float32Array(PARTICLES_PER_RIBBON);

    for (var i = 0; i < PARTICLES_PER_RIBBON; i++) {
      var t = i / PARTICLES_PER_RIBBON;
      var pt = curve.getPointAt(t);
      // Add slight random spread perpendicular to the ribbon
      var spread = 0.15 + Math.random() * 0.3;
      var angle = Math.random() * Math.PI * 2;
      positions[i*3]   = pt.x + Math.cos(angle) * spread;
      positions[i*3+1] = pt.y + Math.sin(angle) * spread;
      positions[i*3+2] = pt.z + (Math.random() - 0.5) * 0.3;
      basePositions[i*3]   = positions[i*3];
      basePositions[i*3+1] = positions[i*3+1];
      basePositions[i*3+2] = positions[i*3+2];
      sizes[i] = 0.02 + Math.random() * 0.04;
      opacities[i] = 0.3 + Math.random() * 0.5;
    }

    geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    // Site palette colors for each ribbon
    var ribbonColors = [0x7c3aed, 0xf75092, 0x3b82f6, 0x047857, 0xf59e0b];
    var mat = new THREE.PointsMaterial({
      color: ribbonColors[ri % ribbonColors.length],
      size: 0.05,
      transparent: true,
      opacity: 0.65,
      sizeAttenuation: true
    });

    var points = new THREE.Points(geo, mat);
    scene.add(points);
    ribbons.push({
      points: points,
      geo: geo,
      base: basePositions,
      curve: curve,
      speed: 0.15 + ri * 0.05,
      waveAmp: 0.08 + ri * 0.03,
      waveFreq: 1.5 + ri * 0.4
    });
  });

  // Scattered dust particles
  var dustGeo = new THREE.BufferGeometry();
  var dustArr = new Float32Array(300 * 3);
  for (var i = 0; i < 300; i++) {
    dustArr[i*3]   = (Math.random() - 0.5) * 30;
    dustArr[i*3+1] = (Math.random() - 0.5) * 20;
    dustArr[i*3+2] = 10 - Math.random() * 50;
  }
  dustGeo.setAttribute('position', new THREE.BufferAttribute(dustArr, 3));
  var dust = new THREE.Points(dustGeo, new THREE.PointsMaterial({
    color: 0xffffff, size: 0.015, transparent: true, opacity: 0.2
  }));
  scene.add(dust);

  /* ===== Scroll tracking ===== */
  var sections = document.querySelectorAll('.scene');
  var totalH, scrollProg=0, smoothProg=0;

  function measure(){
    totalH = document.documentElement.scrollHeight - window.innerHeight;
  }
  measure();
  window.addEventListener('resize',function(){
    W=innerWidth; H=innerHeight;
    camera.aspect=W/H; camera.updateProjectionMatrix();
    renderer.setSize(W,H);
    measure();
  });

  window.addEventListener('scroll',function(){
    scrollProg = totalH > 0 ? window.pageYOffset / totalH : 0;
    // Parallax: move elements at different speeds
    var scrollY = window.pageYOffset;
    var parallaxEls = document.querySelectorAll('[data-speed]');
    parallaxEls.forEach(function(el){
      var speed = parseFloat(el.getAttribute('data-speed'));
      var tilt = parseFloat(el.getAttribute('data-tilt')) || 0;
      var rect = el.getBoundingClientRect();
      var center = rect.top + rect.height/2;
      var offset = (center - H/2) * (speed - 1) * 0.3;
      var rotY = tilt * Math.sin(scrollY * 0.002);
      el.style.transform = 'translateY('+offset+'px) rotateY('+rotY+'deg)';
    });
  },{passive:true});

  /* ===== Intersection Observer for reveal ===== */
  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting) e.target.classList.add('in-view');
    });
  },{threshold:0.25});
  sections.forEach(function(s){observer.observe(s);});

  /* ===== UI refs ===== */
  var dots=document.querySelectorAll('.dots__item');
  var secNum=document.getElementById('secNum');
  var progBar=document.getElementById('progress');

  /* ===== Render ===== */
  var clock=new THREE.Clock();

  function render(){
    requestAnimationFrame(render);
    var el=clock.getElapsedTime();

    // Smooth camera interpolation
    smoothProg += (scrollProg - smoothProg) * 0.05;
    var t = smoothProg;

    // Camera: scroll drives Z position through the ribbon world
    var camZ = 20 - t * 55; // move from z=20 to z=-35
    var camX = Math.sin(t * Math.PI * 2) * 3; // gentle sway
    var camY = Math.cos(t * Math.PI * 1.5) * 2;
    camera.position.set(camX, camY, camZ);
    camera.lookAt(camX * 0.3, camY * 0.3, camZ - 8);

    // Light follows camera
    ptLight.position.set(camX + 3, camY + 4, camZ + 3);
    ptLight.intensity = 1.0 + Math.sin(el * 0.5) * 0.3;

    // Animate ribbon particles — flowing wave motion driven by scroll + time
    for (var ri = 0; ri < ribbons.length; ri++) {
      var rb = ribbons[ri];
      var positions = rb.geo.attributes.position.array;
      var base = rb.base;
      var scrollWave = t * 10; // scroll drives wave phase

      for (var i = 0; i < PARTICLES_PER_RIBBON; i++) {
        var along = i / PARTICLES_PER_RIBBON;
        // Wave displacement perpendicular to ribbon
        var wave = Math.sin(along * rb.waveFreq * 6.28 + el * rb.speed * 3 + scrollWave + ri) * rb.waveAmp;
        var wave2 = Math.cos(along * rb.waveFreq * 4 + el * rb.speed * 2 + scrollWave * 0.7) * rb.waveAmp * 0.6;

        positions[i*3]   = base[i*3]   + wave;
        positions[i*3+1] = base[i*3+1] + wave2;
        positions[i*3+2] = base[i*3+2] + Math.sin(along * 3 + el * rb.speed) * 0.05;
      }
      rb.geo.attributes.position.needsUpdate = true;

      // Vary opacity based on proximity to camera
      var distZ = Math.abs(rb.curve.getPointAt(0.5).z - camZ);
      rb.points.material.opacity = Math.max(0.15, Math.min(0.7, 1 - distZ * 0.03));
    }

    // Dust rotation
    dust.rotation.y = el * 0.005;
    dust.rotation.x = Math.sin(el * 0.003) * 0.05;

    // Dynamic fog
    scene.fog.density = 0.04 + t * 0.02;

    // UI updates
    var idx=Math.min(Math.floor(smoothProg*sections.length), sections.length-1);
    secNum.textContent=('0'+(idx+1)).slice(-2);
    progBar.style.width=(smoothProg*100)+'%';
    dots.forEach(function(d,i){d.classList.toggle('active',i===idx);});

    renderer.render(scene,camera);
  }
  render();

  /* ===== Dots nav ===== */
  dots.forEach(function(d){
    d.addEventListener('click',function(){
      var i=parseInt(d.getAttribute('data-idx'));
      sections[i].scrollIntoView({behavior:'smooth'});
    });
  });

})();
</script>
</body>
</html>
