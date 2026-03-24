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
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@200;300;400;500;600;700&display=swap" rel="stylesheet"/>
  <style>
    *,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
    html,body{width:100%;overflow-x:hidden;font-family:'Inter',system-ui,sans-serif;background:#faf8ff;color:#1e1b4b}
    body.layer2-active{overflow-y:auto}
    body:not(.layer2-active){overflow-y:hidden;height:100vh}

    canvas#mainCanvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:1;pointer-events:none}

    /* Film grain overlay */
    .film-grain{position:fixed;top:0;left:0;width:100%;height:100%;z-index:9998;pointer-events:none;opacity:0.04;
      background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
      background-size:128px 128px}

    /* ====== LAYER 1: Card Landing ====== */
    #layer1{position:fixed;top:0;left:0;width:100%;height:100%;z-index:10;display:flex;align-items:center;justify-content:center}
    #layer1 .title-text{position:absolute;bottom:8%;left:50%;transform:translateX(-50%);text-align:center;z-index:12;pointer-events:none}
    #layer1 .title-text h1{font-family:'Playfair Display',serif;font-size:clamp(1.5rem,3vw,2.5rem);font-weight:400;color:rgba(30,27,75,0.6);letter-spacing:0.05em}
    #layer1 .title-text p{font-size:0.75rem;color:rgba(30,27,75,0.3);margin-top:0.5rem;letter-spacing:0.15em;text-transform:uppercase}

    /* ====== LAYER 2: Detail Page ====== */
    #layer2{display:none;position:relative;z-index:10;width:100%;height:600vh}

    /* Back button */
    .back-btn{position:fixed;top:2rem;left:2rem;z-index:100;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);
      color:rgba(255,255,255,0.6);padding:0.5rem 1.2rem;border-radius:30px;font-size:0.75rem;font-family:'Inter',sans-serif;
      letter-spacing:0.1em;cursor:pointer;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);transition:all 0.3s;display:none}
    .back-btn:hover{background:rgba(255,255,255,0.1);color:#fff}

    /* Content panels */
    .panel{position:fixed;top:0;left:0;width:100%;height:100vh;z-index:50;display:none;align-items:center;justify-content:center;
      pointer-events:none;opacity:0;transform:translateY(30px)}
    .panel.visible{display:flex}
    .panel-inner{max-width:600px;width:90%;padding:2rem;pointer-events:auto}
    .panel-number{font-size:0.7rem;letter-spacing:0.2em;color:rgba(255,255,255,0.2);margin-bottom:1rem;font-weight:300}
    .panel-title{font-family:'Playfair Display',serif;font-size:clamp(1.8rem,4vw,3rem);font-weight:400;line-height:1.2;
      color:rgba(255,255,255,0.9);margin-bottom:1rem;letter-spacing:-0.01em}
    .panel-text{font-size:0.9rem;font-weight:300;line-height:1.8;color:rgba(255,255,255,0.45);margin-bottom:1.5rem}
    .panel-photo{width:100%;height:200px;border:1px dashed rgba(255,255,255,0.15);border-radius:8px;display:flex;align-items:center;
      justify-content:center;color:rgba(255,255,255,0.2);font-size:0.75rem;letter-spacing:0.1em;background:rgba(255,255,255,0.02)}

    /* Right dot nav */
    .dot-nav{position:fixed;right:2rem;top:50%;transform:translateY(-50%);z-index:100;display:none;flex-direction:column;gap:1rem}
    .dot-nav .dot{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,0.15);cursor:pointer;transition:all 0.3s;position:relative}
    .dot-nav .dot.active{background:rgba(255,255,255,0.8);transform:scale(1.5)}
    .dot-nav .dot::after{content:attr(data-label);position:absolute;right:16px;top:50%;transform:translateY(-50%);font-size:0.6rem;
      letter-spacing:0.1em;text-transform:uppercase;white-space:nowrap;opacity:0;transition:opacity 0.3s;color:rgba(255,255,255,0.5)}
    .dot-nav .dot:hover::after{opacity:1}

    /* Progress bar */
    .progress-bar{position:fixed;top:0;left:0;height:2px;z-index:200;background:linear-gradient(90deg,#7c3aed,#f75092);width:0%;
      pointer-events:none;display:none}

    /* Section counter */
    .section-counter{position:fixed;right:2rem;bottom:2rem;z-index:100;font-size:0.7rem;letter-spacing:0.15em;
      color:rgba(255,255,255,0.2);pointer-events:none;display:none}
    .section-counter span{color:rgba(255,255,255,0.6);font-weight:600;font-size:0.9rem}

    /* Panel CTA button */
    .panel-cta{display:inline-block;padding:0.6rem 1.8rem;border-radius:30px;font-size:0.75rem;font-weight:500;letter-spacing:0.1em;
      cursor:pointer;color:#fff;background:linear-gradient(135deg,#7c3aed,#f75092);border:none;font-family:'Inter',sans-serif;
      transition:all 0.3s;pointer-events:auto}
    .panel-cta:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(124,58,237,0.4)}

    /* Mobile */
    @media(max-width:768px){
      .dot-nav{right:0.8rem}
      .section-counter{right:1rem;bottom:1rem}
      .back-btn{top:1rem;left:1rem;padding:0.4rem 0.8rem;font-size:0.65rem}
      .panel-inner{padding:1.5rem}
    }
  </style>
</head>
<body>
  <canvas id="mainCanvas"></canvas>
  <div class="film-grain"></div>

  <!-- LAYER 1: 3D Card Landing -->
  <div id="layer1">
    <div class="title-text">
      <h1>Beyond the Research</h1>
      <p>Click a card to explore</p>
    </div>
  </div>

  <!-- LAYER 2: Detail Page -->
  <div id="layer2"></div>

  <button class="back-btn" id="backBtn">&larr; Back</button>

  <div class="progress-bar" id="progressBar"></div>

  <div class="dot-nav" id="dotNav"></div>

  <div class="section-counter" id="sectionCounter"><span id="secNum">01</span> / 06</div>

  <!-- 6 panels -->
  <div class="panel" id="panel0"><div class="panel-inner"><div class="panel-number">01</div><div class="panel-title" id="pt0"></div><div class="panel-text" id="px0"></div></div></div>
  <div class="panel" id="panel1"><div class="panel-inner"><div class="panel-number">02</div><div class="panel-title" id="pt1"></div><div class="panel-text" id="px1"></div><div class="panel-photo">Add photo</div></div></div>
  <div class="panel" id="panel2"><div class="panel-inner"><div class="panel-number">03</div><div class="panel-title" id="pt2"></div><div class="panel-text" id="px2"></div></div></div>
  <div class="panel" id="panel3"><div class="panel-inner"><div class="panel-number">04</div><div class="panel-title" id="pt3"></div><div class="panel-text" id="px3"></div><div class="panel-photo">Add photo</div></div></div>
  <div class="panel" id="panel4"><div class="panel-inner"><div class="panel-number">05</div><div class="panel-title" id="pt4"></div><div class="panel-text" id="px4"></div><div class="panel-photo">Add photo</div></div></div>
  <div class="panel" id="panel5"><div class="panel-inner"><div class="panel-number">06</div><div class="panel-title" id="pt5"></div><div class="panel-text" id="px5"></div><button class="panel-cta" id="panelCta">Return to Cards</button></div></div>

<script>
(function(){

/* ====== CONTENT DATA ====== */
var THEMES = {
  pet: {
    panels: [
      { title: "A Life with Paws", text: "Some of the purest joys in life come from the companionship of animals. They teach patience, unconditional love, and the art of living in the present moment." },
      { title: "My Furry Family", text: "Every pet has a personality as unique as any person. They greet you at the door, curl up beside you while you work, and remind you that the simplest pleasures are the deepest.", photo: true },
      { title: "Daily Joy", text: "Morning walks, afternoon naps in sunbeams, evening play sessions. The rhythm of life with pets is a gentle, grounding cadence that keeps everything in perspective." },
      { title: "Grooming Love", text: "There is something meditative about caring for another living being. Brushing fur, trimming nails, preparing their favorite meals \u2014 these small acts of care are acts of love.", photo: true },
      { title: "Captured Moments", text: "Every photo tells a story. A mid-yawn portrait, a blurry action shot of zoomies, a peaceful sleeping pose. These are the moments worth preserving.", photo: true },
      { title: "Back to Cards", text: "Thank you for sharing this journey through my life with paws. There is always more to discover." }
    ]
  },
  florist: {
    panels: [
      { title: "Bloom & Craft", text: "Flowers speak a language older than words. Arranging them is my way of creating small moments of beauty in an otherwise busy world." },
      { title: "My Arrangements", text: "Each bouquet begins with intuition \u2014 a color that calls, a texture that intrigues. The arrangement grows organically, guided by an eye for balance and harmony.", photo: true },
      { title: "The Creative Process", text: "Selecting stems at the market, conditioning flowers in water, experimenting with vase shapes. The process is as rewarding as the final result." },
      { title: "Styles & Seasons", text: "Spring pastels, summer wildflowers, autumn warmth, winter minimalism. Each season brings its own palette and mood, and I love adapting to nature's rhythm.", photo: true },
      { title: "Gallery", text: "A curated collection of arrangements \u2014 from everyday table settings to special occasion centerpieces. Each one is a unique expression.", photo: true },
      { title: "Back to Cards", text: "Thank you for wandering through my floral world. Every bloom has a story." }
    ]
  },
  travel: {
    panels: [
      { title: "Wander & Wonder", text: "Travel is not just about the places you visit, but the perspectives you gain. Every journey reshapes the way I see the world and my place in it." },
      { title: "Places I've Been", text: "From bustling cities to quiet countryside, each destination leaves its mark. The architecture, the food, the light at golden hour \u2014 these details stay with me.", photo: true },
      { title: "Favorite Memories", text: "A spontaneous conversation with a stranger in a caf\u00e9. Getting lost in a neighborhood and finding the best meal of the trip. These unplanned moments are the ones I treasure most." },
      { title: "People Along the Way", text: "Travel connects you with people whose lives are beautifully different from your own. These brief encounters leave lasting impressions and broaden understanding.", photo: true },
      { title: "Postcards", text: "Snapshots from the road \u2014 sunsets, street scenes, market stalls, mountain vistas. Each image is a postcard from a moment in time.", photo: true },
      { title: "Back to Cards", text: "Thank you for traveling with me. The journey never truly ends." }
    ]
  }
};

var CARD_DATA = [
  { key: "pet",     label: "Pet Lover", img: "/images/life/pet.jpg" },
  { key: "florist", label: "Florist",   img: "/images/life/florist.jpg" },
  { key: "travel",  label: "Travel",    img: "/images/life/travel.jpg" }
];

/* ====== GLOBALS ====== */
var canvas = document.getElementById('mainCanvas');
var layer1 = document.getElementById('layer1');
var layer2 = document.getElementById('layer2');
var backBtn = document.getElementById('backBtn');
var progressBar = document.getElementById('progressBar');
var dotNav = document.getElementById('dotNav');
var sectionCounter = document.getElementById('sectionCounter');
var secNum = document.getElementById('secNum');
var panelCta = document.getElementById('panelCta');

var renderer, camera, currentScene;
var currentLayer = 1;
var animId;
var activeTheme = null;
var transitioning = false;
var entrancePlayed = false;

/* ====== RENDERER SETUP ====== */
renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0xfaf8ff, 1);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;

/* ====== LAYER 1: CARD SCENE ====== */
var cardScene, cardCamera, cardClock, cards3D = [], cardMeshes = [];
var raycaster = new THREE.Raycaster();
var mouse2 = new THREE.Vector2(-999, -999);
var mouseRaw = { x: 0, y: 0 };
var hoveredCard = null;
var starPoints;
var starBasePos;

function createCardTexture(label, imgSrc) {
  var c = document.createElement('canvas');
  c.width = 512; c.height = 720;
  var ctx = c.getContext('2d');

  // Solid dark base while image loads
  ctx.fillStyle = '#1e1b4b';
  ctx.fillRect(0, 0, 512, 720);

  // Label text at bottom with gradient overlay
  ctx.fillStyle = 'rgba(0,0,0,0.5)';
  ctx.fillRect(0, 560, 512, 160);
  var grad = ctx.createLinearGradient(0, 520, 0, 720);
  grad.addColorStop(0, 'rgba(0,0,0,0)');
  grad.addColorStop(0.3, 'rgba(0,0,0,0.6)');
  grad.addColorStop(1, 'rgba(0,0,0,0.8)');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 520, 512, 200);

  ctx.font = '700 42px Playfair Display, serif';
  ctx.textAlign = 'center';
  ctx.fillStyle = '#ffffff';
  ctx.fillText(label, 256, 660);

  var tex = new THREE.CanvasTexture(c);
  tex.needsUpdate = true;

  // Load photo and redraw
  var img = new Image();
  img.crossOrigin = 'anonymous';
  img.onload = function() {
    // Cover-fit the image
    var iw = img.width, ih = img.height;
    var cw = 512, ch = 720;
    var scale = Math.max(cw/iw, ch/ih);
    var sw = iw * scale, sh = ih * scale;
    var sx = (cw - sw) / 2, sy = (ch - sh) / 2;
    ctx.drawImage(img, sx, sy, sw, sh);

    // Bottom gradient overlay for text
    var grad2 = ctx.createLinearGradient(0, 480, 0, 720);
    grad2.addColorStop(0, 'rgba(0,0,0,0)');
    grad2.addColorStop(0.4, 'rgba(0,0,0,0.5)');
    grad2.addColorStop(1, 'rgba(0,0,0,0.75)');
    ctx.fillStyle = grad2;
    ctx.fillRect(0, 480, 512, 240);

    // Label
    ctx.font = '700 42px Playfair Display, serif';
    ctx.textAlign = 'center';
    ctx.fillStyle = '#ffffff';
    ctx.shadowColor = 'rgba(0,0,0,0.5)';
    ctx.shadowBlur = 8;
    ctx.fillText(label, 256, 660);
    ctx.shadowBlur = 0;

    tex.needsUpdate = true;
  };
  img.src = imgSrc;

  return tex;
}

function initCardScene() {
  cardScene = new THREE.Scene();
  cardCamera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);
  cardCamera.position.set(0, 0, 12);
  cardClock = new THREE.Clock();

  // Lights — bright enough to see cards
  cardScene.add(new THREE.AmbientLight(0xffffff, 0.8));
  var dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
  dirLight.position.set(0, 2, 10);
  cardScene.add(dirLight);
  var ptLight = new THREE.PointLight(0x7c3aed, 1.0, 30);
  ptLight.position.set(5, 5, 10);
  cardScene.add(ptLight);
  var ptLight2 = new THREE.PointLight(0xf75092, 0.7, 30);
  ptLight2.position.set(-5, -3, 8);
  cardScene.add(ptLight2);

  // Cards
  cards3D = [];
  cardMeshes = [];
  var positions = [
    new THREE.Vector3(-4.5, 0, 0),
    new THREE.Vector3(0, 0.3, 0.5),
    new THREE.Vector3(4.5, 0, 0)
  ];
  var rotations = [-0.15, 0, 0.15];

  for (var i = 0; i < 3; i++) {
    var tex = createCardTexture(CARD_DATA[i].label, CARD_DATA[i].img);
    var geo = new THREE.PlaneGeometry(3.5, 5);
    var mat = new THREE.MeshBasicMaterial({
      map: tex,
      transparent: true,
      opacity: 0.95,
      side: THREE.DoubleSide
    });
    var mesh = new THREE.Mesh(geo, mat);
    mesh.position.copy(positions[i]);
    mesh.rotation.y = rotations[i];
    mesh.userData = { idx: i, basePos: positions[i].clone(), baseRot: rotations[i], floatOffset: i * 2.1 };
    cardScene.add(mesh);
    cards3D.push(mesh);
    cardMeshes.push(mesh);
  }

  // Colored flowing particles (site palette)
  var particleColors = [0x7c3aed, 0x9f50d3, 0xf75092, 0xa78bfa, 0xf9a8d4];
  var totalParticles = 600;
  var starGeo = new THREE.BufferGeometry();
  var starPos = new Float32Array(totalParticles * 3);
  var starColors = new Float32Array(totalParticles * 3);
  for (var i = 0; i < totalParticles; i++) {
    starPos[i * 3] = (Math.random() - 0.5) * 35;
    starPos[i * 3 + 1] = (Math.random() - 0.5) * 25;
    starPos[i * 3 + 2] = (Math.random() - 0.5) * 15 - 3;
    var col = new THREE.Color(particleColors[i % particleColors.length]);
    starColors[i * 3] = col.r;
    starColors[i * 3 + 1] = col.g;
    starColors[i * 3 + 2] = col.b;
  }
  starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
  starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));
  starPoints = new THREE.Points(starGeo, new THREE.PointsMaterial({
    size: 0.08, transparent: true, opacity: 0.6, sizeAttenuation: true, vertexColors: true
  }));
  cardScene.add(starPoints);

  // Store base positions for mouse-driven flow
  starBasePos = new Float32Array(starPos);

  currentScene = cardScene;
  camera = cardCamera;
}

function playEntranceAnimation() {
  // Set initial state for entrance animation
  for (var i = 0; i < cards3D.length; i++) {
    cards3D[i].scale.set(0.3, 0.3, 0.3);
    cards3D[i].material.opacity = 0;
    cards3D[i].position.set(0, -1, 0);
    cards3D[i].rotation.y = 0;
  }

  // Hide title text initially
  var titleText = layer1.querySelector('.title-text');
  gsap.set(titleText, { opacity: 0 });

  var tl = gsap.timeline({
    onComplete: function() {
      entrancePlayed = true;
    }
  });

  // Phase 1 (0-2s): Arc fan-out
  var arcPositions = [
    { x: -5, y: 0.5, z: 0.5 },
    { x: 0, y: 1, z: 1 },
    { x: 5, y: 0.5, z: 0.5 }
  ];
  var arcRotations = [-0.3, 0, 0.3];

  for (var i = 0; i < cards3D.length; i++) {
    tl.to(cards3D[i].position, { x: arcPositions[i].x, y: arcPositions[i].y, z: arcPositions[i].z, duration: 1.5, ease: 'power2.out' }, i * 0.15);
    tl.to(cards3D[i].scale, { x: 1.0, y: 1.0, z: 1.0, duration: 1.5, ease: 'power2.out' }, i * 0.15);
    tl.to(cards3D[i].material, { opacity: 0.95, duration: 1.2, ease: 'power1.out' }, i * 0.15);
    tl.to(cards3D[i].rotation, { y: arcRotations[i], duration: 1.5, ease: 'power2.out' }, i * 0.15);
  }

  // Phase 2 (2-3.5s): Hold in arc + show text + breathing float
  tl.to(titleText, { opacity: 1, duration: 1.0, ease: 'power1.out' }, 2);
  for (var i = 0; i < cards3D.length; i++) {
    tl.to(cards3D[i].position, { y: arcPositions[i].y + 0.2, duration: 0.8, ease: 'sine.inOut', yoyo: true, repeat: 1 }, 2);
  }

  // Phase 3 (3.5-5s): Settle to final positions
  for (var i = 0; i < cards3D.length; i++) {
    var bp = cards3D[i].userData.basePos;
    var br = cards3D[i].userData.baseRot;
    tl.to(cards3D[i].position, { x: bp.x, y: bp.y, z: bp.z, duration: 1.2, ease: 'power2.inOut' }, 3.5);
    tl.to(cards3D[i].rotation, { y: br, duration: 1.2, ease: 'power2.inOut' }, 3.5);
  }
}

/* ====== LAYER 1 RENDER ====== */
function renderCardScene() {
  if (currentLayer !== 1) return;
  animId = requestAnimationFrame(renderCardScene);

  var el = cardClock.getElapsedTime();

  // Float animation (only after entrance completes)
  if (entrancePlayed) {
    for (var i = 0; i < cards3D.length; i++) {
      var card = cards3D[i];
      var bp = card.userData.basePos;
      var fo = card.userData.floatOffset;
      card.position.y = bp.y + Math.sin(el * 0.8 + fo) * 0.15;
      card.position.x = bp.x + Math.sin(el * 0.5 + fo + 1) * 0.03;
    }
  }

  // Raycaster hover
  raycaster.setFromCamera(mouse2, cardCamera);
  var intersects = raycaster.intersectObjects(cardMeshes);

  if (intersects.length > 0) {
    var hit = intersects[0].object;
    hoveredCard = hit;
    canvas.style.cursor = 'pointer';

    for (var i = 0; i < cards3D.length; i++) {
      var card = cards3D[i];
      if (card === hit) {
        // Scale up, tilt toward mouse, glow
        card.scale.lerp(new THREE.Vector3(1.15, 1.15, 1.15), 0.08);
        card.rotation.y = card.userData.baseRot + (mouseRaw.x - 0.5) * 0.15;
        card.rotation.x = (mouseRaw.y - 0.5) * -0.1;
        card.material.emissiveIntensity = 0.4;
      } else {
        // Dim + push back
        card.scale.lerp(new THREE.Vector3(0.92, 0.92, 0.92), 0.06);
        card.material.emissiveIntensity = 0.02;
        card.rotation.y += (card.userData.baseRot - card.rotation.y) * 0.05;
        card.rotation.x *= 0.95;
      }
    }
  } else {
    hoveredCard = null;
    canvas.style.cursor = 'default';
    for (var i = 0; i < cards3D.length; i++) {
      var card = cards3D[i];
      card.scale.lerp(new THREE.Vector3(1, 1, 1), 0.06);
      card.material.emissiveIntensity = 0.1;
      card.rotation.y += (card.userData.baseRot - card.rotation.y) * 0.05;
      card.rotation.x *= 0.95;
    }
  }

  // Animate particles — mouse-driven flow
  if (starPoints && starBasePos) {
    var positions = starPoints.geometry.attributes.position.array;
    for (var i = 0; i < 600; i++) {
      var bx = starBasePos[i*3], by = starBasePos[i*3+1], bz = starBasePos[i*3+2];
      positions[i*3] = bx + Math.sin(el * 0.3 + i * 0.1) * 0.15 + mouseRaw.x * 0.5;
      positions[i*3+1] = by + Math.cos(el * 0.25 + i * 0.13) * 0.12 + mouseRaw.y * 0.3;
      positions[i*3+2] = bz + Math.sin(el * 0.2 + i * 0.07) * 0.1;
    }
    starPoints.geometry.attributes.position.needsUpdate = true;
  }

  renderer.render(cardScene, cardCamera);
}

/* ====== MOUSE EVENTS (LAYER 1) ====== */
window.addEventListener('mousemove', function(e) {
  mouse2.x = (e.clientX / window.innerWidth) * 2 - 1;
  mouse2.y = -(e.clientY / window.innerHeight) * 2 + 1;
  mouseRaw.x = e.clientX / window.innerWidth;
  mouseRaw.y = e.clientY / window.innerHeight;
});

window.addEventListener('click', function(e) {
  if (currentLayer !== 1 || !hoveredCard || transitioning) return;
  var idx = hoveredCard.userData.idx;
  transitionToDetail(idx);
});

/* ====== TRANSITION: CARD -> DETAIL ====== */
function transitionToDetail(cardIdx) {
  transitioning = true;
  activeTheme = CARD_DATA[cardIdx].key;
  populatePanels(activeTheme);

  var clicked = cards3D[cardIdx];

  var tl = gsap.timeline({
    onComplete: function() {
      showDetailLayer();
      transitioning = false;
    }
  });

  // Other cards fly out to sides and fade
  for (var i = 0; i < cards3D.length; i++) {
    if (i !== cardIdx) {
      var dir = i < cardIdx ? -1 : 1;
      tl.to(cards3D[i].position, { x: dir * 12, duration: 0.6, ease: 'power2.in' }, 0);
      tl.to(cards3D[i].scale, { x: 0.6, y: 0.6, z: 0.6, duration: 0.6, ease: 'power2.in' }, 0);
      tl.to(cards3D[i].material, { opacity: 0, duration: 0.4 }, 0.2);
    }
  }

  // Clicked card: move to center, scale up, flip on Y axis
  tl.to(clicked.position, { x: 0, y: 0, z: 2, duration: 0.5, ease: 'power2.out' }, 0);
  tl.to(clicked.scale, { x: 1.3, y: 1.3, z: 1.3, duration: 0.5, ease: 'power2.out' }, 0);
  tl.to(clicked.rotation, { y: Math.PI, duration: 0.7, ease: 'power2.inOut' }, 0.3);
  tl.to(clicked.material, { opacity: 0, duration: 0.3 }, 0.8);

  // Flash white on renderer
  tl.to({}, { duration: 0.1, onComplete: function() {
    renderer.setClearColor(0xcccccc, 1);
  }}, 0.7);
  tl.to({}, { duration: 0.3, onComplete: function() {
    renderer.setClearColor(0x0a0a0a, 1);
  }}, 0.9);

  // Hide title text
  tl.to(layer1.querySelector('.title-text'), { opacity: 0, duration: 0.3 }, 0);
}

function populatePanels(themeKey) {
  var panels = THEMES[themeKey].panels;
  for (var i = 0; i < 6; i++) {
    document.getElementById('pt' + i).textContent = panels[i].title;
    document.getElementById('px' + i).textContent = panels[i].text;
  }
}

/* ====== SHOW DETAIL LAYER ====== */
function showDetailLayer() {
  currentLayer = 2;
  cancelAnimationFrame(animId);

  layer1.style.display = 'none';
  layer2.style.display = 'block';
  backBtn.style.display = 'block';
  progressBar.style.display = 'block';
  dotNav.style.display = 'flex';
  sectionCounter.style.display = 'block';
  document.body.classList.add('layer2-active');

  window.scrollTo(0, 0);

  // Build dot nav
  dotNav.innerHTML = '';
  var panelData = THEMES[activeTheme].panels;
  for (var i = 0; i < 6; i++) {
    var dot = document.createElement('div');
    dot.className = 'dot' + (i === 0 ? ' active' : '');
    dot.setAttribute('data-label', panelData[i].title);
    dot.setAttribute('data-idx', i);
    dot.addEventListener('click', (function(idx) {
      return function() {
        var targetScroll = (idx / 6) * (document.documentElement.scrollHeight - window.innerHeight);
        window.scrollTo({ top: targetScroll, behavior: 'smooth' });
      };
    })(i));
    dotNav.appendChild(dot);
  }

  initDetailScene();
  renderDetailScene();
}

/* ====== LAYER 2: DETAIL SCENE ====== */
var detailScene, detailCamera, detailClock;
var cameraPath, lookAtPath;
var detailParticles;

function initDetailScene() {
  detailScene = new THREE.Scene();
  detailScene.fog = new THREE.FogExp2(0x0c0a12, 0.04);

  detailCamera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 200);

  detailScene.add(new THREE.AmbientLight(0xffffff, 0.15));
  var dl = new THREE.DirectionalLight(0x7c3aed, 0.3);
  dl.position.set(5, 10, 5);
  detailScene.add(dl);
  var dl2 = new THREE.DirectionalLight(0xf75092, 0.2);
  dl2.position.set(-5, -5, -10);
  detailScene.add(dl2);

  // Camera path
  cameraPath = new THREE.CatmullRomCurve3([
    new THREE.Vector3(0, 0, 12),
    new THREE.Vector3(3, 1, 8),
    new THREE.Vector3(-2, 2, 4),
    new THREE.Vector3(4, -1, 0),
    new THREE.Vector3(-3, 0, -4),
    new THREE.Vector3(0, 3, -8),
    new THREE.Vector3(2, -1, -12),
    new THREE.Vector3(0, 0, -16)
  ]);

  // LookAt path (offset from camera path)
  lookAtPath = new THREE.CatmullRomCurve3([
    new THREE.Vector3(1, 0.5, 8),
    new THREE.Vector3(-1, 1.5, 5),
    new THREE.Vector3(2, 1, 1),
    new THREE.Vector3(-2, 0, -3),
    new THREE.Vector3(1, 1, -7),
    new THREE.Vector3(-1, 2, -11),
    new THREE.Vector3(0, 0.5, -15),
    new THREE.Vector3(1, 0, -20)
  ]);

  // 40 wireframe objects along path
  var wireGeos = [
    new THREE.IcosahedronGeometry(0.5, 0),
    new THREE.OctahedronGeometry(0.5, 0),
    new THREE.TetrahedronGeometry(0.5, 0),
    new THREE.BoxGeometry(0.7, 0.7, 0.7)
  ];
  for (var i = 0; i < 40; i++) {
    var t = i / 40;
    var pt = cameraPath.getPointAt(t);
    var geo = wireGeos[i % wireGeos.length];
    var mat = new THREE.MeshPhongMaterial({
      color: i % 2 === 0 ? 0x7c3aed : 0xf75092,
      wireframe: true,
      transparent: true,
      opacity: 0.15
    });
    var mesh = new THREE.Mesh(geo, mat);
    mesh.position.set(
      pt.x + (Math.random() - 0.5) * 8,
      pt.y + (Math.random() - 0.5) * 6,
      pt.z + (Math.random() - 0.5) * 4
    );
    mesh.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, 0);
    mesh.userData.rotSpeed = { x: (Math.random() - 0.5) * 0.01, y: (Math.random() - 0.5) * 0.01 };
    detailScene.add(mesh);
  }

  // 60 metallic small objects
  for (var i = 0; i < 60; i++) {
    var t = i / 60;
    var pt = cameraPath.getPointAt(t);
    var geo = new THREE.SphereGeometry(0.08 + Math.random() * 0.12, 8, 8);
    var mat = new THREE.MeshPhongMaterial({
      color: 0xaaaacc,
      shininess: 100,
      transparent: true,
      opacity: 0.3
    });
    var mesh = new THREE.Mesh(geo, mat);
    mesh.position.set(
      pt.x + (Math.random() - 0.5) * 10,
      pt.y + (Math.random() - 0.5) * 8,
      pt.z + (Math.random() - 0.5) * 6
    );
    detailScene.add(mesh);
  }

  // 600 particles along path
  var pGeo = new THREE.BufferGeometry();
  var pPos = new Float32Array(600 * 3);
  for (var i = 0; i < 600; i++) {
    var t = Math.random();
    var pt = cameraPath.getPointAt(t);
    pPos[i * 3] = pt.x + (Math.random() - 0.5) * 12;
    pPos[i * 3 + 1] = pt.y + (Math.random() - 0.5) * 10;
    pPos[i * 3 + 2] = pt.z + (Math.random() - 0.5) * 8;
  }
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
  detailParticles = new THREE.Points(pGeo, new THREE.PointsMaterial({
    color: 0xffffff, size: 0.04, transparent: true, opacity: 0.3, sizeAttenuation: true
  }));
  detailScene.add(detailParticles);

  detailClock = new THREE.Clock();
  currentScene = detailScene;
  camera = detailCamera;

  // Set up ScrollTrigger
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.getAll().forEach(function(st) { st.kill(); });

  ScrollTrigger.create({
    trigger: layer2,
    start: 'top top',
    end: 'bottom bottom',
    scrub: 0.8,
    onUpdate: function(self) {
      detailProgress = self.progress;
    }
  });
}

var detailProgress = 0;

/* ====== LAYER 2 RENDER ====== */
function renderDetailScene() {
  if (currentLayer !== 2) return;
  animId = requestAnimationFrame(renderDetailScene);

  var el = detailClock.getElapsedTime();
  var prog = Math.max(0, Math.min(detailProgress, 0.999));

  // Camera on path
  var camPos = cameraPath.getPointAt(prog);
  var lookPos = lookAtPath.getPointAt(Math.min(prog + 0.05, 0.999));
  detailCamera.position.copy(camPos);
  detailCamera.lookAt(lookPos);

  // Fog and exposure driven by scroll
  detailScene.fog.density = 0.04 + prog * 0.02;
  renderer.toneMappingExposure = 1.0 + Math.sin(prog * Math.PI) * 0.3;

  // Rotate wireframe objects
  detailScene.children.forEach(function(child) {
    if (child.userData.rotSpeed) {
      child.rotation.x += child.userData.rotSpeed.x;
      child.rotation.y += child.userData.rotSpeed.y;
    }
  });

  // Particle subtle drift
  if (detailParticles) {
    detailParticles.rotation.y = el * 0.005;
  }

  // Panel visibility
  var sectionSize = 1 / 6;
  var currentIdx = Math.min(Math.floor(prog / sectionSize), 5);
  var localT = (prog - currentIdx * sectionSize) / sectionSize;

  for (var i = 0; i < 6; i++) {
    var panel = document.getElementById('panel' + i);
    if (i === currentIdx) {
      panel.classList.add('visible');
      // Fade in first 15%, hold, fade out last 15%
      var opacity, ty;
      if (localT < 0.15) {
        opacity = localT / 0.15;
        ty = 30 * (1 - localT / 0.15);
      } else if (localT > 0.85) {
        opacity = (1 - localT) / 0.15;
        ty = -30 * (1 - (1 - localT) / 0.15);
      } else {
        opacity = 1;
        ty = 0;
      }
      panel.style.opacity = Math.max(0, Math.min(1, opacity));
      panel.style.transform = 'translateY(' + ty + 'px)';
    } else {
      panel.classList.remove('visible');
      panel.style.opacity = 0;
    }
  }

  // Update UI
  secNum.textContent = ('0' + (currentIdx + 1)).slice(-2);
  progressBar.style.width = (prog * 100) + '%';

  // Update dots
  var dots = dotNav.querySelectorAll('.dot');
  dots.forEach(function(d, i) { d.classList.toggle('active', i === currentIdx); });

  renderer.render(detailScene, detailCamera);
}

/* ====== TRANSITION: DETAIL -> CARDS ====== */
function transitionToCards() {
  transitioning = true;
  currentLayer = 0; // prevent rendering
  cancelAnimationFrame(animId);

  // Kill ScrollTrigger
  ScrollTrigger.getAll().forEach(function(st) { st.kill(); });

  // Hide detail UI
  layer2.style.display = 'none';
  backBtn.style.display = 'none';
  progressBar.style.display = 'none';
  dotNav.style.display = 'none';
  sectionCounter.style.display = 'none';
  document.body.classList.remove('layer2-active');

  // Hide all panels
  for (var i = 0; i < 6; i++) {
    var panel = document.getElementById('panel' + i);
    panel.classList.remove('visible');
    panel.style.opacity = 0;
  }

  window.scrollTo(0, 0);

  // Re-show layer 1
  layer1.style.display = 'flex';
  layer1.querySelector('.title-text').style.opacity = '1';

  // Re-init card scene
  initCardScene();

  // Place cards at final positions directly (no entrance replay)
  for (var i = 0; i < cards3D.length; i++) {
    var bp = cards3D[i].userData.basePos;
    cards3D[i].position.copy(bp);
    cards3D[i].scale.set(1, 1, 1);
    cards3D[i].material.opacity = 0.95;
    cards3D[i].rotation.y = cards3D[i].userData.baseRot;
  }

  // Reset hover state
  hoveredCard = null;
  mouse2.set(-999, -999);

  currentLayer = 1;
  renderCardScene();

  // Delay clearing transitioning flag to prevent re-click
  setTimeout(function() {
    transitioning = false;
  }, 500);
}

backBtn.addEventListener('click', transitionToCards);
panelCta.addEventListener('click', transitionToCards);

/* ====== RESIZE ====== */
window.addEventListener('resize', function() {
  renderer.setSize(window.innerWidth, window.innerHeight);
  if (currentLayer === 1 && cardCamera) {
    cardCamera.aspect = window.innerWidth / window.innerHeight;
    cardCamera.updateProjectionMatrix();
  }
  if (currentLayer === 2 && detailCamera) {
    detailCamera.aspect = window.innerWidth / window.innerHeight;
    detailCamera.updateProjectionMatrix();
  }
});

/* ====== INIT ====== */
initCardScene();
renderCardScene();
playEntranceAnimation();

})();
</script>
</body>
</html>
