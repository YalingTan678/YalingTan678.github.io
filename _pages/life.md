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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior: smooth; }
    body { font-family:'Inter',system-ui,sans-serif; background:#0a0a1a; color:#e2e8f0; overflow-x:hidden; }

    /* ===== 3D Canvas (fixed background) ===== */
    #scene-canvas { position:fixed; top:0; left:0; width:100%; height:100%; z-index:0; }

    /* ===== Top Nav ===== */
    .life-nav {
      position:fixed; top:0; left:0; right:0; z-index:100;
      display:flex; align-items:center; justify-content:space-between;
      padding:1rem 2.5rem;
      background:linear-gradient(180deg,rgba(10,10,26,0.85) 0%,transparent 100%);
      backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px);
      transition:background 0.4s;
    }
    .life-nav__logo { font-size:1.1rem; font-weight:700; color:#fff; text-decoration:none; letter-spacing:-0.02em; }
    .life-nav__logo span { background:linear-gradient(135deg,#7c3aed,#f75092); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    .life-nav__links { display:flex; gap:0.3rem; }
    .life-nav__links a {
      padding:0.4rem 0.9rem; border-radius:20px; font-size:0.78rem; font-weight:500;
      color:rgba(255,255,255,0.6); text-decoration:none; transition:all 0.3s;
      border:1px solid transparent;
    }
    .life-nav__links a:hover, .life-nav__links a.active {
      color:#fff; background:rgba(124,58,237,0.2); border-color:rgba(124,58,237,0.3);
    }
    .life-nav__back {
      font-size:0.78rem; color:rgba(255,255,255,0.5); text-decoration:none;
      transition:color 0.3s; display:flex; align-items:center; gap:0.4rem;
    }
    .life-nav__back:hover { color:#fff; }

    /* ===== Scroll Container ===== */
    .scroll-container { position:relative; z-index:1; }

    /* ===== Hero ===== */
    .life-hero {
      height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center;
      text-align:center; position:relative;
    }
    .life-hero h1 {
      font-size:clamp(2.5rem,6vw,4.5rem); font-weight:800; letter-spacing:-0.03em;
      background:linear-gradient(135deg,#fff 0%,#c4b5fd 50%,#f9a8d4 100%);
      -webkit-background-clip:text; -webkit-text-fill-color:transparent;
      margin-bottom:0.8rem; line-height:1.1;
    }
    .life-hero p { font-size:1.1rem; color:rgba(255,255,255,0.5); font-weight:300; max-width:500px; line-height:1.7; }
    .scroll-hint {
      position:absolute; bottom:2.5rem; display:flex; flex-direction:column; align-items:center; gap:0.5rem;
      color:rgba(255,255,255,0.3); font-size:0.72rem; letter-spacing:0.1em; text-transform:uppercase;
      animation: float 2.5s ease-in-out infinite;
    }
    .scroll-hint__arrow { width:20px; height:20px; border-right:2px solid rgba(255,255,255,0.3); border-bottom:2px solid rgba(255,255,255,0.3); transform:rotate(45deg); }
    @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(8px)} }

    /* ===== Story Sections ===== */
    .story-section {
      min-height:100vh; display:flex; align-items:center; padding:6rem 2rem;
      position:relative;
    }
    .story-section__inner {
      max-width:1100px; margin:0 auto; width:100%;
      display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center;
    }
    .story-section:nth-child(odd) .story-section__inner { direction:rtl; }
    .story-section:nth-child(odd) .story-section__inner > * { direction:ltr; }

    .story-content { position:relative; }
    .story-content__label {
      font-size:0.68rem; font-weight:600; letter-spacing:0.15em; text-transform:uppercase;
      margin-bottom:0.8rem; display:inline-block; padding:0.3rem 0.8rem; border-radius:20px;
    }
    .story-content h2 {
      font-size:clamp(1.8rem,3.5vw,2.8rem); font-weight:800; letter-spacing:-0.02em;
      line-height:1.15; margin-bottom:1rem;
    }
    .story-content p { font-size:0.95rem; color:rgba(255,255,255,0.55); line-height:1.8; }

    /* Photo grid */
    .photo-grid { display:grid; gap:0.8rem; }
    .photo-grid--duo { grid-template-columns:1fr 1fr; }
    .photo-grid--trio { grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; }
    .photo-grid--trio .photo-card:first-child { grid-row:1/3; }
    .photo-grid--single { grid-template-columns:1fr; }

    .photo-card {
      border-radius:16px; overflow:hidden; position:relative;
      background:linear-gradient(135deg,rgba(124,58,237,0.1),rgba(247,80,146,0.1));
      border:1px solid rgba(255,255,255,0.06);
      aspect-ratio:4/3; transition:transform 0.5s cubic-bezier(0.4,0,0.2,1), box-shadow 0.5s;
    }
    .photo-card:hover { transform:scale(1.03) translateY(-4px); box-shadow:0 20px 60px rgba(124,58,237,0.2); }
    .photo-card img { width:100%; height:100%; object-fit:cover; display:block; }
    .photo-card__placeholder {
      width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;
      font-size:0.8rem; color:rgba(255,255,255,0.25); gap:0.5rem;
    }
    .photo-card__placeholder svg { width:32px; height:32px; opacity:0.3; }

    /* Section color themes */
    .theme-purple .story-content__label { color:#a78bfa; background:rgba(124,58,237,0.15); }
    .theme-purple .story-content h2 { color:#e9e0ff; }
    .theme-blue .story-content__label { color:#60a5fa; background:rgba(59,130,246,0.15); }
    .theme-blue .story-content h2 { color:#dbeafe; }
    .theme-green .story-content__label { color:#34d399; background:rgba(16,185,129,0.15); }
    .theme-green .story-content h2 { color:#d1fae5; }
    .theme-rose .story-content__label { color:#fb7185; background:rgba(244,63,94,0.15); }
    .theme-rose .story-content h2 { color:#ffe4e6; }
    .theme-amber .story-content__label { color:#fbbf24; background:rgba(245,158,11,0.15); }
    .theme-amber .story-content h2 { color:#fef3c7; }

    /* ===== Ending ===== */
    .life-ending {
      height:80vh; display:flex; flex-direction:column; align-items:center; justify-content:center;
      text-align:center; padding:2rem;
    }
    .life-ending h2 {
      font-size:clamp(2rem,4vw,3rem); font-weight:800;
      background:linear-gradient(135deg,#c4b5fd,#f9a8d4,#fcd34d);
      -webkit-background-clip:text; -webkit-text-fill-color:transparent;
      margin-bottom:1rem;
    }
    .life-ending p { color:rgba(255,255,255,0.4); font-size:1rem; max-width:450px; line-height:1.7; }
    .life-ending__btn {
      margin-top:2rem; display:inline-flex; align-items:center; gap:0.5rem;
      padding:0.7rem 1.8rem; border-radius:30px; font-size:0.85rem; font-weight:600;
      color:#fff; text-decoration:none;
      background:linear-gradient(135deg,#7c3aed,#f75092);
      box-shadow:0 4px 20px rgba(124,58,237,0.3);
      transition:transform 0.3s, box-shadow 0.3s;
    }
    .life-ending__btn:hover { transform:translateY(-2px); box-shadow:0 8px 30px rgba(124,58,237,0.5); }

    /* ===== Section reveal animation ===== */
    .reveal { opacity:0; transform:translateY(40px); transition:opacity 0.8s ease, transform 0.8s ease; }
    .reveal.visible { opacity:1; transform:translateY(0); }

    /* ===== Side dots nav ===== */
    .dot-nav {
      position:fixed; right:1.5rem; top:50%; transform:translateY(-50%); z-index:90;
      display:flex; flex-direction:column; gap:1rem; align-items:center;
    }
    .dot-nav__dot {
      width:10px; height:10px; border-radius:50%; border:2px solid rgba(255,255,255,0.25);
      background:transparent; cursor:pointer; transition:all 0.3s; position:relative;
    }
    .dot-nav__dot:hover { border-color:rgba(255,255,255,0.6); }
    .dot-nav__dot.active { background:#7c3aed; border-color:#7c3aed; transform:scale(1.3); }
    .dot-nav__dot::after {
      content:attr(data-label); position:absolute; right:22px; top:50%; transform:translateY(-50%);
      font-size:0.68rem; color:rgba(255,255,255,0.5); white-space:nowrap;
      opacity:0; transition:opacity 0.3s; pointer-events:none;
    }
    .dot-nav__dot:hover::after { opacity:1; }

    /* ===== Progress bar ===== */
    .life-progress { position:fixed; top:0; left:0; height:3px; z-index:110; border-radius:0 2px 2px 0;
      background:linear-gradient(90deg,#7c3aed,#f75092,#fbbf24); width:0%; transition:width 0.1s; }

    /* ===== Mobile ===== */
    @media(max-width:768px) {
      .story-section__inner { grid-template-columns:1fr; gap:2rem; }
      .story-section:nth-child(odd) .story-section__inner { direction:ltr; }
      .life-nav__links { display:none; }
      .dot-nav { right:0.8rem; }
      .life-nav { padding:1rem 1.5rem; }
    }
  </style>
</head>
<body>
  <!-- Progress bar -->
  <div class="life-progress" id="progress"></div>

  <!-- 3D Background -->
  <canvas id="scene-canvas"></canvas>

  <!-- Top nav -->
  <nav class="life-nav">
    <a href="/" class="life-nav__back">&larr; Back to Home</a>
    <a href="/" class="life-nav__logo">Lily <span>Tan</span></a>
    <div class="life-nav__links">
      <a href="#origin" data-section="0">Origin</a>
      <a href="#journey" data-section="1">Journey</a>
      <a href="#explore" data-section="2">Explore</a>
      <a href="#connect" data-section="3">Connect</a>
      <a href="#moments" data-section="4">Moments</a>
    </div>
  </nav>

  <!-- Side dot nav -->
  <div class="dot-nav" id="dotNav">
    <div class="dot-nav__dot active" data-section="0" data-label="Origin" onclick="scrollToSection(0)"></div>
    <div class="dot-nav__dot" data-section="1" data-label="Journey" onclick="scrollToSection(1)"></div>
    <div class="dot-nav__dot" data-section="2" data-label="Explore" onclick="scrollToSection(2)"></div>
    <div class="dot-nav__dot" data-section="3" data-label="Connect" onclick="scrollToSection(3)"></div>
    <div class="dot-nav__dot" data-section="4" data-label="Moments" onclick="scrollToSection(4)"></div>
  </div>

  <!-- ===== SCROLL CONTENT ===== -->
  <div class="scroll-container">

    <!-- HERO -->
    <section class="life-hero" id="hero" data-scene="hero">
      <h1>Beyond the<br>Research</h1>
      <p>A glimpse into the moments, places, and people that shape who I am outside the lab.</p>
      <div class="scroll-hint">
        <span>Scroll to explore</span>
        <div class="scroll-hint__arrow"></div>
      </div>
    </section>

    <!-- SECTION 1: Origin -->
    <section class="story-section theme-purple" id="origin" data-scene="origin">
      <div class="story-section__inner">
        <div class="story-content reveal">
          <div class="story-content__label">Chapter 01</div>
          <h2>Where It All Began</h2>
          <p>Every story has a beginning. Mine starts with curiosity, family, and the places that first made me wonder about the world.</p>
        </div>
        <div class="photo-grid photo-grid--duo reveal">
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: Journey -->
    <section class="story-section theme-blue" id="journey" data-scene="journey">
      <div class="story-section__inner">
        <div class="story-content reveal">
          <div class="story-content__label">Chapter 02</div>
          <h2>The Academic Journey</h2>
          <p>From classrooms to conferences, from late-night coding to early-morning writing sessions. The path of a researcher is never straight, but always meaningful.</p>
        </div>
        <div class="photo-grid photo-grid--trio reveal">
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: Explore -->
    <section class="story-section theme-green" id="explore" data-scene="explore">
      <div class="story-section__inner">
        <div class="story-content reveal">
          <div class="story-content__label">Chapter 03</div>
          <h2>Exploring the World</h2>
          <p>Travel broadens the mind and feeds the soul. Every new place brings fresh perspectives that find their way back into my work and thinking.</p>
        </div>
        <div class="photo-grid photo-grid--duo reveal">
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: Connect -->
    <section class="story-section theme-rose" id="connect" data-scene="connect">
      <div class="story-section__inner">
        <div class="story-content reveal">
          <div class="story-content__label">Chapter 04</div>
          <h2>People & Connection</h2>
          <p>The mentors who guided me, the friends who supported me, and the communities that inspired me. Research is never a solo endeavor.</p>
        </div>
        <div class="photo-grid photo-grid--trio reveal">
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
          <div class="photo-card">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: Moments -->
    <section class="story-section theme-amber" id="moments" data-scene="moments">
      <div class="story-section__inner">
        <div class="story-content reveal">
          <div class="story-content__label">Chapter 05</div>
          <h2>Little Moments</h2>
          <p>A perfect cup of coffee, a sunset walk, a book that changed everything. It is the small things that make life extraordinary.</p>
        </div>
        <div class="photo-grid photo-grid--single reveal">
          <div class="photo-card" style="aspect-ratio:16/9">
            <div class="photo-card__placeholder">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>
              <span>Add photo</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ENDING -->
    <section class="life-ending" data-scene="ending">
      <h2>The Story Continues...</h2>
      <p>Every day writes a new chapter. Thank you for taking a moment to know me beyond the publications.</p>
      <a href="/" class="life-ending__btn">&larr; Back to Home</a>
    </section>

  </div>

  <!-- ===== THREE.JS 3D SCENE ===== -->
  <script>
  (function(){
    // --- Scene Setup ---
    var canvas = document.getElementById('scene-canvas');
    var renderer = new THREE.WebGLRenderer({ canvas:canvas, antialias:true, alpha:true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    var scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x0a0a1a, 0.015);

    var camera = new THREE.PerspectiveCamera(60, window.innerWidth/window.innerHeight, 0.1, 100);
    camera.position.set(0, 0, 8);

    // --- Lights ---
    var ambientLight = new THREE.AmbientLight(0x222244, 0.6);
    scene.add(ambientLight);

    var mainLight = new THREE.PointLight(0x7c3aed, 2, 30);
    mainLight.position.set(5, 5, 5);
    scene.add(mainLight);

    var accentLight = new THREE.PointLight(0xf75092, 1.5, 25);
    accentLight.position.set(-5, -3, 3);
    scene.add(accentLight);

    var rimLight = new THREE.PointLight(0x3b82f6, 1, 20);
    rimLight.position.set(0, 5, -5);
    scene.add(rimLight);

    // --- Floating Objects ---
    var objects = [];
    var geometries = [
      new THREE.IcosahedronGeometry(0.6, 0),
      new THREE.TorusGeometry(0.5, 0.2, 16, 32),
      new THREE.OctahedronGeometry(0.5, 0),
      new THREE.TorusKnotGeometry(0.4, 0.15, 64, 8),
      new THREE.DodecahedronGeometry(0.45, 0),
      new THREE.SphereGeometry(0.35, 32, 32),
      new THREE.TetrahedronGeometry(0.5, 0),
      new THREE.ConeGeometry(0.35, 0.7, 6),
    ];
    var colors = [0x7c3aed, 0x60a5fa, 0x34d399, 0xf75092, 0xfbbf24, 0xa78bfa, 0xfb923c, 0x22d3ee];

    for (var i = 0; i < 25; i++) {
      var geo = geometries[i % geometries.length];
      var mat = new THREE.MeshPhongMaterial({
        color: colors[i % colors.length],
        transparent: true,
        opacity: 0.15 + Math.random() * 0.2,
        shininess: 100,
        wireframe: Math.random() > 0.6
      });
      var mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(
        (Math.random() - 0.5) * 20,
        (Math.random() - 0.5) * 16,
        (Math.random() - 0.5) * 12 - 3
      );
      mesh.rotation.set(Math.random()*Math.PI, Math.random()*Math.PI, 0);
      var s = 0.4 + Math.random() * 1.2;
      mesh.scale.set(s, s, s);
      mesh.userData = {
        basePos: mesh.position.clone(),
        floatSpeed: 0.3 + Math.random() * 0.7,
        floatAmp: 0.3 + Math.random() * 0.5,
        rotSpeed: { x: (Math.random()-0.5)*0.01, y: (Math.random()-0.5)*0.01 }
      };
      scene.add(mesh);
      objects.push(mesh);
    }

    // --- Particle field ---
    var particleGeo = new THREE.BufferGeometry();
    var particleCount = 300;
    var pPositions = new Float32Array(particleCount * 3);
    for (var i = 0; i < particleCount; i++) {
      pPositions[i*3] = (Math.random()-0.5)*30;
      pPositions[i*3+1] = (Math.random()-0.5)*30;
      pPositions[i*3+2] = (Math.random()-0.5)*20 - 5;
    }
    particleGeo.setAttribute('position', new THREE.BufferAttribute(pPositions, 3));
    var particleMat = new THREE.PointsMaterial({ color:0xffffff, size:0.03, transparent:true, opacity:0.4 });
    var particles = new THREE.Points(particleGeo, particleMat);
    scene.add(particles);

    // --- Scene presets for each section ---
    var sceneStates = {
      hero:    { cam:[0,0,8],    mainCol:0x7c3aed, accentCol:0xf75092, rimCol:0x3b82f6, fog:0x0a0a1a, fogDensity:0.015 },
      origin:  { cam:[2,1,7],    mainCol:0xa78bfa, accentCol:0xc084fc, rimCol:0x7c3aed, fog:0x0d0520, fogDensity:0.018 },
      journey: { cam:[-2,0.5,6], mainCol:0x3b82f6, accentCol:0x60a5fa, rimCol:0x2563eb, fog:0x050d1a, fogDensity:0.012 },
      explore: { cam:[1,-1,7],   mainCol:0x10b981, accentCol:0x34d399, rimCol:0x059669, fog:0x051a10, fogDensity:0.014 },
      connect: { cam:[-1,1,6.5], mainCol:0xf43f5e, accentCol:0xfb7185, rimCol:0xe11d48, fog:0x1a0510, fogDensity:0.016 },
      moments: { cam:[0,0.5,5],  mainCol:0xf59e0b, accentCol:0xfbbf24, rimCol:0xd97706, fog:0x1a1005, fogDensity:0.010 },
      ending:  { cam:[0,2,9],    mainCol:0x8b5cf6, accentCol:0xf9a8d4, rimCol:0xfbbf24, fog:0x0a0a1a, fogDensity:0.020 }
    };

    // --- Scroll tracking ---
    var scrollProgress = 0;
    var currentState = sceneStates.hero;
    var targetState = sceneStates.hero;
    var lerpFactor = 0;

    function getScrollData() {
      var sections = document.querySelectorAll('[data-scene]');
      var scrollY = window.pageYOffset;
      var winH = window.innerHeight;
      for (var i = sections.length - 1; i >= 0; i--) {
        var rect = sections[i].getBoundingClientRect();
        var top = rect.top + scrollY;
        if (scrollY >= top - winH * 0.5) {
          var sceneName = sections[i].getAttribute('data-scene');
          var progress = Math.min(1, Math.max(0, (scrollY - top + winH * 0.5) / winH));
          return { scene: sceneName, progress: progress, index: i };
        }
      }
      return { scene:'hero', progress:0, index:0 };
    }

    // --- Lerp helpers ---
    function lerpVal(a, b, t) { return a + (b - a) * t; }
    function lerpColor(colObj, target, t) {
      var tc = new THREE.Color(target);
      colObj.r = lerpVal(colObj.r, tc.r, t);
      colObj.g = lerpVal(colObj.g, tc.g, t);
      colObj.b = lerpVal(colObj.b, tc.b, t);
    }

    // --- Animation ---
    var clock = new THREE.Clock();
    function animate() {
      requestAnimationFrame(animate);
      var elapsed = clock.getElapsedTime();
      var dt = Math.min(clock.getDelta(), 0.05);

      // Get current scroll state
      var sd = getScrollData();
      var target = sceneStates[sd.scene] || sceneStates.hero;
      var t = 0.03; // smooth lerp speed

      // Lerp camera
      camera.position.x = lerpVal(camera.position.x, target.cam[0], t);
      camera.position.y = lerpVal(camera.position.y, target.cam[1], t);
      camera.position.z = lerpVal(camera.position.z, target.cam[2], t);
      camera.lookAt(0, 0, 0);

      // Lerp lights
      lerpColor(mainLight.color, target.mainCol, t);
      lerpColor(accentLight.color, target.accentCol, t);
      lerpColor(rimLight.color, target.rimCol, t);

      // Lerp fog
      lerpColor(scene.fog.color, target.fog, t);
      scene.fog.density = lerpVal(scene.fog.density, target.fogDensity, t);
      renderer.setClearColor(scene.fog.color, 1);

      // Float and rotate objects
      for (var i = 0; i < objects.length; i++) {
        var o = objects[i];
        var ud = o.userData;
        o.position.y = ud.basePos.y + Math.sin(elapsed * ud.floatSpeed + i) * ud.floatAmp;
        o.position.x = ud.basePos.x + Math.cos(elapsed * ud.floatSpeed * 0.7 + i * 1.3) * ud.floatAmp * 0.5;
        o.rotation.x += ud.rotSpeed.x;
        o.rotation.y += ud.rotSpeed.y;
      }

      // Rotate particles slowly
      particles.rotation.y = elapsed * 0.02;
      particles.rotation.x = Math.sin(elapsed * 0.01) * 0.1;

      renderer.render(scene, camera);
    }
    animate();

    // --- Resize ---
    window.addEventListener('resize', function() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // --- Scroll: update nav, progress, reveals ---
    var dots = document.querySelectorAll('.dot-nav__dot');
    var navLinks = document.querySelectorAll('.life-nav__links a');
    var progressBar = document.getElementById('progress');
    var reveals = document.querySelectorAll('.reveal');

    window.addEventListener('scroll', function() {
      var scrollY = window.pageYOffset;
      var docH = document.documentElement.scrollHeight - window.innerHeight;
      var pct = docH > 0 ? (scrollY / docH) * 100 : 0;
      progressBar.style.width = pct + '%';

      // Update active dot & nav link
      var sd = getScrollData();
      dots.forEach(function(d, i) {
        d.classList.toggle('active', i === sd.index);
      });
      navLinks.forEach(function(a) {
        a.classList.toggle('active', parseInt(a.getAttribute('data-section')) === sd.index - 1);
      });

      // Reveal elements
      reveals.forEach(function(el) {
        var rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.8) {
          el.classList.add('visible');
        }
      });
    }, { passive:true });

    // --- Scroll to section ---
    window.scrollToSection = function(idx) {
      var sections = document.querySelectorAll('[data-scene]');
      if (sections[idx]) {
        sections[idx].scrollIntoView({ behavior:'smooth' });
      }
    };

    // --- Nav link click ---
    navLinks.forEach(function(a) {
      a.addEventListener('click', function(e) {
        e.preventDefault();
        var idx = parseInt(a.getAttribute('data-section')) + 1;
        window.scrollToSection(idx);
      });
    });

  })();
  </script>
</body>
</html>
