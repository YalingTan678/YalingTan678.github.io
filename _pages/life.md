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

  <!-- Libs -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html, body { overscroll-behavior:none; }
    body {
      font-family:'Inter',system-ui,-apple-system,sans-serif;
      background:#000; color:#fff; overflow-x:hidden;
    }

    /* ===== 3D Canvas fixed background ===== */
    #c { position:fixed; inset:0; z-index:0; pointer-events:none; }

    /* ===== Global overlay grain ===== */
    .grain {
      position:fixed; inset:0; z-index:9999; pointer-events:none; opacity:0.04;
      background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
      background-size:128px 128px;
    }

    /* ===== Progress ===== */
    #progress {
      position:fixed; top:0; left:0; height:2px; z-index:200;
      background:#fff; width:0%; transform-origin:left;
    }

    /* ===== Top Bar ===== */
    .topbar {
      position:fixed; top:0; left:0; right:0; z-index:100;
      display:flex; justify-content:space-between; align-items:center;
      padding:1.8rem 3rem; mix-blend-mode:difference;
    }
    .topbar a { color:#fff; text-decoration:none; font-size:0.75rem; font-weight:500;
      letter-spacing:0.12em; text-transform:uppercase; transition:opacity 0.3s; }
    .topbar a:hover { opacity:0.5; }
    .topbar__logo { font-size:0.85rem; font-weight:700; letter-spacing:0.05em; }

    /* ===== Side counter ===== */
    .counter {
      position:fixed; right:3rem; bottom:3rem; z-index:100;
      font-size:0.7rem; letter-spacing:0.15em; text-transform:uppercase;
      color:rgba(255,255,255,0.4); mix-blend-mode:difference;
    }
    .counter span { color:#fff; font-weight:600; font-size:1rem; }

    /* ===== Scroll spacer — each section = 100vh of scroll ===== */
    .scroll-space { height:600vh; position:relative; z-index:1; width:100%; }
    .sec-marker { width:100%; pointer-events:none; }

    /* ===== Fixed UI overlay panels ===== */
    .panels { position:fixed; inset:0; z-index:10; pointer-events:none; }

    .panel {
      position:absolute; inset:0;
      display:flex; align-items:center; justify-content:center;
      opacity:0; visibility:hidden;
      transition:none; /* GSAP controls */
    }

    /* Panel layout variants */
    .panel--hero { flex-direction:column; text-align:center; }
    .panel--left .panel__inner { margin-right:auto; margin-left:8vw; max-width:480px; }
    .panel--right .panel__inner { margin-left:auto; margin-right:8vw; max-width:480px; }
    .panel--center .panel__inner { text-align:center; max-width:560px; }

    .panel__label {
      font-size:0.65rem; font-weight:600; letter-spacing:0.2em; text-transform:uppercase;
      color:rgba(255,255,255,0.35); margin-bottom:1.2rem;
      display:inline-block;
    }
    .panel__title {
      font-family:'Playfair Display',serif; font-size:clamp(2.2rem,5vw,4rem);
      font-weight:400; line-height:1.12; letter-spacing:-0.02em;
      margin-bottom:1.2rem;
    }
    .panel__title em { font-style:italic; font-weight:400; }
    .panel__text {
      font-size:0.92rem; font-weight:300; line-height:1.85;
      color:rgba(255,255,255,0.5); max-width:380px;
    }
    .panel__divider {
      width:40px; height:1px; background:rgba(255,255,255,0.2);
      margin:1.5rem 0;
    }

    /* Hero specific */
    .hero__title {
      font-family:'Playfair Display',serif;
      font-size:clamp(3rem,8vw,7rem); font-weight:400; letter-spacing:-0.03em;
      line-height:1.05;
    }
    .hero__title em { font-style:italic; }
    .hero__sub {
      margin-top:1.5rem; font-size:0.85rem; font-weight:300;
      color:rgba(255,255,255,0.35); letter-spacing:0.05em;
    }
    .hero__scroll {
      position:absolute; bottom:3rem; left:50%; transform:translateX(-50%);
      font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase;
      color:rgba(255,255,255,0.3);
    }
    .hero__scroll::after {
      content:''; display:block; width:1px; height:40px;
      background:linear-gradient(rgba(255,255,255,0.3),transparent);
      margin:0.8rem auto 0;
    }

    /* Photo frames inside panels */
    .panel__photo {
      width:280px; height:360px; border-radius:6px; overflow:hidden;
      border:1px solid rgba(255,255,255,0.08);
      background:rgba(255,255,255,0.03);
      display:flex; align-items:center; justify-content:center;
      position:relative; pointer-events:auto;
    }
    .panel__photo img { width:100%; height:100%; object-fit:cover; }
    .panel__photo--wide { width:400px; height:260px; }
    .panel__photo-placeholder {
      color:rgba(255,255,255,0.15); font-size:0.72rem; text-align:center;
      display:flex; flex-direction:column; align-items:center; gap:0.5rem;
    }

    /* Dual photo layout */
    .panel__photos {
      display:flex; gap:1rem; pointer-events:auto;
    }
    .panel__photos .panel__photo { width:220px; height:300px; }
    .panel__photos .panel__photo:nth-child(2) { margin-top:3rem; }

    /* Ending */
    .panel--ending .panel__title {
      font-size:clamp(1.8rem,4vw,3rem);
    }
    .panel__btn {
      display:inline-block; margin-top:1.5rem; padding:0.7rem 2rem;
      border:1px solid rgba(255,255,255,0.2); border-radius:30px;
      color:#fff; text-decoration:none; font-size:0.78rem; font-weight:500;
      letter-spacing:0.08em; transition:all 0.3s; pointer-events:auto;
    }
    .panel__btn:hover { background:#fff; color:#000; }

    /* ===== Right nav dots ===== */
    .dots {
      position:fixed; right:2.5rem; top:50%; transform:translateY(-50%); z-index:100;
      display:flex; flex-direction:column; gap:1.2rem;
      mix-blend-mode:difference;
    }
    .dots__item {
      width:6px; height:6px; border-radius:50%; background:rgba(255,255,255,0.25);
      cursor:pointer; transition:all 0.4s; position:relative;
    }
    .dots__item.active { background:#fff; transform:scale(1.6); }
    .dots__item::after {
      content:attr(data-label); position:absolute; right:18px; top:50%;
      transform:translateY(-50%); font-size:0.6rem; letter-spacing:0.1em;
      text-transform:uppercase; white-space:nowrap; opacity:0; transition:opacity 0.3s;
      color:rgba(255,255,255,0.5);
    }
    .dots__item:hover::after { opacity:1; }

    /* ===== Mobile ===== */
    @media(max-width:768px) {
      .topbar { padding:1.2rem 1.5rem; }
      .panel--left .panel__inner, .panel--right .panel__inner { margin:0 auto; padding:0 1.5rem; text-align:center; }
      .panel__photos { flex-direction:column; align-items:center; }
      .panel__photos .panel__photo:nth-child(2) { margin-top:0; }
      .panel__photo { width:220px!important; height:280px!important; }
      .dots { right:1rem; }
      .counter { right:1.5rem; bottom:1.5rem; }
    }
  </style>
</head>
<body>

<!-- Film grain overlay -->
<div class="grain"></div>

<!-- Progress bar -->
<div id="progress"></div>

<!-- 3D Canvas -->
<canvas id="c"></canvas>

<!-- Top bar -->
<nav class="topbar">
  <a href="/">&#8592; Home</a>
  <a href="/" class="topbar__logo">LILY TAN</a>
  <a href="/cv/">CV &#8594;</a>
</nav>

<!-- Section counter -->
<div class="counter"><span id="secNum">01</span> / 06</div>

<!-- Right dots -->
<div class="dots" id="dots">
  <div class="dots__item active" data-label="Intro" data-idx="0"></div>
  <div class="dots__item" data-label="Origin" data-idx="1"></div>
  <div class="dots__item" data-label="Journey" data-idx="2"></div>
  <div class="dots__item" data-label="Explore" data-idx="3"></div>
  <div class="dots__item" data-label="Connect" data-idx="4"></div>
  <div class="dots__item" data-label="Moments" data-idx="5"></div>
</div>

<!-- ===== UI Panels (fixed, toggled by GSAP) ===== -->
<div class="panels">

  <!-- 0: Hero -->
  <div class="panel panel--hero" id="p0" style="opacity:1;visibility:visible">
    <div class="hero__title">Beyond the<br><em>Research</em></div>
    <div class="hero__sub">A personal story told through light, space, and memory</div>
    <div class="hero__scroll">Scroll to begin<span></span></div>
  </div>

  <!-- 1: Origin -->
  <div class="panel panel--left" id="p1">
    <div class="panel__inner">
      <div class="panel__label">01 &mdash; Origin</div>
      <div class="panel__title">Where It<br>All <em>Began</em></div>
      <div class="panel__divider"></div>
      <div class="panel__text">Every story has a beginning. Mine starts with curiosity, family, and the places that first made me wonder about the world.</div>
    </div>
    <div class="panel__photo" style="position:absolute;right:8vw">
      <div class="panel__photo-placeholder">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
        Add photo
      </div>
    </div>
  </div>

  <!-- 2: Journey -->
  <div class="panel panel--right" id="p2">
    <div class="panel__photos" style="position:absolute;left:8vw">
      <div class="panel__photo">
        <div class="panel__photo-placeholder">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          Add photo
        </div>
      </div>
      <div class="panel__photo">
        <div class="panel__photo-placeholder">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          Add photo
        </div>
      </div>
    </div>
    <div class="panel__inner">
      <div class="panel__label">02 &mdash; Journey</div>
      <div class="panel__title">The Academic<br><em>Path</em></div>
      <div class="panel__divider"></div>
      <div class="panel__text">From classrooms to conferences, from late-night coding to early-morning writing. The path of a researcher is never straight, but always meaningful.</div>
    </div>
  </div>

  <!-- 3: Explore -->
  <div class="panel panel--left" id="p3">
    <div class="panel__inner">
      <div class="panel__label">03 &mdash; Explore</div>
      <div class="panel__title">Exploring<br>the <em>World</em></div>
      <div class="panel__divider"></div>
      <div class="panel__text">Travel broadens the mind and feeds the soul. Every new place brings fresh perspectives that find their way back into my work.</div>
    </div>
    <div class="panel__photo panel__photo--wide" style="position:absolute;right:8vw">
      <div class="panel__photo-placeholder">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
        Add photo
      </div>
    </div>
  </div>

  <!-- 4: Connect -->
  <div class="panel panel--right" id="p4">
    <div class="panel__photos" style="position:absolute;left:8vw">
      <div class="panel__photo">
        <div class="panel__photo-placeholder">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          Add photo
        </div>
      </div>
      <div class="panel__photo">
        <div class="panel__photo-placeholder">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
          Add photo
        </div>
      </div>
    </div>
    <div class="panel__inner">
      <div class="panel__label">04 &mdash; Connect</div>
      <div class="panel__title">People &<br><em>Connection</em></div>
      <div class="panel__divider"></div>
      <div class="panel__text">The mentors who guided me, the friends who supported me, and the communities that inspired me. Research is never a solo endeavor.</div>
    </div>
  </div>

  <!-- 5: Moments -->
  <div class="panel panel--center" id="p5">
    <div class="panel__inner">
      <div class="panel__label">05 &mdash; Moments</div>
      <div class="panel__title">Little<br><em>Moments</em></div>
      <div class="panel__divider" style="margin-left:auto;margin-right:auto"></div>
      <div class="panel__text" style="margin:0 auto">A perfect cup of coffee, a sunset walk, a book that changed everything. The small things that make life extraordinary.</div>
    </div>
  </div>

  <!-- 6: Ending -->
  <div class="panel panel--hero panel--ending" id="p6">
    <div class="panel__inner" style="text-align:center">
      <div class="panel__title">The Story<br><em>Continues</em>...</div>
      <div class="panel__text" style="margin:0 auto">Thank you for taking a moment to know me beyond the publications.</div>
      <a href="/" class="panel__btn">Back to Home &#8594;</a>
    </div>
  </div>

</div>

<!-- ===== Scroll spacer with section markers ===== -->
<div class="scroll-space">
  <div class="sec-marker" data-panel="0" style="position:absolute;top:0;height:14.28%"></div>
  <div class="sec-marker" data-panel="1" style="position:absolute;top:14.28%;height:14.28%"></div>
  <div class="sec-marker" data-panel="2" style="position:absolute;top:28.57%;height:14.28%"></div>
  <div class="sec-marker" data-panel="3" style="position:absolute;top:42.85%;height:14.28%"></div>
  <div class="sec-marker" data-panel="4" style="position:absolute;top:57.14%;height:14.28%"></div>
  <div class="sec-marker" data-panel="5" style="position:absolute;top:71.42%;height:14.28%"></div>
  <div class="sec-marker" data-panel="6" style="position:absolute;top:85.71%;height:14.29%"></div>
</div>

<!-- ===== ENGINE ===== -->
<script>
(function(){
  'use strict';

  // Register GSAP plugin
  gsap.registerPlugin(ScrollTrigger);

  /* ---------- Three.js Scene ---------- */
  var canvas = document.getElementById('c');
  var renderer = new THREE.WebGLRenderer({ canvas:canvas, antialias:true, alpha:false });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setClearColor(0x000000);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;

  var scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x000000, 0.035);

  var camera = new THREE.PerspectiveCamera(50, window.innerWidth/window.innerHeight, 0.1, 200);
  camera.position.set(0, 0, 12);

  /* --- Lights --- */
  scene.add(new THREE.AmbientLight(0xffffff, 0.15));

  var keyLight = new THREE.DirectionalLight(0xffffff, 0.6);
  keyLight.position.set(5, 8, 5);
  scene.add(keyLight);

  var pointA = new THREE.PointLight(0xffffff, 1.5, 30);
  pointA.position.set(0, 0, 8);
  scene.add(pointA);

  scene.add(new THREE.PointLight(0x888899, 0.8, 25).position.set(-5, 3, -5) || new THREE.PointLight(0x888899, 0.8, 25));

  /* --- Camera path (CatmullRom spline) --- */
  var cameraPath = new THREE.CatmullRomCurve3([
    new THREE.Vector3(0, 0, 12),
    new THREE.Vector3(3, 1, 8),
    new THREE.Vector3(-2, 2, 4),
    new THREE.Vector3(4, -1, 0),
    new THREE.Vector3(-3, 0, -4),
    new THREE.Vector3(0, 3, -8),
    new THREE.Vector3(0, 0, -13)
  ], false, 'catmullrom', 0.5);

  var lookAtPath = new THREE.CatmullRomCurve3([
    new THREE.Vector3(0, 0, 0),
    new THREE.Vector3(1, 0, 4),
    new THREE.Vector3(-1, 1, 0),
    new THREE.Vector3(2, -1, -3),
    new THREE.Vector3(-1, 0, -7),
    new THREE.Vector3(0, 1, -11),
    new THREE.Vector3(0, 0, -18)
  ], false, 'catmullrom', 0.5);

  /* --- 3D Objects along path --- */
  var meshes = [];
  var geos = [
    new THREE.IcosahedronGeometry(1, 1),
    new THREE.TorusGeometry(0.8, 0.25, 16, 40),
    new THREE.OctahedronGeometry(0.9, 0),
    new THREE.TorusKnotGeometry(0.6, 0.2, 64, 8, 2, 3),
    new THREE.DodecahedronGeometry(0.7, 0),
    new THREE.IcosahedronGeometry(1.2, 0)
  ];

  for (var i = 0; i < 40; i++) {
    var pathPos = cameraPath.getPointAt(i / 40);
    var m = new THREE.Mesh(geos[i % geos.length],
      new THREE.MeshPhongMaterial({ color:0xffffff, wireframe:true, transparent:true, opacity:0.06+Math.random()*0.08 }));
    m.position.set(pathPos.x+(Math.random()-0.5)*12, pathPos.y+(Math.random()-0.5)*8, pathPos.z+(Math.random()-0.5)*6);
    var s = 0.3+Math.random()*1.5; m.scale.set(s,s,s);
    m.rotation.set(Math.random()*Math.PI, Math.random()*Math.PI, 0);
    m.userData = { rotX:(Math.random()-0.5)*0.003, rotY:(Math.random()-0.5)*0.003 };
    scene.add(m); meshes.push(m);
  }

  var solidGeos = [new THREE.SphereGeometry(0.15,32,32), new THREE.BoxGeometry(0.2,0.2,0.2), new THREE.TetrahedronGeometry(0.18)];
  for (var i = 0; i < 60; i++) {
    var pp = cameraPath.getPointAt(Math.random());
    var solid = new THREE.Mesh(solidGeos[i%solidGeos.length],
      new THREE.MeshStandardMaterial({ color:0xffffff, metalness:0.9, roughness:0.1, transparent:true, opacity:0.3+Math.random()*0.3 }));
    solid.position.set(pp.x+(Math.random()-0.5)*16, pp.y+(Math.random()-0.5)*10, pp.z+(Math.random()-0.5)*8);
    var ss = 0.3+Math.random()*0.8; solid.scale.set(ss,ss,ss);
    solid.userData = { rotX:(Math.random()-0.5)*0.005, rotY:(Math.random()-0.5)*0.005, floatSpeed:0.5+Math.random(), floatAmp:0.2+Math.random()*0.3, baseY:solid.position.y };
    scene.add(solid); meshes.push(solid);
  }

  /* --- Particles --- */
  var pGeo = new THREE.BufferGeometry();
  var pPos = new Float32Array(600*3);
  for (var i = 0; i < 600; i++) { pPos[i*3]=(Math.random()-0.5)*40; pPos[i*3+1]=(Math.random()-0.5)*30; pPos[i*3+2]=15-Math.random()*40; }
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
  var points = new THREE.Points(pGeo, new THREE.PointsMaterial({ color:0xffffff, size:0.02, transparent:true, opacity:0.5 }));
  scene.add(points);

  /* --- Path line --- */
  scene.add(new THREE.Line(
    new THREE.BufferGeometry().setFromPoints(cameraPath.getPoints(200)),
    new THREE.LineBasicMaterial({ color:0xffffff, transparent:true, opacity:0.03 })
  ));

  /* ---------- Scroll progress via native scroll listener ---------- */
  var scrollProgress = 0;
  var scrollSpace = document.querySelector('.scroll-space');

  function updateScrollProgress() {
    var rect = scrollSpace.getBoundingClientRect();
    var total = scrollSpace.offsetHeight - window.innerHeight;
    var scrolled = -rect.top;
    scrollProgress = Math.max(0, Math.min(1, scrolled / total));
  }

  window.addEventListener('scroll', updateScrollProgress, { passive:true });
  updateScrollProgress();

  /* ---------- Panel visibility via scroll ---------- */
  var totalSections = 7;
  var panels = [];
  for (var i = 0; i <= 6; i++) panels.push(document.getElementById('p'+i));
  var dots = document.querySelectorAll('.dots__item');
  var secNum = document.getElementById('secNum');
  var progressBar = document.getElementById('progress');

  function updatePanels(t) {
    var sectionSize = 1 / totalSections;
    var currentIdx = Math.min(Math.floor(t / sectionSize), totalSections - 1);
    var localT = (t - currentIdx * sectionSize) / sectionSize; // 0→1 within section

    for (var i = 0; i < totalSections; i++) {
      var panel = panels[i];
      if (!panel) continue;

      var opacity = 0;
      if (i === currentIdx) {
        // Current section: fade in first 15%, hold, fade out last 15%
        if (localT < 0.15) opacity = localT / 0.15;
        else if (localT > 0.85 && i < totalSections - 1) opacity = (1 - localT) / 0.15;
        else opacity = 1;
      }

      panel.style.opacity = opacity;
      panel.style.visibility = opacity > 0.01 ? 'visible' : 'hidden';

      // Slide up on enter
      if (i === currentIdx && localT < 0.15) {
        var yShift = 50 * (1 - localT / 0.15);
        var els = panel.querySelectorAll('.panel__inner,.panel__photo,.panel__photos,.hero__title,.hero__sub,.hero__scroll');
        els.forEach(function(c){ c.style.transform = 'translateY('+yShift+'px)'; });
      } else if (i === currentIdx) {
        var els = panel.querySelectorAll('.panel__inner,.panel__photo,.panel__photos,.hero__title,.hero__sub,.hero__scroll');
        els.forEach(function(c){ c.style.transform = 'translateY(0)'; });
      }
    }

    // Update UI
    secNum.textContent = ('0' + (currentIdx + 1)).slice(-2);
    progressBar.style.width = (t * 100) + '%';
    dots.forEach(function(d, i){ d.classList.toggle('active', i === currentIdx); });
  }

  /* ---------- Render loop ---------- */
  var clock = new THREE.Clock();
  var smoothProgress = 0;

  function render() {
    requestAnimationFrame(render);
    var elapsed = clock.getElapsedTime();

    // Smooth interpolation for buttery camera movement
    smoothProgress += (scrollProgress - smoothProgress) * 0.06;
    var t = smoothProgress;

    // Camera follows path
    camera.position.copy(cameraPath.getPointAt(Math.min(Math.max(t, 0.001), 0.999)));
    camera.lookAt(lookAtPath.getPointAt(Math.min(Math.max(t, 0.001), 0.999)));

    // Light follows camera
    pointA.position.copy(camera.position);
    pointA.position.x += 2; pointA.position.y += 1;
    pointA.intensity = 1.2 + Math.sin(elapsed * 0.5) * 0.3;

    // Dynamic fog & exposure
    scene.fog.density = 0.03 + t * 0.015;
    renderer.toneMappingExposure = 0.8 + Math.sin(t * Math.PI) * 0.4;

    // Animate objects
    for (var i = 0; i < meshes.length; i++) {
      var m = meshes[i];
      m.rotation.x += m.userData.rotX || 0;
      m.rotation.y += m.userData.rotY || 0;
      if (m.userData.floatSpeed) m.position.y = m.userData.baseY + Math.sin(elapsed * m.userData.floatSpeed + i) * m.userData.floatAmp;
    }
    points.rotation.y = elapsed * 0.01;

    // Update panels
    updatePanels(t);

    renderer.render(scene, camera);
  }
  render();

  /* ---------- Dots click ---------- */
  dots.forEach(function(d){
    d.addEventListener('click', function(){
      var idx = parseInt(d.getAttribute('data-idx'));
      var target = (idx / totalSections) * scrollSpace.offsetHeight;
      window.scrollTo({ top:target, behavior:'smooth' });
    });
  });

  /* ---------- Resize ---------- */
  window.addEventListener('resize', function(){
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

})();
</script>

</body>
</html>
