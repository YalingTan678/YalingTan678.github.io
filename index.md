---
layout: home
author_profile: false
---

<!-- ========== RESEARCH CONSTELLATION MAP ========== -->
<section class="lt-section lt-fade-in" style="padding-top:0">
  <h2 class="lt-section__title">Research Strands</h2>
  <div style="background:#0f172a;border-radius:20px;padding:2.5rem 2rem;position:relative;overflow:hidden;min-height:480px">
    <!-- Animated background stars -->
    <div style="position:absolute;inset:0;overflow:hidden;pointer-events:none">
      <div style="position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;top:12%;left:8%;animation:twinkle 3s infinite"></div>
      <div style="position:absolute;width:1px;height:1px;background:#fff;border-radius:50%;top:25%;left:92%;animation:twinkle 4s infinite 1s"></div>
      <div style="position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;top:70%;left:15%;animation:twinkle 5s infinite 0.5s"></div>
      <div style="position:absolute;width:1px;height:1px;background:#fff;border-radius:50%;top:85%;left:75%;animation:twinkle 3.5s infinite 2s"></div>
      <div style="position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;top:45%;left:50%;animation:twinkle 4s infinite 1.5s"></div>
      <div style="position:absolute;width:1px;height:1px;background:#fff;border-radius:50%;top:60%;left:30%;animation:twinkle 3s infinite 0.8s"></div>
      <div style="position:absolute;width:1px;height:1px;background:#fff;border-radius:50%;top:15%;left:65%;animation:twinkle 5s infinite 2.5s"></div>
      <div style="position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;top:90%;left:45%;animation:twinkle 4s infinite 0.3s"></div>
    </div>
    <style>@keyframes twinkle{0%,100%{opacity:0.3}50%{opacity:1}}@keyframes glow-pulse{0%,100%{box-shadow:0 0 15px currentColor,0 0 30px currentColor}50%{box-shadow:0 0 25px currentColor,0 0 50px currentColor}}</style>
    <!-- Center node: Dissertation -->
    <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:20;text-align:center">
      <div style="width:100px;height:100px;border-radius:50%;background:radial-gradient(circle,#1e293b,#0f172a);border:2px solid rgba(255,255,255,0.3);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#e2e8f0;animation:glow-pulse 4s infinite;box-shadow:0 0 20px rgba(148,163,184,0.3)">
        <div style="font-size:0.55rem;text-transform:uppercase;letter-spacing:0.15em;color:#94a3b8;margin-bottom:0.15rem">Dissertation</div>
        <div style="font-size:0.8rem;font-weight:700">AI &amp;<br>Learning</div>
      </div>
    </div>
    <!-- ===== IDLE CLUSTER (top-left, blue) ===== -->
    <div style="position:absolute;left:12%;top:8%;z-index:10">
      <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:1rem">
        <div style="width:14px;height:14px;border-radius:50%;background:#3b82f6;box-shadow:0 0 12px #3b82f6,0 0 24px rgba(59,130,246,0.4);flex-shrink:0"></div>
        <span style="color:#93c5fd;font-size:0.95rem;font-weight:700;letter-spacing:0.02em">IDLE &amp; Pragmatics</span>
      </div>
      <div style="display:flex;flex-direction:column;gap:0.45rem;padding-left:1.8rem">
        <a href="/publication/2026-doubao-genai-efl" style="color:#bfdbfe;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.3);border-radius:8px;transition:all 0.25s;display:inline-block;width:fit-content" onmouseover="this.style.background='rgba(59,130,246,0.3)';this.style.boxShadow='0 0 15px rgba(59,130,246,0.3)';this.style.transform='translateX(4px)'" onmouseout="this.style.background='rgba(59,130,246,0.15)';this.style.boxShadow='';this.style.transform=''">Doubao EFL · PE '26</a>
        <a href="/publication/2025-pointing-to-context" style="color:#bfdbfe;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.3);border-radius:8px;transition:all 0.25s;display:inline-block;width:fit-content" onmouseover="this.style.background='rgba(59,130,246,0.3)';this.style.boxShadow='0 0 15px rgba(59,130,246,0.3)';this.style.transform='translateX(4px)'" onmouseout="this.style.background='rgba(59,130,246,0.15)';this.style.boxShadow='';this.style.transform=''">Context · MJSS '25</a>
        <a href="/publication/2024-call-context" style="color:#bfdbfe;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.3);border-radius:8px;transition:all 0.25s;display:inline-block;width:fit-content" onmouseover="this.style.background='rgba(59,130,246,0.3)';this.style.boxShadow='0 0 15px rgba(59,130,246,0.3)';this.style.transform='translateX(4px)'" onmouseout="this.style.background='rgba(59,130,246,0.15)';this.style.boxShadow='';this.style.transform=''">CALL Tokyo '24</a>
      </div>
    </div>
    <!-- SVG connecting lines -->
    <svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:5" viewBox="0 0 680 480">
      <line x1="160" y1="105" x2="310" y2="230" stroke="rgba(59,130,246,0.2)" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="560" y1="105" x2="370" y2="230" stroke="rgba(245,158,11,0.2)" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="340" y1="380" x2="340" y2="270" stroke="rgba(34,197,94,0.2)" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="200" y1="340" x2="310" y2="250" stroke="rgba(139,92,246,0.15)" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="500" y1="340" x2="370" y2="250" stroke="rgba(236,72,153,0.15)" stroke-width="1" stroke-dasharray="4,4"/>
    </svg>
    <!-- ===== EQUITY CLUSTER (top-right, amber) ===== -->
    <div style="position:absolute;right:8%;top:8%;z-index:10;text-align:right">
      <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:1rem;justify-content:flex-end">
        <span style="color:#fcd34d;font-size:0.95rem;font-weight:700;letter-spacing:0.02em">Authenticity &amp; Equity</span>
        <div style="width:14px;height:14px;border-radius:50%;background:#f59e0b;box-shadow:0 0 12px #f59e0b,0 0 24px rgba(245,158,11,0.4);flex-shrink:0"></div>
      </div>
      <div style="display:flex;flex-direction:column;gap:0.45rem;align-items:flex-end;padding-right:1.8rem">
        <a href="/publication/2026-aera-meta-analysis" style="color:#fde68a;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.3);border-radius:8px;transition:all 0.25s;display:inline-block" onmouseover="this.style.background='rgba(245,158,11,0.3)';this.style.boxShadow='0 0 15px rgba(245,158,11,0.3)';this.style.transform='translateX(-4px)'" onmouseout="this.style.background='rgba(245,158,11,0.15)';this.style.boxShadow='';this.style.transform=''">Meta-analysis · AERA '26</a>
        <a href="/publication/2025-aect-authenticity" style="color:#fde68a;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.3);border-radius:8px;transition:all 0.25s;display:inline-block" onmouseover="this.style.background='rgba(245,158,11,0.3)';this.style.boxShadow='0 0 15px rgba(245,158,11,0.3)';this.style.transform='translateX(-4px)'" onmouseout="this.style.background='rgba(245,158,11,0.15)';this.style.boxShadow='';this.style.transform=''">Authenticity · AECT '25</a>
        <a href="/publication/ur-authorship-agency-ai" style="color:#fde68a;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.3);border-radius:8px;transition:all 0.25s;display:inline-block" onmouseover="this.style.background='rgba(245,158,11,0.3)';this.style.boxShadow='0 0 15px rgba(245,158,11,0.3)';this.style.transform='translateX(-4px)'" onmouseout="this.style.background='rgba(245,158,11,0.15)';this.style.boxShadow='';this.style.transform=''">Authorship &amp; AI &#8594;</a>
      </div>
    </div>
    <!-- ===== AI/DESIGN CLUSTER (bottom-center, green) ===== -->
    <div style="position:absolute;left:50%;transform:translateX(-50%);bottom:12%;z-index:10;text-align:center">
      <div style="display:flex;flex-direction:column;gap:0.45rem;align-items:center;margin-bottom:0.8rem">
        <a href="/publication/ur-tutor-not-solver" style="color:#bbf7d0;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);border-radius:8px;transition:all 0.25s;display:inline-block" onmouseover="this.style.background='rgba(34,197,94,0.3)';this.style.boxShadow='0 0 15px rgba(34,197,94,0.3)';this.style.transform='translateY(-3px)'" onmouseout="this.style.background='rgba(34,197,94,0.15)';this.style.boxShadow='';this.style.transform=''">PeteChat Design Case &#8594;</a>
        <a href="/publication/2025-two-years-innovation" style="color:#bbf7d0;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);border-radius:8px;transition:all 0.25s;display:inline-block" onmouseover="this.style.background='rgba(34,197,94,0.3)';this.style.boxShadow='0 0 15px rgba(34,197,94,0.3)';this.style.transform='translateY(-3px)'" onmouseout="this.style.background='rgba(34,197,94,0.15)';this.style.boxShadow='';this.style.transform=''">2yr GenAI Review · CAEAI '25</a>
        <a href="/publication/2026-clawdbot-unboxed" style="color:#bbf7d0;font-size:0.75rem;text-decoration:none;padding:0.3rem 0.7rem;background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);border-radius:8px;transition:all 0.25s;display:inline-block" onmouseover="this.style.background='rgba(34,197,94,0.3)';this.style.boxShadow='0 0 15px rgba(34,197,94,0.3)';this.style.transform='translateY(-3px)'" onmouseout="this.style.background='rgba(34,197,94,0.15)';this.style.boxShadow='';this.style.transform=''">Clawdbot · Talk '26</a>
      </div>
      <div style="display:flex;align-items:center;gap:0.6rem;justify-content:center">
        <div style="width:14px;height:14px;border-radius:50%;background:#22c55e;box-shadow:0 0 12px #22c55e,0 0 24px rgba(34,197,94,0.4);flex-shrink:0"></div>
        <span style="color:#86efac;font-size:0.95rem;font-weight:700;letter-spacing:0.02em">AI Literacy &amp; Design</span>
      </div>
    </div>
    <!-- Cross-area nodes -->
    <a href="/publication/2025-purdue-ai-gai" style="position:absolute;left:18%;bottom:28%;z-index:10;color:#c4b5fd;font-size:0.7rem;text-decoration:none;padding:0.25rem 0.6rem;background:rgba(139,92,246,0.15);border:1px solid rgba(139,92,246,0.3);border-radius:8px;transition:all 0.25s" onmouseover="this.style.background='rgba(139,92,246,0.3)';this.style.boxShadow='0 0 15px rgba(139,92,246,0.3)'" onmouseout="this.style.background='rgba(139,92,246,0.15)';this.style.boxShadow=''">GAI-IDLE · P-12 '25</a>
    <a href="/publication/ur-tpack-xinjiang" style="position:absolute;right:16%;bottom:28%;z-index:10;color:#fbcfe8;font-size:0.7rem;text-decoration:none;padding:0.25rem 0.6rem;background:rgba(236,72,153,0.15);border:1px solid rgba(236,72,153,0.3);border-radius:8px;transition:all 0.25s" onmouseover="this.style.background='rgba(236,72,153,0.3)';this.style.boxShadow='0 0 15px rgba(236,72,153,0.3)'" onmouseout="this.style.background='rgba(236,72,153,0.15)';this.style.boxShadow=''">TPACK Xinjiang &#8594;</a>
  </div>
</section>

<!-- ========== METHODOLOGY ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Methodology</h2>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem">
    <div style="background:#fff;border:1px solid #e8edf5;border-radius:14px;padding:1.3rem;text-align:center;transition:transform 0.25s,box-shadow 0.25s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
      <div style="font-size:1.6rem;margin-bottom:0.5rem">&#128218;</div>
      <div style="font-size:0.85rem;font-weight:600;color:#1a1a2e">Systematic Reviews</div>
    </div>
    <div style="background:#fff;border:1px solid #e8edf5;border-radius:14px;padding:1.3rem;text-align:center;transition:transform 0.25s,box-shadow 0.25s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
      <div style="font-size:1.6rem;margin-bottom:0.5rem">&#128300;</div>
      <div style="font-size:0.85rem;font-weight:600;color:#1a1a2e">Mixed Methods</div>
    </div>
    <div style="background:#fff;border:1px solid #e8edf5;border-radius:14px;padding:1.3rem;text-align:center;transition:transform 0.25s,box-shadow 0.25s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
      <div style="font-size:1.6rem;margin-bottom:0.5rem">&#128202;</div>
      <div style="font-size:0.85rem;font-weight:600;color:#1a1a2e">Statistical Analysis</div>
    </div>
    <div style="background:#fff;border:1px solid #e8edf5;border-radius:14px;padding:1.3rem;text-align:center;transition:transform 0.25s,box-shadow 0.25s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.04)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
      <div style="font-size:1.6rem;margin-bottom:0.5rem">&#127919;</div>
      <div style="font-size:0.85rem;font-weight:600;color:#1a1a2e">Design-Based Research</div>
    </div>
  </div>
</section>

<!-- ========== INTERACTIVE TIMELINE ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Journey</h2>
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
  <h2 class="lt-section__title">Experience</h2>
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
