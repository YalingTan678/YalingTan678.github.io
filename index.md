---
layout: home
author_profile: false
---

<!-- ========== RESEARCH STRANDS VENN ========== -->
<section class="lt-section lt-fade-in" style="padding-top:0">
  <h2 class="lt-section__title">Research Strands</h2>
  <p style="font-size:0.92rem;color:#4a5568;line-height:1.7;margin-bottom:1.5rem">My work moves across four interconnected strands. Hover over each area to see how they relate:</p>

  <div style="position:relative;max-width:960px;margin:0 auto">
    <!-- SVG Venn Diagram -->
    <svg viewBox="0 0 900 680" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
      <defs>
        <filter id="shadow-green" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#047857" flood-opacity="0.25"/>
        </filter>
        <filter id="shadow-blue" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#2563eb" flood-opacity="0.25"/>
        </filter>
        <filter id="shadow-orange" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#c2410c" flood-opacity="0.25"/>
        </filter>
        <filter id="shadow-purple" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#6d28d9" flood-opacity="0.25"/>
        </filter>
        <filter id="pill-shadow" x="-15%" y="-40%" width="130%" height="200%">
          <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="blur"/>
          <feOffset dy="2" result="shifted"/>
          <feFlood flood-opacity="0.15" result="color"/>
          <feComposite in="color" in2="shifted" operator="in" result="shadow"/>
          <feMerge><feMergeNode in="shadow"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
        <!-- Gradient fills for ellipses -->
        <radialGradient id="grad-literacy" cx="35%" cy="30%" r="70%">
          <stop offset="0%" stop-color="#6ee7b7" stop-opacity="0.55"/>
          <stop offset="45%" stop-color="#34d399" stop-opacity="0.30"/>
          <stop offset="100%" stop-color="#047857" stop-opacity="0.10"/>
        </radialGradient>
        <radialGradient id="grad-idle" cx="35%" cy="30%" r="70%">
          <stop offset="0%" stop-color="#93c5fd" stop-opacity="0.55"/>
          <stop offset="45%" stop-color="#60a5fa" stop-opacity="0.30"/>
          <stop offset="100%" stop-color="#2563eb" stop-opacity="0.10"/>
        </radialGradient>
        <radialGradient id="grad-equity" cx="65%" cy="30%" r="70%">
          <stop offset="0%" stop-color="#fdba74" stop-opacity="0.55"/>
          <stop offset="45%" stop-color="#fb923c" stop-opacity="0.30"/>
          <stop offset="100%" stop-color="#c2410c" stop-opacity="0.10"/>
        </radialGradient>
        <radialGradient id="grad-tpack" cx="65%" cy="30%" r="70%">
          <stop offset="0%" stop-color="#c4b5fd" stop-opacity="0.55"/>
          <stop offset="45%" stop-color="#a78bfa" stop-opacity="0.30"/>
          <stop offset="100%" stop-color="#6d28d9" stop-opacity="0.10"/>
        </radialGradient>
        <!-- Pill gradient backgrounds -->
        <linearGradient id="pill-green" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#ffffff"/><stop offset="40%" stop-color="#ecfdf5"/><stop offset="100%" stop-color="#a7f3d0"/>
        </linearGradient>
        <linearGradient id="pill-blue" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#ffffff"/><stop offset="40%" stop-color="#eff6ff"/><stop offset="100%" stop-color="#bfdbfe"/>
        </linearGradient>
        <linearGradient id="pill-orange" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#ffffff"/><stop offset="40%" stop-color="#fff7ed"/><stop offset="100%" stop-color="#fed7aa"/>
        </linearGradient>
        <linearGradient id="pill-purple" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#ffffff"/><stop offset="40%" stop-color="#f5f3ff"/><stop offset="100%" stop-color="#ddd6fe"/>
        </linearGradient>
        <linearGradient id="pill-center" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/>
        </linearGradient>
      </defs>

      <!-- Strand ellipses with gradient fills -->
      <ellipse id="venn-literacy" cx="340" cy="240" rx="240" ry="185" fill="url(#grad-literacy)" stroke="#047857" stroke-width="2.5" stroke-opacity="0.5" filter="url(#shadow-green)" style="cursor:pointer;transition:all 0.5s ease"/>
      <ellipse id="venn-idle" cx="230" cy="410" rx="220" ry="175" fill="url(#grad-idle)" stroke="#2563eb" stroke-width="2.5" stroke-opacity="0.5" filter="url(#shadow-blue)" style="cursor:pointer;transition:all 0.5s ease"/>
      <ellipse id="venn-equity" cx="530" cy="410" rx="220" ry="175" fill="url(#grad-equity)" stroke="#c2410c" stroke-width="2.5" stroke-opacity="0.5" filter="url(#shadow-orange)" style="cursor:pointer;transition:all 0.5s ease"/>
      <ellipse id="venn-tpack" cx="650" cy="240" rx="210" ry="170" fill="url(#grad-tpack)" stroke="#6d28d9" stroke-width="2.5" stroke-opacity="0.5" filter="url(#shadow-purple)" style="cursor:pointer;transition:all 0.5s ease"/>

      <!-- ===== AI Literacy & Learning Design (top-left green) ===== -->
      <g class="strand-group" data-strand="literacy">
        <g class="strand-title" style="cursor:pointer">
          <text x="250" y="105" font-size="19" font-weight="800" fill="#047857" text-anchor="middle">AI Literacy &amp;</text>
          <text x="250" y="130" font-size="19" font-weight="800" fill="#047857" text-anchor="middle">Learning Design</text>
          <text x="250" y="150" font-size="11" fill="#047857" opacity="0.6" text-anchor="middle" font-style="italic">Design principles &amp; environments</text>
        </g>
        <g class="strand-pills">
          <a href="/publication/2025-two-years-innovation" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="185" y="170" width="180" height="26" rx="13" fill="url(#pill-green)" stroke="#047857" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="275" y="188" font-size="11.5" fill="#047857" font-weight="600" text-anchor="middle" style="cursor:pointer">GenAI Review · CAEAI '25</text>
          </a>
          <a href="/publication/ur-tutor-not-solver" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="185" y="202" width="180" height="26" rx="13" fill="url(#pill-green)" stroke="#047857" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="275" y="220" font-size="11.5" fill="#047857" font-weight="600" text-anchor="middle" style="cursor:pointer">PeteChat Design Case →</text>
          </a>
          <a href="/publication/2026-clawdbot-unboxed" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="200" y="234" width="150" height="26" rx="13" fill="url(#pill-green)" stroke="#047857" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="275" y="252" font-size="11.5" fill="#047857" font-weight="600" text-anchor="middle" style="cursor:pointer">Clawdbot · Talk '26</text>
          </a>
        </g>
      </g>

      <!-- ===== TPACK & Teacher Ed (top-right purple) ===== -->
      <g class="strand-group" data-strand="tpack">
        <g class="strand-title" style="cursor:pointer">
          <text x="720" y="115" font-size="19" font-weight="800" fill="#6d28d9" text-anchor="middle">TPACK &amp;</text>
          <text x="720" y="140" font-size="19" font-weight="800" fill="#6d28d9" text-anchor="middle">Teacher Ed</text>
          <text x="720" y="160" font-size="11" fill="#6d28d9" opacity="0.6" text-anchor="middle" font-style="italic">Technology integration &amp; diversity</text>
        </g>
        <g class="strand-pills">
          <a href="/publication/ur-tpack-xinjiang" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="640" y="180" width="160" height="26" rx="13" fill="url(#pill-purple)" stroke="#6d28d9" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="720" y="198" font-size="11.5" fill="#6d28d9" font-weight="600" text-anchor="middle" style="cursor:pointer">TPACK Xinjiang →</text>
          </a>
          <a href="/publication/2025-purdue-ai-gai" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="640" y="212" width="160" height="26" rx="13" fill="url(#pill-purple)" stroke="#6d28d9" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="720" y="230" font-size="11.5" fill="#6d28d9" font-weight="600" text-anchor="middle" style="cursor:pointer">GAI-IDLE · P-12 '25</text>
          </a>
        </g>
      </g>

      <!-- ===== IDLE & Pragmatics (bottom-left blue) ===== -->
      <g class="strand-group" data-strand="idle">
        <g class="strand-title" style="cursor:pointer">
          <text x="140" y="360" font-size="19" font-weight="800" fill="#2563eb" text-anchor="middle">IDLE &amp;</text>
          <text x="140" y="385" font-size="19" font-weight="800" fill="#2563eb" text-anchor="middle">Pragmatics</text>
          <text x="140" y="405" font-size="11" fill="#2563eb" opacity="0.6" text-anchor="middle" font-style="italic">AI chatbots &amp; self-directed learning</text>
        </g>
        <g class="strand-pills">
          <a href="/publication/2026-doubao-genai-efl" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="55" y="420" width="170" height="26" rx="13" fill="url(#pill-blue)" stroke="#2563eb" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="140" y="438" font-size="11.5" fill="#2563eb" font-weight="600" text-anchor="middle" style="cursor:pointer">Doubao EFL · PE '26</text>
          </a>
          <a href="/publication/2025-pointing-to-context" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="55" y="452" width="170" height="26" rx="13" fill="url(#pill-blue)" stroke="#2563eb" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="140" y="470" font-size="11.5" fill="#2563eb" font-weight="600" text-anchor="middle" style="cursor:pointer">Context · MJSS '25</text>
          </a>
          <a href="/publication/2024-call-context" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="70" y="484" width="140" height="26" rx="13" fill="url(#pill-blue)" stroke="#2563eb" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="140" y="502" font-size="11.5" fill="#2563eb" font-weight="600" text-anchor="middle" style="cursor:pointer">CALL Tokyo '24</text>
          </a>
        </g>
      </g>

      <!-- ===== Equity & Assessment (bottom-right orange) ===== -->
      <g class="strand-group" data-strand="equity">
        <g class="strand-title" style="cursor:pointer">
          <text x="620" y="360" font-size="19" font-weight="800" fill="#c2410c" text-anchor="middle">Equity &amp;</text>
          <text x="620" y="385" font-size="19" font-weight="800" fill="#c2410c" text-anchor="middle">Assessment</text>
          <text x="620" y="405" font-size="11" fill="#c2410c" opacity="0.6" text-anchor="middle" font-style="italic">Authenticity &amp; evaluative judgment</text>
        </g>
        <g class="strand-pills">
          <a href="/publication/2026-aera-meta-analysis" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="520" y="420" width="200" height="26" rx="13" fill="url(#pill-orange)" stroke="#c2410c" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="620" y="438" font-size="11.5" fill="#c2410c" font-weight="600" text-anchor="middle" style="cursor:pointer">Meta-analysis · AERA '26</text>
          </a>
          <a href="/publication/2025-aect-authenticity" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="530" y="452" width="180" height="26" rx="13" fill="url(#pill-orange)" stroke="#c2410c" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="620" y="470" font-size="11.5" fill="#c2410c" font-weight="600" text-anchor="middle" style="cursor:pointer">Authenticity · AECT '25</text>
          </a>
          <a href="/publication/ur-authorship-agency-ai" class="strand-pill" style="opacity:0;transform:translateY(8px)">
            <rect x="545" y="484" width="150" height="26" rx="13" fill="url(#pill-orange)" stroke="#c2410c" stroke-opacity="0.4" stroke-width="1.2" filter="url(#pill-shadow)"/>
            <text x="620" y="502" font-size="11.5" fill="#c2410c" font-weight="600" text-anchor="middle" style="cursor:pointer">Authorship &amp; AI →</text>
          </a>
        </g>
      </g>

      <!-- ===== Center overlap ===== -->
      <g class="overlap-labels">
        <rect x="340" y="335" width="130" height="40" rx="20" fill="url(#pill-center)" stroke="#64748b" stroke-opacity="0.2" stroke-width="1" filter="url(#pill-shadow)"/>
        <text x="405" y="353" font-size="13" fill="#1e1b4b" font-weight="700" text-anchor="middle" opacity="0.7">AI × Education</text>
        <text x="405" y="368" font-size="10" fill="#64748b" text-anchor="middle" opacity="0.6">Shared foundation</text>

        <!-- Overlap: Literacy ∩ IDLE -->
        <text x="250" y="310" font-size="10.5" fill="#0f766e" text-anchor="middle" opacity="0.6" font-style="italic">Design for</text>
        <text x="250" y="324" font-size="10.5" fill="#0f766e" text-anchor="middle" opacity="0.6" font-style="italic">informal learning</text>

        <!-- Overlap: Literacy ∩ Equity / center-top -->
        <text x="470" y="280" font-size="10.5" fill="#92400e" text-anchor="middle" opacity="0.6" font-style="italic">Authentic</text>
        <text x="470" y="294" font-size="10.5" fill="#92400e" text-anchor="middle" opacity="0.6" font-style="italic">AI integration</text>

        <!-- Overlap: IDLE ∩ Equity -->
        <text x="385" y="460" font-size="10.5" fill="#7c2d12" text-anchor="middle" opacity="0.6" font-style="italic">AI tools &amp;</text>
        <text x="385" y="474" font-size="10.5" fill="#7c2d12" text-anchor="middle" opacity="0.6" font-style="italic">fair assessment</text>

        <!-- Overlap: Literacy ∩ TPACK -->
        <text x="540" y="195" font-size="10.5" fill="#4c1d95" text-anchor="middle" opacity="0.6" font-style="italic">Curriculum</text>
        <text x="540" y="209" font-size="10.5" fill="#4c1d95" text-anchor="middle" opacity="0.6" font-style="italic">design</text>
      </g>

      <!-- Pulse animation for active ellipse -->
      <style>
        @keyframes venn-pulse {
          0%, 100% { stroke-width: 3; }
          50% { stroke-width: 5; }
        }
        .strand-pill { transition: opacity 0.4s ease, transform 0.4s ease; }
        .strand-title { transition: opacity 0.3s ease; }
        .strand-title:hover text { font-size: 20px; }
        .overlap-labels { transition: opacity 0.4s ease; }
      </style>
    </svg>
  </div>

  <!-- Description panel (appears on click) -->
  <div id="venn-desc-panel" style="max-width:660px;margin:1rem auto 0;padding:0;overflow:hidden;transition:all 0.5s cubic-bezier(0.4,0,0.2,1);max-height:0;opacity:0">
    <div style="padding:1.2rem 1.5rem;border-radius:14px;border:1px solid rgba(100,100,200,0.12);background:linear-gradient(135deg,#f8fafc,#f1f5f9);box-shadow:0 2px 12px rgba(0,0,0,0.06)">
      <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem">
        <div id="venn-desc-dot" style="width:10px;height:10px;border-radius:50%;background:#047857"></div>
        <strong id="venn-desc-title" style="font-size:1.05rem;color:#1e1b4b"></strong>
      </div>
      <p id="venn-desc-text" style="font-size:0.92rem;color:#475569;line-height:1.7;margin:0"></p>
    </div>
  </div>

  <!-- Click interaction -->
  <script>
  (function(){
    var active = null;
    var strandData = {
      literacy: {
        color: '#047857',
        title: 'AI Literacy & Learning Design',
        desc: 'Exploring how to design learning environments that build AI literacy through hands-on, principle-driven experiences. Projects include GenAI curriculum reviews, the PeteChat AI tutor, and the Clawdbot tangible learning kit.'
      },
      tpack: {
        color: '#6d28d9',
        title: 'TPACK & Teacher Ed',
        desc: 'Investigating how teachers integrate technology into diverse classrooms using the TPACK framework. Research spans Xinjiang teacher education contexts and P-12 generative AI readiness.'
      },
      idle: {
        color: '#2563eb',
        title: 'IDLE & Pragmatics',
        desc: 'Studying informal and self-directed language learning with AI chatbots. Research includes Doubao-powered EFL practice, pragmatic context awareness, and CALL methodologies.'
      },
      equity: {
        color: '#c2410c',
        title: 'Equity & Assessment',
        desc: 'Examining how AI reshapes assessment authenticity and academic authorship. Work includes meta-analyses of AI in education, evaluative judgment frameworks, and equity-centered design.'
      }
    };
    var ids = ['literacy','idle','equity','tpack'];
    var panel = document.getElementById('venn-desc-panel');
    var descTitle = document.getElementById('venn-desc-title');
    var descText = document.getElementById('venn-desc-text');
    var descDot = document.getElementById('venn-desc-dot');

    function resetAll() {
      ids.forEach(function(id) {
        var el = document.getElementById('venn-'+id);
        if (el) {
          el.style.opacity = '';
          el.setAttribute('stroke-width','2');
          el.setAttribute('stroke-opacity','0.4');
          el.style.animation = '';
        }
        var grp = document.querySelector('[data-strand="'+id+'"]');
        if (grp) {
          grp.querySelector('.strand-title').style.opacity = '';
          var pills = grp.querySelectorAll('.strand-pill');
          pills.forEach(function(p) {
            p.style.opacity = '0';
            p.style.transform = 'translateY(8px)';
          });
        }
      });
      var overlaps = document.querySelector('.overlap-labels');
      if (overlaps) overlaps.style.opacity = '';
      panel.style.maxHeight = '0';
      panel.style.opacity = '0';
      active = null;
    }

    function activateStrand(strand) {
      if (active === strand) { resetAll(); return; }
      active = strand;
      var data = strandData[strand];

      // Dim all ellipses and titles, then highlight selected
      ids.forEach(function(id) {
        var el = document.getElementById('venn-'+id);
        var grp = document.querySelector('[data-strand="'+id+'"]');
        if (id === strand) {
          el.style.opacity = '1';
          el.setAttribute('stroke-width','3');
          el.setAttribute('stroke-opacity','0.8');
          el.style.animation = 'venn-pulse 2s ease-in-out infinite';
          if (grp) {
            grp.querySelector('.strand-title').style.opacity = '1';
            var pills = grp.querySelectorAll('.strand-pill');
            pills.forEach(function(p, i) {
              setTimeout(function() {
                p.style.opacity = '1';
                p.style.transform = 'translateY(0)';
              }, 100 + i * 120);
            });
          }
        } else {
          el.style.opacity = '0.35';
          el.setAttribute('stroke-width','1.5');
          el.setAttribute('stroke-opacity','0.15');
          el.style.animation = '';
          if (grp) {
            grp.querySelector('.strand-title').style.opacity = '0.3';
            var pills = grp.querySelectorAll('.strand-pill');
            pills.forEach(function(p) {
              p.style.opacity = '0';
              p.style.transform = 'translateY(8px)';
            });
          }
        }
      });

      // Dim overlaps
      var overlaps = document.querySelector('.overlap-labels');
      if (overlaps) overlaps.style.opacity = '0.2';

      // Show description panel
      descTitle.textContent = data.title;
      descText.textContent = data.desc;
      descDot.style.background = data.color;
      descTitle.style.color = data.color;
      panel.style.maxHeight = '200px';
      panel.style.opacity = '1';
    }

    // Attach click to titles and ellipses
    ids.forEach(function(id) {
      var ellipse = document.getElementById('venn-'+id);
      var grp = document.querySelector('[data-strand="'+id+'"]');
      if (ellipse) ellipse.addEventListener('click', function(e) { e.stopPropagation(); activateStrand(id); });
      if (grp) {
        var title = grp.querySelector('.strand-title');
        if (title) title.addEventListener('click', function(e) { e.stopPropagation(); activateStrand(id); });
      }
    });

    // Click outside to reset
    document.addEventListener('click', function(e) {
      if (active && !e.target.closest('.strand-group') && !e.target.closest('[id^="venn-"]') && !e.target.closest('#venn-desc-panel')) {
        resetAll();
      }
    });
  })();
  </script>
</section>

<!-- ========== METHODOLOGY (interactive pipeline) ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Methodology</h2>
  <p style="font-size:0.88rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">I combine large-scale evidence synthesis with in-depth qualitative inquiry and iterative design. Each method feeds the next: reviews surface gaps, mixed methods explore them, statistics test claims, and design-based research translates findings into tools educators can actually use.</p>
  <div style="display:flex;align-items:stretch;gap:0;background:#0f172a;border-radius:16px;overflow:hidden;position:relative">
    <!-- Connecting line -->
    <div style="position:absolute;top:50%;left:0;right:0;height:2px;background:linear-gradient(90deg,#3b82f6,#8b5cf6,#22c55e,#f59e0b);z-index:1;opacity:0.3"></div>
    <!-- Card 1 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;border-right:1px solid rgba(255,255,255,0.06);cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(59,130,246,0.15)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#3b82f6,#60a5fa);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(59,130,246,0.35);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(5deg)';this.style.boxShadow='0 8px 25px rgba(59,130,246,0.5)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(59,130,246,0.35)'">&#128269;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#e2e8f0;margin-bottom:0.3rem">Systematic Reviews</div>
      <div style="font-size:0.68rem;color:#94a3b8;line-height:1.5">PRISMA · Scoping<br>Meta-analyses</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#60a5fa;font-weight:600;letter-spacing:0.05em">144 ARTICLES SCREENED</div>
    </div>
    <!-- Arrow -->
    <div style="display:flex;align-items:center;color:rgba(255,255,255,0.2);font-size:1.2rem;z-index:2">&#10132;</div>
    <!-- Card 2 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;border-right:1px solid rgba(255,255,255,0.06);cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(139,92,246,0.15)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#8b5cf6,#a78bfa);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(139,92,246,0.35);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(-5deg)';this.style.boxShadow='0 8px 25px rgba(139,92,246,0.5)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(139,92,246,0.35)'">&#128300;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#e2e8f0;margin-bottom:0.3rem">Mixed Methods</div>
      <div style="font-size:0.68rem;color:#94a3b8;line-height:1.5">Quan + Qual<br>Surveys · Interviews</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#a78bfa;font-weight:600;letter-spacing:0.05em">CONVERGENT DESIGN</div>
    </div>
    <!-- Arrow -->
    <div style="display:flex;align-items:center;color:rgba(255,255,255,0.2);font-size:1.2rem;z-index:2">&#10132;</div>
    <!-- Card 3 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;border-right:1px solid rgba(255,255,255,0.06);cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(34,197,94,0.15)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#22c55e,#4ade80);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(34,197,94,0.35);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(5deg)';this.style.boxShadow='0 8px 25px rgba(34,197,94,0.5)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(34,197,94,0.35)'">&#128200;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#e2e8f0;margin-bottom:0.3rem">Statistical Analysis</div>
      <div style="font-size:0.68rem;color:#94a3b8;line-height:1.5">SPSS · Prism<br>ANOVA · Coh-Metrix</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#4ade80;font-weight:600;letter-spacing:0.05em">108 INDICES TESTED</div>
    </div>
    <!-- Arrow -->
    <div style="display:flex;align-items:center;color:rgba(255,255,255,0.2);font-size:1.2rem;z-index:2">&#10132;</div>
    <!-- Card 4 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(245,158,11,0.15)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#f59e0b,#fbbf24);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(245,158,11,0.35);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(-5deg)';this.style.boxShadow='0 8px 25px rgba(245,158,11,0.5)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(245,158,11,0.35)'">&#127919;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#e2e8f0;margin-bottom:0.3rem">Design-Based Research</div>
      <div style="font-size:0.68rem;color:#94a3b8;line-height:1.5">Iterative cycles<br>In-vivo prototyping</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#fbbf24;font-weight:600;letter-spacing:0.05em">4 DBR PHASES</div>
    </div>
  </div>
</section>

<!-- ========== INTERACTIVE TIMELINE ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Journey</h2>
  <p style="font-size:0.88rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">From translation studies to AI-mediated learning design, every step has brought me closer to one goal: becoming an instructional designer who harnesses AI to create equitable, human-centered learning experiences at scale.</p>
  <!-- Filter buttons -->
  <div style="display:flex;gap:0.4rem;margin-bottom:1.2rem;flex-wrap:wrap">
    <button onclick="filterTL('all')" style="border:none;padding:0.3rem 0.7rem;border-radius:6px;font-size:0.72rem;font-weight:600;cursor:pointer;background:#1a1a2e;color:#fff;transition:all 0.2s">All</button>
    <button onclick="filterTL('pub')" style="border:none;padding:0.3rem 0.7rem;border-radius:6px;font-size:0.72rem;font-weight:600;cursor:pointer;background:rgba(59,130,246,0.1);color:#2563eb;transition:all 0.2s">Publications</button>
    <button onclick="filterTL('talk')" style="border:none;padding:0.3rem 0.7rem;border-radius:6px;font-size:0.72rem;font-weight:600;cursor:pointer;background:rgba(245,158,11,0.1);color:#d97706;transition:all 0.2s">Talks</button>
    <button onclick="filterTL('edu')" style="border:none;padding:0.3rem 0.7rem;border-radius:6px;font-size:0.72rem;font-weight:600;cursor:pointer;background:rgba(139,92,246,0.1);color:#7c3aed;transition:all 0.2s">Education</button>
    <button onclick="filterTL('work')" style="border:none;padding:0.3rem 0.7rem;border-radius:6px;font-size:0.72rem;font-weight:600;cursor:pointer;background:rgba(20,184,166,0.1);color:#0d9488;transition:all 0.2s">Experience</button>
    <button onclick="filterTL('award')" style="border:none;padding:0.3rem 0.7rem;border-radius:6px;font-size:0.72rem;font-weight:600;cursor:pointer;background:rgba(236,72,153,0.1);color:#db2777;transition:all 0.2s">Awards</button>
  </div>
  <!-- Scrollable timeline -->
  <div style="overflow-x:auto;padding-bottom:1rem;-webkit-overflow-scrolling:touch">
    <div id="timeline-track" style="display:flex;align-items:center;min-width:2200px;position:relative;padding:120px 40px 130px">
      <!-- The line -->
      <div style="position:absolute;left:40px;right:40px;top:50%;height:2px;background:linear-gradient(90deg,#e2e8f0,#94a3b8,#e2e8f0);z-index:1"></div>

      <!-- 2019 -->
      <div class="tl-node" data-cat="award" style="position:relative;flex:0 0 120px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <div style="background:#fdf2f8;border:1px solid #fbcfe8;border-radius:10px;padding:0.5rem 0.7rem;max-width:140px;cursor:default;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 20px rgba(236,72,153,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#db2777;font-weight:700;margin-bottom:0.15rem">&#127942; AWARD</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">National Undergraduate Award</div>
            <div style="font-size:0.62rem;color:#94a3b8">SWUST · $750</div>
          </div>
        </div>
        <div style="width:14px;height:14px;border-radius:50%;background:#ec4899;border:3px solid #fff;box-shadow:0 0 0 2px #ec4899;margin:0 auto;position:relative;z-index:3"></div>
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-top:8px">2019</div>
      </div>

      <!-- 2021 -->
      <div class="tl-node" data-cat="work" style="position:relative;flex:0 0 160px;z-index:2;text-align:center">
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-bottom:8px">2021</div>
        <div style="width:14px;height:14px;border-radius:50%;background:#14b8a6;border:3px solid #fff;box-shadow:0 0 0 2px #14b8a6;margin:0 auto;position:relative;z-index:3"></div>
        <div style="position:absolute;top:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/teaching/" style="text-decoration:none;display:block;background:#f0fdfa;border:1px solid #99f6e4;border-radius:10px;padding:0.5rem 0.7rem;max-width:150px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(4px)';this.style.boxShadow='0 8px 20px rgba(20,184,166,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#0d9488;font-weight:700;margin-bottom:0.15rem">&#128188; TEACHING</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">TAL Education</div>
            <div style="font-size:0.62rem;color:#94a3b8">Lecturer · 500+ students</div>
          </a>
        </div>
      </div>

      <!-- 2022 -->
      <div class="tl-node" data-cat="edu" style="position:relative;flex:0 0 130px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <div style="background:#f5f3ff;border:1px solid #ddd6fe;border-radius:10px;padding:0.5rem 0.7rem;max-width:140px;cursor:default;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 20px rgba(139,92,246,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#7c3aed;font-weight:700;margin-bottom:0.15rem">&#127891; DEGREE</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">B.A. Translation</div>
            <div style="font-size:0.62rem;color:#94a3b8">SWUST, China</div>
          </div>
        </div>
        <div style="width:14px;height:14px;border-radius:50%;background:#8b5cf6;border:3px solid #fff;box-shadow:0 0 0 2px #8b5cf6;margin:0 auto;position:relative;z-index:3"></div>
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-top:8px">2022</div>
      </div>

      <!-- 2023 -->
      <div class="tl-node" data-cat="pub" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-bottom:8px">2023</div>
        <div style="width:14px;height:14px;border-radius:50%;background:#3b82f6;border:3px solid #fff;box-shadow:0 0 0 2px #3b82f6;margin:0 auto;position:relative;z-index:3"></div>
        <div style="position:absolute;top:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/publication/2023-clil-translation" style="text-decoration:none;display:block;background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:0.5rem 0.7rem;max-width:150px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(4px)';this.style.boxShadow='0 8px 20px rgba(59,130,246,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#2563eb;font-weight:700;margin-bottom:0.15rem">&#128220; PUB</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">CLIL · Ed. Advances</div>
            <div style="font-size:0.62rem;color:#94a3b8">Gao &amp; Tan</div>
          </a>
        </div>
      </div>

      <!-- 2024 M.A. -->
      <div class="tl-node" data-cat="edu" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <div style="background:#f5f3ff;border:1px solid #ddd6fe;border-radius:10px;padding:0.5rem 0.7rem;max-width:160px;cursor:default;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 20px rgba(139,92,246,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#7c3aed;font-weight:700;margin-bottom:0.15rem">&#127891; DEGREES</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">M.A. Interpreting &amp; Philology</div>
            <div style="font-size:0.62rem;color:#94a3b8">NEU + Silesia (dual)</div>
          </div>
        </div>
        <div style="width:14px;height:14px;border-radius:50%;background:#8b5cf6;border:3px solid #fff;box-shadow:0 0 0 2px #8b5cf6;margin:0 auto;position:relative;z-index:3"></div>
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-top:8px">2024</div>
      </div>

      <!-- 2024 Talks -->
      <div class="tl-node" data-cat="talk" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-bottom:8px"></div>
        <div style="width:14px;height:14px;border-radius:50%;background:#f59e0b;border:3px solid #fff;box-shadow:0 0 0 2px #f59e0b;margin:0 auto;position:relative;z-index:3"></div>
        <div style="position:absolute;top:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/publication/2024-call-context" style="text-decoration:none;display:block;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:0.5rem 0.7rem;max-width:150px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(4px)';this.style.boxShadow='0 8px 20px rgba(245,158,11,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#d97706;font-weight:700;margin-bottom:0.15rem">&#127908; TALKS</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">CALL Tokyo · SCT · Pisa</div>
            <div style="font-size:0.62rem;color:#94a3b8">3 conferences</div>
          </a>
        </div>
      </div>

      <!-- 2024 Award -->
      <div class="tl-node" data-cat="award" style="position:relative;flex:0 0 120px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <div style="background:#fdf2f8;border:1px solid #fbcfe8;border-radius:10px;padding:0.5rem 0.7rem;max-width:140px;cursor:default;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 20px rgba(236,72,153,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#db2777;font-weight:700;margin-bottom:0.15rem">&#127942; AWARDS</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">Fellowship + Erasmus+</div>
            <div style="font-size:0.62rem;color:#94a3b8">$2K + $5K</div>
          </div>
        </div>
        <div style="width:14px;height:14px;border-radius:50%;background:#ec4899;border:3px solid #fff;box-shadow:0 0 0 2px #ec4899;margin:0 auto;position:relative;z-index:3"></div>
      </div>

      <!-- 2025 PhD -->
      <div class="tl-node" data-cat="edu" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <div style="background:linear-gradient(135deg,#f5f3ff,#ede9fe);border:2px solid #a78bfa;border-radius:12px;padding:0.6rem 0.8rem;max-width:160px;cursor:default;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px) scale(1.03)';this.style.boxShadow='0 12px 28px rgba(139,92,246,0.2)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#7c3aed;font-weight:700;margin-bottom:0.15rem">&#127891; STARTED</div>
            <div style="font-size:0.82rem;font-weight:700;color:#5b21b6;line-height:1.35">Ph.D. at Purdue</div>
            <div style="font-size:0.62rem;color:#7c3aed">Learning Design &amp; Tech</div>
          </div>
        </div>
        <div style="width:18px;height:18px;border-radius:50%;background:#8b5cf6;border:3px solid #fff;box-shadow:0 0 0 2px #8b5cf6,0 0 12px rgba(139,92,246,0.4);margin:0 auto;position:relative;z-index:3"></div>
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-top:8px">2025</div>
      </div>

      <!-- 2025 Pubs -->
      <div class="tl-node" data-cat="pub" style="position:relative;flex:0 0 160px;z-index:2;text-align:center">
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-bottom:8px"></div>
        <div style="width:14px;height:14px;border-radius:50%;background:#3b82f6;border:3px solid #fff;box-shadow:0 0 0 2px #3b82f6;margin:0 auto;position:relative;z-index:3"></div>
        <div style="position:absolute;top:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/publication/2025-two-years-innovation" style="text-decoration:none;display:block;background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:0.5rem 0.7rem;max-width:170px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(4px)';this.style.boxShadow='0 8px 20px rgba(59,130,246,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#2563eb;font-weight:700;margin-bottom:0.15rem">&#128220; PUBS</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">CAEAI (Q1) + MJSS</div>
            <div style="font-size:0.62rem;color:#22c55e;font-weight:600">IF ≈ 10.5</div>
          </a>
        </div>
      </div>

      <!-- 2025 Talks -->
      <div class="tl-node" data-cat="talk" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/publication/2025-aect-authenticity" style="text-decoration:none;display:block;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:0.5rem 0.7rem;max-width:150px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 20px rgba(245,158,11,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#d97706;font-weight:700;margin-bottom:0.15rem">&#127908; TALKS</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">AECT + AI P-12</div>
            <div style="font-size:0.62rem;color:#94a3b8">Las Vegas + Purdue</div>
          </a>
        </div>
        <div style="width:14px;height:14px;border-radius:50%;background:#f59e0b;border:3px solid #fff;box-shadow:0 0 0 2px #f59e0b;margin:0 auto;position:relative;z-index:3"></div>
      </div>

      <!-- 2025 Service -->
      <div class="tl-node" data-cat="work" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-bottom:8px"></div>
        <div style="width:14px;height:14px;border-radius:50%;background:#14b8a6;border:3px solid #fff;box-shadow:0 0 0 2px #14b8a6;margin:0 auto;position:relative;z-index:3"></div>
        <div style="position:absolute;top:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/service/" style="text-decoration:none;display:block;background:#f0fdfa;border:1px solid #99f6e4;border-radius:10px;padding:0.5rem 0.7rem;max-width:160px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(4px)';this.style.boxShadow='0 8px 20px rgba(20,184,166,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#0d9488;font-weight:700;margin-bottom:0.15rem">&#127793; SERVICE</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">PALDT + GESC + RA</div>
            <div style="font-size:0.62rem;color:#94a3b8">Purdue University</div>
          </a>
        </div>
      </div>

      <!-- 2026 Pub -->
      <div class="tl-node" data-cat="pub" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/publication/2026-doubao-genai-efl" style="text-decoration:none;display:block;background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:0.5rem 0.7rem;max-width:160px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 20px rgba(59,130,246,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#2563eb;font-weight:700;margin-bottom:0.15rem">&#128220; PUB</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">Doubao · PE (Q2)</div>
            <div style="font-size:0.62rem;color:#94a3b8">Wang &amp; Tan</div>
          </a>
        </div>
        <div style="width:14px;height:14px;border-radius:50%;background:#3b82f6;border:3px solid #fff;box-shadow:0 0 0 2px #3b82f6;margin:0 auto;position:relative;z-index:3"></div>
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-top:8px">2026</div>
      </div>

      <!-- 2026 Clawdbot -->
      <div class="tl-node" data-cat="talk" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="font-size:0.7rem;font-weight:700;color:#1a1a2e;margin-bottom:8px"></div>
        <div style="width:14px;height:14px;border-radius:50%;background:#f59e0b;border:3px solid #fff;box-shadow:0 0 0 2px #f59e0b;margin:0 auto;position:relative;z-index:3"></div>
        <div style="position:absolute;top:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/publication/2026-clawdbot-unboxed" style="text-decoration:none;display:block;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:0.5rem 0.7rem;max-width:150px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(4px)';this.style.boxShadow='0 8px 20px rgba(245,158,11,0.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#d97706;font-weight:700;margin-bottom:0.15rem">&#127908; TALK</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">Clawdbot Unboxed</div>
            <div style="font-size:0.62rem;color:#94a3b8">AI Lunch &amp; Learn</div>
          </a>
        </div>
      </div>

      <!-- 2026 AERA upcoming -->
      <div class="tl-node" data-cat="talk" style="position:relative;flex:0 0 140px;z-index:2;text-align:center">
        <div style="position:absolute;bottom:calc(50% + 12px);left:50%;transform:translateX(-50%);width:max-content">
          <a href="/publication/2026-aera-meta-analysis" style="text-decoration:none;display:block;background:linear-gradient(135deg,#fffbeb,#fef3c7);border:2px dashed #fbbf24;border-radius:10px;padding:0.5rem 0.7rem;max-width:150px;transition:transform 0.3s,box-shadow 0.3s" onmouseover="this.style.transform='translateY(-4px) scale(1.03)';this.style.boxShadow='0 8px 20px rgba(245,158,11,0.2)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
            <div style="font-size:0.62rem;color:#d97706;font-weight:700;margin-bottom:0.15rem">&#128640; UPCOMING</div>
            <div style="font-size:0.72rem;font-weight:600;color:#1a1a2e;line-height:1.35">AERA 2026</div>
            <div style="font-size:0.62rem;color:#94a3b8">Los Angeles, CA</div>
          </a>
        </div>
        <div style="width:18px;height:18px;border-radius:50%;background:#fbbf24;border:3px solid #fff;box-shadow:0 0 0 2px #fbbf24,0 0 12px rgba(251,191,36,0.4);margin:0 auto;position:relative;z-index:3;animation:glow-pulse 3s infinite"></div>
      </div>

    </div>
  </div>
  <!-- Scroll hint -->
  <div style="text-align:center;color:#94a3b8;font-size:0.72rem;margin-top:0.3rem">&#8592; scroll to explore &#8594;</div>
</section>

<script>
function filterTL(cat) {
  var nodes = document.querySelectorAll('.tl-node');
  nodes.forEach(function(n) {
    if (cat === 'all' || n.dataset.cat === cat) {
      n.style.opacity = '1';
      n.style.transform = 'scale(1)';
    } else {
      n.style.opacity = '0.15';
      n.style.transform = 'scale(0.9)';
    }
  });
}
</script>

<!-- ========== NEWS & ACTIVITY ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">News &amp; Activity</h2>
  <div class="lt-news__filters">
    <button class="lt-news__filter active" data-cat="all">All</button>
    <button class="lt-news__filter" data-cat="paper">Papers</button>
    <button class="lt-news__filter" data-cat="talk">Talks</button>
    <button class="lt-news__filter" data-cat="award">Awards</button>
    <button class="lt-news__filter" data-cat="service">Service</button>
  </div>
  <ul class="lt-news__list">
    <li class="lt-news__item" data-cat="talk">
      <div class="lt-news__badge lt-news__badge--talk">&#127908;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">Apr 2026 (upcoming)</div>
        <div class="lt-news__text">Presenting at <strong>AERA</strong>, Los Angeles — Meta-analysis on technology &amp; low-income students.</div>
      </div>
    </li>
    <li class="lt-news__item" data-cat="paper">
      <div class="lt-news__badge lt-news__badge--paper">&#128220;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">2026</div>
        <div class="lt-news__text">Wang &amp; <strong>Tan</strong> published in <em>Psicologia Educativa</em> (Q2) — GenAI scaffolds in EFL writing.</div>
      </div>
    </li>
    <li class="lt-news__item" data-cat="talk">
      <div class="lt-news__badge lt-news__badge--talk">&#127908;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">Feb 2026</div>
        <div class="lt-news__text"><em>Clawdbot Unboxed</em> at <strong>AI Lunch &amp; Learn</strong>, Purdue College of Education.</div>
      </div>
    </li>
    <li class="lt-news__item" data-cat="paper">
      <div class="lt-news__badge lt-news__badge--paper">&#128220;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">2025</div>
        <div class="lt-news__text">Li, <strong>Tan</strong> et al. in <em>Computers &amp; Education: AI</em> (Q1, IF&asymp;10.5) — GenAI systematic review.</div>
      </div>
    </li>
    <li class="lt-news__item" data-cat="service">
      <div class="lt-news__badge lt-news__badge--service">&#127793;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">Sep 2025</div>
        <div class="lt-news__text">Joined <strong>PALDT</strong> (Marketing) and <strong>GESC</strong> (Committee Member) at Purdue.</div>
      </div>
    </li>
    <li class="lt-news__item" data-cat="award">
      <div class="lt-news__badge lt-news__badge--award">&#127942;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">2024</div>
        <div class="lt-news__text"><strong>Erasmus+ Fund</strong> ($5,000) — University of Silesia, Poland.</div>
      </div>
    </li>
  </ul>
</section>

<!-- ========== EXPERIENCE ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Professional Experience</h2>
  <div class="lt-exp__item">
    <div class="lt-exp__header">
      <div>
        <div class="lt-exp__org">Purdue University</div>
        <div class="lt-exp__role">Research Assistant, Library &amp; School of Information Studies</div>
      </div>
      <div class="lt-exp__date-loc"><span>2025 &ndash; Present</span></div>
    </div>
    <ul class="lt-exp__bullets">
      <li>Three research projects: scoping review (20,000+ articles), AI-assisted learning, audio/video in teaching.</li>
    </ul>
  </div>
  <div class="lt-exp__item">
    <div class="lt-exp__header">
      <div>
        <div class="lt-exp__org">Honeybee Technology Co., Ltd</div>
        <div class="lt-exp__role">Career Planning Specialist</div>
      </div>
      <div class="lt-exp__date-loc"><span>Jan &ndash; Jul 2025</span></div>
    </div>
    <ul class="lt-exp__bullets">
      <li>300+ students assessed; 100+ CVs revised; 100% placement success rate.</li>
    </ul>
  </div>
</section>
