---
layout: single
title: "Research & Publications"
permalink: /publications/
author_profile: true
---

<style>
  .page__title { display: none; }
  /* G-style philosophy box */
  .pub-page { font-size: 0.95rem; line-height: 1.75; }
  .pub-page h2 {
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #2a7ae2;
    margin-top: 2.2rem; margin-bottom: 1rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #eef4ff;
  }
  .pub-page .research-stmt {
    position: relative;
    color: #374151;
    padding: 1.4rem 1.6rem;
    margin-bottom: 2.5rem;
    background: #fff;
    border-radius: 14px;
    line-height: 1.75;
    font-size: 0.92rem;
    border: 1px solid #e2e8f0;
    overflow: hidden;
    cursor: default;
    transition: box-shadow .4s, border-color .4s;
  }
  .pub-page .research-stmt:hover {
    box-shadow: 0 4px 24px rgba(99,102,241,.1);
    border-color: rgba(139,92,246,.2);
  }
  .pub-page .research-stmt::before {
    content: "\201C";
    position: absolute;
    top: -0.1rem; left: 0.8rem;
    font-size: 3.5rem;
    font-family: Georgia, serif;
    color: rgba(139,92,246,.12);
    line-height: 1;
  }
  .pub-page .research-stmt::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899, #f59e0b);
    opacity: 0;
    transition: opacity .4s;
  }
  .pub-page .research-stmt:hover::after {
    opacity: 1;
  }
  .pub-page .stats {
    font-size: 0.8rem; color: #718096; margin: -0.5rem 0 1.2rem;
  }

  /* ===== Year-grouped compact list ===== */
  .pub-page .pub-item p, .pub-page .conf-item p {
    margin: 0 !important;
    line-height: 1.5 !important;
  }
  .pub-page .pub-item__m, .pub-page .conf-item__m { margin-top: 7px !important; }
  .pub-page .pub-item__note { margin-top: 6px !important; line-height: 1.45 !important; }
  .pub-yr { display: grid; grid-template-columns: 64px 1fr; gap: 16px; }
  .pub-yr h3 { color: #C2185B; font-size: 1.15rem; font-weight: 700; margin: 0; padding-top: 16px; }
  .pub-item {
    display: flex; gap: 14px; padding: 12px 0;
    border-bottom: 1px solid #f0eef4; align-items: flex-start;
    color: inherit; text-decoration: none;
  }
  a.pub-item:hover .pub-item__t { color: #2a7ae2; }
  img.pub-item__th {
    flex: none; width: 86px; height: 64px; object-fit: cover;
    border-radius: 8px; border: 1px solid #eee9f3;
    transition: transform .3s ease, box-shadow .3s;
  }
  .pub-item:hover img.pub-item__th, .conf-item:hover img.pub-item__th {
    transform: scale(1.45); box-shadow: 0 10px 30px rgba(30,27,75,.2);
    position: relative; z-index: 5;
  }
  img.pub-item__th--tall { width: 58px; height: 76px; object-fit: cover; }
  .pub-item__icon {
    flex: none; width: 86px; height: 64px; border-radius: 8px;
    background: #f6f4fa; border: 1px solid #eee9f3;
    display: flex; align-items: center; justify-content: center; font-size: 1.5rem;
  }
  .pub-item__bd { min-width: 0; }
  .pub-item__t { font-size: .93rem; font-weight: 600; color: #1a1a2e; line-height: 1.5; }
  .pub-item__t .pub-badge { margin-left: 6px; vertical-align: 2px; }
  .pub-item__m { font-size: .8rem; color: #718096; margin-top: 2px; }
  .pub-item__m strong { color: #1a1a2e; }
  .pub-item__m i { color: #4a5568; }
  .pub-item__note { font-size: .74rem; color: #94a3b8; margin-top: 3px; }

  /* conference compact rows */
  .conf-item {
    display: flex; gap: 12px; padding: 11px 0;
    border-bottom: 1px solid #f4f2f7; align-items: baseline;
    color: inherit; text-decoration: none;
  }
  a.conf-item:hover .conf-item__t { color: #2a7ae2; }
  .conf-item--featured { align-items: flex-start; }
  .conf-item--featured img.pub-item__th--tall { margin-top: 2px; }
  .conf-item__y { flex: none; width: 64px; font-size: .8rem; font-weight: 700; color: #9a96ae; font-variant-numeric: tabular-nums; }
  .conf-item__bd { min-width: 0; }
  .conf-item__t { font-size: .88rem; font-weight: 600; color: #1a1a2e; line-height: 1.5; }
  .conf-item__t .pub-badge { margin-left: 6px; vertical-align: 2px; }
  .conf-item__m { font-size: .78rem; color: #718096; margin-top: 1px; }

  /* Badges */
  .pub-badge {
    font-size: 0.65rem;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    white-space: nowrap;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    display: inline-block;
  }
  .pub-badge--q1 { background: #dcfce7; color: #16a34a; }
  .pub-badge--q2 { background: #dbeafe; color: #2563eb; }
  .pub-badge--ur { background: #fef3c7; color: #d97706; }
  .pub-badge--upcoming { background: #ede9fe; color: #7c3aed; }
  .pub-badge--pdf { background: #fee2e2; color: #dc2626; }
  .pub-badge--doi { background: #dbeafe; color: #2563eb; }
  .pub-badge--web { background: #d1fae5; color: #059669; }
  .pub-badge--conf { background: #e0e7ff; color: #4f46e5; }
  .pub-badge--talk { background: #ffe4f0; color: #c2185b; }

  /* Responsive */
  @media (max-width: 768px) {
    .pub-page { font-size: 0.9rem; }
    .pub-page .research-stmt { padding: 1.2rem 1.3rem; font-size: 0.9rem; }
  }
  @media (max-width: 600px) {
    .pub-yr { grid-template-columns: 1fr; gap: 4px; }
    .pub-yr h3 { padding-top: 10px; }
    img.pub-item__th, .pub-item__icon { width: 68px; height: 52px; }
  }
</style>

<div class="pub-page">


<!-- ========== RESEARCH MAP ========== -->
<section style="margin:2.2rem 0 1rem">
  <h2>Research Strands</h2>
  <p style="font-size:0.92rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">My work moves across three interconnected strands. Click a circle to explore how they relate:</p>

  <div style="display:flex;justify-content:center;gap:0.4rem;margin-bottom:1.2rem;flex-wrap:wrap">
    <button class="rdr-fb rdr-fb--on" data-filter="all">All</button>
    <button class="rdr-fb" data-filter="publication">Publications</button>
    <button class="rdr-fb" data-filter="talk">Talks</button>
  </div>

  <p style="font-size:clamp(1.25rem,3.4vw,1.75rem);font-weight:700;line-height:1.35;margin:1.6rem 0 1.2rem;text-align:center;letter-spacing:-0.01em;background:linear-gradient(90deg,#6366f1,#8b5cf6,#ec4899);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#8b5cf6">Educators define learning, for people and for machines.</p>

  <div id="rmap" style="max-width:980px;margin:0 auto">
    <div id="rmap-box" aria-live="polite"></div>
    <svg id="rmap-svg" viewBox="0 0 1300 710" xmlns="http://www.w3.org/2000/svg" role="group" aria-label="Interactive research map" style="width:100%;height:auto;overflow:visible;display:block">
      <defs>
        <radialGradient id="rmap-g-outer" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f0f4ff" stop-opacity="0.5"/><stop offset="70%" stop-color="#e8ecf4" stop-opacity="0.25"/><stop offset="100%" stop-color="#dde3ee" stop-opacity="0.08"/></radialGradient>
        <filter id="rmap-shd" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur in="SourceAlpha" stdDeviation="4" result="b"/><feOffset dy="2" result="o"/>
          <feFlood flood-opacity="0.12" result="c"/><feComposite in="c" in2="o" operator="in" result="s"/>
          <feMerge><feMergeNode in="s"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
        
        <radialGradient id="rmap-g-lang" cx="50%" cy="60%" r="70%"><stop offset="0%" stop-color="#7dd3fc" stop-opacity="0.75"/><stop offset="45%" stop-color="#0ea5e9" stop-opacity="0.45"/><stop offset="100%" stop-color="#0369A1" stop-opacity="0.12"/></radialGradient>
        <radialGradient id="rmap-g-hai" cx="65%" cy="60%" r="70%"><stop offset="0%" stop-color="#c4b5fd" stop-opacity="0.75"/><stop offset="45%" stop-color="#8b5cf6" stop-opacity="0.45"/><stop offset="100%" stop-color="#7C3AED" stop-opacity="0.12"/></radialGradient>
        <radialGradient id="rmap-g-evid" cx="35%" cy="60%" r="70%"><stop offset="0%" stop-color="#fdba74" stop-opacity="0.75"/><stop offset="45%" stop-color="#f97316" stop-opacity="0.45"/><stop offset="100%" stop-color="#EA580C" stop-opacity="0.12"/></radialGradient>
      </defs>
      <g id="rmap-layer"></g>
    </svg>
    <div id="rmap-foot">
      <div class="rmap-hl"><span>Recent History</span></div>
      <div id="rmap-hist"></div>
    </div>
  </div>

  <style>
  .rdr-fb{font-size:.78rem;padding:.35rem .9rem;border-radius:20px;border:1px solid #cbd5e1;background:#fff;color:#475569;cursor:pointer;transition:all .25s;font-weight:500;font-family:inherit}
  .rdr-fb:hover{border-color:#94a3b8;background:#f8fafc;transform:translateY(-1px)}
  .rdr-fb--on{background:#1e293b;color:#fff;border-color:#1e293b;box-shadow:0 2px 8px rgba(30,41,59,.3)}
  @media(max-width:640px){.rdr-fb{font-size:.72rem;padding:.25rem .65rem}}
  @media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
  #rmap-box{--c:#1e1b4b;position:relative;max-width:600px;min-height:128px;margin:0 auto 22px;padding:.9rem 1.2rem 1rem;border:1.2px solid color-mix(in srgb,var(--c) 30%,#fff);border-radius:16px;background:#fff;text-align:center;box-sizing:border-box;box-shadow:0 3px 14px rgba(30,27,75,.08);transition:border-color .3s}
  #rmap-box::after{content:"";position:absolute;left:50%;bottom:-8.5px;width:14px;height:14px;background:#fff;border-right:1.2px solid color-mix(in srgb,var(--c) 30%,#fff);border-bottom:1.2px solid color-mix(in srgb,var(--c) 30%,#fff);transform:translateX(-50%) rotate(45deg);transition:border-color .3s}
  .rmap-kick{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--c)}
  .rmap-title{font-size:1.12rem;font-weight:800;color:#1a1a2e;line-height:1.35;margin-top:1px}
  .rmap-meta{font-size:.8rem;color:#64748b;margin-top:2px}
  .rmap-st{display:inline-block;padding:1px 7px;border-radius:10px;font-size:.68rem;font-weight:600;margin-left:3px}
  #rmap-box .rmap-desc{font-size:.88rem!important;color:#475569!important;line-height:1.55!important;margin:.35rem 0 0!important}
  #rmap-box .rmap-desc--sub{font-style:italic;color:#8a86a0!important}
  .rmap-chip{display:inline-block;margin:.45rem 3px 0;padding:1px 10px;border-radius:10px;font-size:.74rem;font-weight:700;color:var(--c);background:color-mix(in srgb,var(--c) 10%,#fff)}
  .rmap-link{display:inline-block;margin-top:.5rem;font-size:.84rem;font-weight:600}
  #rmap-svg text{font-family:inherit;-webkit-user-select:none;user-select:none;pointer-events:none}
  /* circles: satellites and the small current-term circle are clickable */
  .rmap-btn{cursor:pointer;outline:none}
  .rmap-btn .rmap-disc{transition:fill-opacity .25s,stroke-width .25s,stroke-opacity .25s}
  .rmap-bg{pointer-events:none}
  .rmap-sat .rmap-disc{fill-opacity:.75}
  .rmap-btn:hover .rmap-disc,.rmap-btn:focus-visible .rmap-disc{fill-opacity:1}
  .rmap-center.rmap-btn:hover .rmap-disc{stroke-opacity:.9}
  .rmap-off text{opacity:.55}
  /* term dots */
  #rmap-svg .rmap-item text{pointer-events:auto}
  .rmap-item{cursor:pointer;outline:none;animation:rmapFan .5s cubic-bezier(.34,1.3,.64,1) both}
  .rmap-item .rmap-dot{transform-box:fill-box;transform-origin:center;transition:transform .25s ease,filter .3s ease}
  .rmap-item:hover .rmap-dot,.rmap-item:focus-visible .rmap-dot{transform:scale(1.5);filter:drop-shadow(0 0 6px var(--ic))}
  .rmap-item:hover .rmap-l1,.rmap-item:focus-visible .rmap-l1{text-decoration:underline;fill:var(--ic)}
  .rmap-pulse{animation:rmapPulse 2s ease-in-out infinite}
  @keyframes rmapPulse{0%,100%{opacity:.3}50%{opacity:.65}}
  @keyframes rmapFan{from{opacity:0;transform:translate(var(--dx),var(--dy))}to{opacity:1;transform:none}}
  /* circle transitions: slide and resize from the previous layout, as on the Sage map */
  .rmap-flip{transform-box:fill-box;transform-origin:center;animation:rmapFlip .65s cubic-bezier(.4,0,.2,1) both}
  @keyframes rmapFlip{from{transform:translate(var(--fx),var(--fy)) scale(var(--fs))}to{transform:none}}
  .rmap-pop{transform-box:fill-box;transform-origin:center;animation:rmapPop .5s cubic-bezier(.34,1.56,.64,1) both}
  @keyframes rmapPop{from{opacity:0;transform:scale(.8)}to{opacity:1;transform:none}}
  .rmap-fade{animation:rmapFade .5s ease .15s both}
  .rmap-intro .rmap-fade{animation-duration:1.1s}
  .rmap-intro .rmap-item{animation-duration:1.3s;animation-timing-function:cubic-bezier(.22,1,.36,1)}
  .rmap-orbit{transform-origin:650px 225px;animation:rmapOrbit 2s cubic-bezier(.5,0,.2,1) both}
  @keyframes rmapOrbit{from{transform:rotate(-360deg)}to{transform:rotate(0deg)}}
  .rmap-intro .rmap-sat.rmap-fade{animation-duration:.8s}
  .rmap-intro .rmap-sat text{animation:rmapIn .7s ease 1.7s both}
  @keyframes rmapIn{from{opacity:0}}
  .rmap-wait *{animation-play-state:paused!important}
  html[data-theme="dark"] #rmap{background:#fff;border-radius:18px;padding:18px 14px}
  @keyframes rmapFade{from{opacity:0}to{opacity:1}}
  .rmap-back rect{fill:#fff;stroke:#94a3b8;stroke-width:1.3;transition:fill .2s,stroke .2s}
  .rmap-back:hover rect,.rmap-back:focus-visible rect{fill:#f8fafc;stroke:#475569}
  #rmap-foot{margin-top:.4rem}
  .rmap-hl{display:flex;align-items:center;gap:.9rem;font-size:.82rem;color:#64748b;font-weight:600}
  .rmap-hl::before,.rmap-hl::after{content:"";flex:1;height:1px;background:#e2e8f0}
  #rmap-hist{display:flex;gap:1.1rem;flex-wrap:wrap;min-height:58px;padding:.7rem .2rem 0}
  .rmap-hc{display:flex;flex-direction:column;align-items:center;gap:.3rem;max-width:120px;padding:0;border:0;background:none;font-family:inherit;font-size:.74rem;line-height:1.25;color:#475569;cursor:pointer;text-align:center}
  .rmap-hc i{width:14px;height:14px;border-radius:50%;border:2px solid var(--c);box-sizing:border-box;background:#fff;transition:background .2s}
  .rmap-hc:hover i{background:var(--c)}
  .rmap-hc:hover{text-decoration:underline}
  </style>

  <script>
  (function(){
    var NS='http://www.w3.org/2000/svg',RAD=Math.PI/180;
    var layer=document.getElementById('rmap-layer');
    var svg=document.getElementById('rmap-svg');
    var intro=true;
    var box=document.getElementById('rmap-box');
    var histEl=document.getElementById('rmap-hist');

    /* data: carried over unchanged from the radar */
    var S=[
      {id:'lang',lbl:['GenAI &','Language Learning'],sub:'IDLE · informal & self-directed learning',c:'#0369A1'},
      {id:'hai',lbl:['Human-AI Interaction &','Learning Design'],sub:'LLM tutors · guardrails · design cases',c:'#7C3AED'},
      {id:'evid',lbl:['Evidence, Equity &','Integrity'],sub:'Meta-analysis · authenticity · contexts',c:'#EA580C'}
    ];
    var CHIPS={
      lang:['language use','IDLE','GenAI tools'],
      hai:['design','agency','systems'],
      evid:['review','measurement','ethics']
    };
    var P=[
      {id:'genai',l:'GenAI Review · CAEAI (Q1) ’25',s:'lang',t:'publication',v:'Computers & Education: AI',y:2025,st:'Published',lk:'/publication/2025-two-years-innovation',d:'Systematic review of empirical GenAI research in language learning and teaching (2023–2024).'},
      {id:'doubao',l:'Doubao · PE (Q2) ’26',s:'lang',t:'publication',v:'Psicologia Educativa',y:2026,st:'Published',lk:'/publication/2026-doubao-genai-efl',d:'Doubao as a GenAI scaffold in senior high school EFL writing.'},
      {id:'mjss',l:'Interpreting · MJSS ’25',s:'lang',t:'publication',v:'MJSS',y:2025,st:'Published',lk:'/publication/2025-pointing-to-context',d:'Human vs. machine interpreting from a relevance theory perspective.'},
      {id:'idle-gai',l:'IDLE & GAI · Talk ’25',s:'lang',t:'talk',v:'Purdue AI in P-12',y:2025,st:'Presented',lk:null,d:'Extramural GAI-mediated IDLE and pragmatic competence of Chinese undergraduates.'},
      {id:'clil',l:'CLIL · Ed. Adv. ’23',s:'lang',t:'publication',v:'Education Advances',y:2023,st:'Published',lk:'/publication/2023-clil-translation',d:'MTI talent cultivation from the perspective of CLIL.'},
      {id:'pete-arxiv',l:'PeteChat DBR Case · arXiv ’26',s:'hai',t:'publication',v:'arXiv preprint',y:2026,st:'Published',lk:'/publication/2026-tutor-not-solver',d:'Tutor, not solver: eight design principles for a guardrailed, assessment-aware AI tutor.'},
      {id:'pete',l:'PeteChat Design Case · Springer',s:'hai',t:'publication',v:'Springer (in press)',y:2026,st:'Upcoming',lk:'/publication/answer-bot-to-tutor',d:'From answer bot to course tutor: a guardrailed AI assistant design case.'},
      {id:'claw',l:'Clawdbot Unboxed · Talk ’26',s:'hai',t:'talk',v:'AI Lunch & Learn, Purdue',y:2026,st:'Presented',lk:'/publication/2026-clawdbot-unboxed',d:'Invited talk: what Clawdbot does, why it’s hot, and where it breaks.'},
      {id:'aect26',l:'IDLE Pragmatics (ENA) · AECT ’26',s:'lang',t:'talk',v:'AECT Convention, Chicago',y:2026,st:'Upcoming',lk:null,d:'Scaffolding extramural GAI-mediated IDLE for pragmatic competence: an epistemic network analysis.'},
      {id:'pete26',l:'PeteChat · AECT ’26',s:'hai',t:'talk',v:'AECT Convention, Chicago',y:2026,st:'Upcoming',lk:null,d:'A design case of PeteChat: AI tutors that teach students how to think, not what to answer.'},
      {id:'aect25',l:'Artificial Authenticity · AECT ’25',s:'evid',t:'talk',v:'AECT Convention, Las Vegas',y:2025,st:'Presented',lk:'/publication/2025-aect-authenticity',d:'Higher education instructors’ perspectives on academic integrity in the age of generative AI.'}
    ];
    /* work-to-work links: the radar's web lines whose both ends still exist */
    var LINKS=[['genai','doubao'],['doubao','idle-gai'],['mjss','idle-gai'],['clil','mjss'],['genai','pete'],['pete','claw']];

    /* methods: titles, tags and descriptions copied from the Methodology cards */
    var M=[
      {id:'sr',lbl:['Systematic Reviews'],c:'#0D9488',chips:['PRISMA','Scoping','Meta-analyses'],d:'Able to conduct PRISMA-guided systematic literature reviews and multi-level meta-analyses end to end, from search strategy and screening to coding and effect-size synthesis.'},
      {id:'mm',lbl:['Mixed Methods'],c:'#7C3AED',chips:['Surveys','Interviews','Interventions'],d:'Triangulating surveys, interviews, and multi-week classroom interventions in convergent designs for richer, validated findings.'},
      {id:'st',lbl:['Statistics &','Learning Analytics'],c:'#0369A1',chips:['R','SPSS','Coh-Metrix','ONA'],d:'From descriptive and inferential statistics to learning analytics: regression and multilevel models in R and SPSS, Ordered Network Analysis (ONA), and text metrics with Coh-Metrix.'},
      {id:'dbr',lbl:['Design-Based Research'],c:'#EA580C',chips:['Iterative cycles','In-vivo prototyping'],d:'Translating findings into real tools through iterative design-test-refine cycles in authentic classroom contexts.'}
    ];
 /* which works use which method. DRAFT: only the three that name their method in their own title or summary */
    var USES={genai:['sr'],'pete-arxiv':['dbr'],aect26:['st']};
    /* one node table: root, strands, methods, works. soft = second line is secondary text */
    var N={root:{id:'root',k:'root',c:'#1e1b4b',lines:['AI × Education','Shared foundation'],soft:1,kick:'Shared foundation',d:'My work moves across three interconnected strands.'}};
    S.forEach(function(s){N[s.id]={id:s.id,k:'strand',s:s.id,c:s.c,lines:s.lbl,kick:'Research strand',d:s.sub,chips:CHIPS[s.id]};});
    M.forEach(function(m){N[m.id]={id:m.id,k:'method',c:m.c,lines:m.lbl,kick:'Method',d:m.d,chips:m.chips};});
    P.forEach(function(p){
      var a=p.l.split(' · ');
      N[p.id]={id:p.id,k:'work',s:p.s,c:N[p.s].c,lines:[a[0],a.slice(1).join(' · ')],soft:1,kick:p.t==='talk'?'Talk':'Publication',d:p.d,p:p};
    });
    function nm(n){return n.soft?n.lines[0]:n.lines.join(' ');}

    /* state: trail of visited terms, which satellite is expanded, filter */
    var flt='all',trail=['root'],exp=null,prev={},lastId=null;
    function cur(){return trail[trail.length-1];}
    function vis(id){var p=N[id].p;return !p||flt==='all'||p.t===flt;}

    /* up = part of, down = includes, side = related */
    function rel(id){
      var n=N[id],o={up:[],down:[],side:[]};
      if(n.k==='root'){
        o.down=S.map(function(s){return s.id;});
        o.side=M.map(function(m){return m.id;});
      }else if(n.k==='method'){
        o.up=['root'];
        o.down=P.filter(function(p){return (USES[p.id]||[]).indexOf(id)!==-1;}).sort(function(a,b){return b.y-a.y;}).map(function(p){return p.id;});
        o.side=M.filter(function(m){return m.id!==id;}).map(function(m){return m.id;});
      }
      else if(n.k==='strand'){
        o.up=['root'];
        o.down=P.filter(function(p){return p.s===id;}).sort(function(a,b){return b.y-a.y;}).map(function(p){return p.id;});
        o.side=S.filter(function(s){return s.id!==id;}).map(function(s){return s.id;});
      }else{
        o.up=[n.p.s];
        LINKS.forEach(function(l){if(l[0]===id)o.side.push(l[1]);if(l[1]===id)o.side.push(l[0]);});
      }
      o.down=o.down.filter(vis);o.side=o.side.filter(vis);
      return o;
    }

    function el(tag,at,txt){var e=document.createElementNS(NS,tag);for(var k in at)e.setAttribute(k,at[k]);if(txt!=null)e.textContent=txt;return e;}
    function stC(st){return st==='Published'?'#059669':st==='Upcoming'?'#d97706':'#6366f1';}
    function onAct(g,fn){
      g.addEventListener('click',fn);
      g.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();fn();}});
    }

    /* paint: the current term is the radar's white badge (ringed in its strand colour);
       the three satellites carry the radar's three colours, placed as on the radar
       (orange left, purple right, blue on the remaining side) */
    function paint(n){
      return {fill:'#fff',stroke:n.k==='root'?'#e2e8f0':n.c,so:n.k==='root'?'1':'.55',sw:n.k==='root'?'2':'3',text:'#1a1a2e',filter:'url(#rmap-shd)'};
    }
    var ROLE={
      up:{fill:'url(#rmap-g-evid)',stroke:'none',so:'0',sw:'0',line:'#EA580C',text:'#9a3412'},
      down:{fill:'url(#rmap-g-hai)',stroke:'none',so:'0',sw:'0',line:'#7C3AED',text:'#5b21b6'},
      side:{fill:'url(#rmap-g-lang)',stroke:'none',so:'0',sw:'0',line:'#0369A1',text:'#075985'}
    };

    /* geometry: default view, and the expanded view (one satellite opened into a ring) */
    var C0={x:650,y:225,r:135};
    var G={
      up:{x:445,y:225,r:180,a:180,dir:-1,R:232,step:20,max:100,lbl:'Part of',tx:-62,ty:0},
      down:{x:855,y:225,r:180,a:0,dir:1,R:232,step:20,max:100,lbl:'Includes',tx:62,ty:0},
      side:{x:650,y:425,r:165,a:90,dir:-1,R:215,step:70,max:110,lbl:'Related',tx:0,ty:52}
    };
    var EX={x:720,y:350,r:160,R:262},SM={x:190,y:350,r:95};
    var next,moved;

    /* a circle with centred text; animates from where the same circle sat in the previous layout */
    function disc(key,geo,pt,lines,fs,soft,tx,ty,cls,pop){
      var g=el('g',{class:cls}),p=prev[key];
      if(!p){g.classList.add('rmap-fade');}
      else if(p.x!==geo.x||p.y!==geo.y||p.r!==geo.r){
        g.classList.add('rmap-flip');moved=true;
        g.setAttribute('style','--fx:'+(p.x-geo.x)+'px;--fy:'+(p.y-geo.y)+'px;--fs:'+(p.r/geo.r));
      }else if(pop){g.classList.add('rmap-pop');}
      next[key]=geo;
      var at={cx:geo.x,cy:geo.y,r:geo.r,fill:pt.fill,stroke:pt.stroke,'stroke-opacity':pt.so,'stroke-width':pt.sw,class:'rmap-disc'};
      if(pt.filter)at.filter=pt.filter;
      g.appendChild(el('circle',at));
      var lh=fs*1.22,y0=geo.y+ty-(lines.length-1)*lh/2+fs*0.34;
      lines.forEach(function(t,i){
        var sec=soft&&i>0;
        g.appendChild(el('text',{x:geo.x+tx,y:y0+i*lh,'text-anchor':'middle','font-size':sec?fs*0.76:fs,'font-weight':sec?'600':'700',fill:sec?'#4a5568':pt.text},t));
      });
      layer.appendChild(g);
      return g;
    }

    /* term dots fanned around (cx,cy); same dot as the radar: white, coloured ring, soft core */
    function fan(ids,cx,cy,rEdge,R,a0,dir,step,delay){
      var n=ids.length;
      ids.forEach(function(id,i){
        var t=N[id],ang=(a0+dir*(i-(n-1)/2)*step)*RAD,cs=Math.cos(ang),sn=Math.sin(ang);
        var x=cx+R*cs,y=cy+R*sn;
        var it=el('g',{class:'rmap-item',tabindex:'0',role:'button','aria-label':t.lines.join(' '),
          style:'--ic:'+t.c+';--dx:'+((cx-x)*0.55).toFixed(1)+'px;--dy:'+((cy-y)*0.55).toFixed(1)+'px;animation-delay:'+(delay+i*(intro?0.45:0.05)).toFixed(2)+'s'});
        it.appendChild(el('line',{x1:cx+rEdge*cs,y1:cy+rEdge*sn,x2:x,y2:y,stroke:'#475569','stroke-width':'1.2','stroke-dasharray':'6 4',opacity:'.45'}));
        it.appendChild(el('circle',{cx:x,cy:y,r:24,fill:'transparent'}));
        var d=el('g',{class:'rmap-dot'});
        d.appendChild(t.k==='method'
          ?el('rect',{x:x-9.5,y:y-9.5,width:19,height:19,rx:3,transform:'rotate(45 '+x.toFixed(1)+' '+y.toFixed(1)+')',fill:'#fff',stroke:t.c,'stroke-width':'2.8'})
          :el('circle',{cx:x,cy:y,r:10.5,fill:'#fff',stroke:t.c,'stroke-width':'2.8'}));
        d.appendChild(el('circle',{cx:x,cy:y,r:4,fill:t.c,class:'rmap-pulse'}));
        it.appendChild(d);
        var two=t.lines.length>1;
        var an=cs>0.3?'start':cs<-0.3?'end':'middle';
        var lx=an==='start'?x+19:an==='end'?x-19:x;
        var ly=an!=='middle'?(two?y-3:y+6):sn>0?y+34:(two?y-38:y-20);
        it.appendChild(el('text',{x:lx,y:ly,'text-anchor':an,'font-size':'17','font-weight':'700',fill:'#1a1a2e',class:'rmap-l1'},t.lines[0]));
        if(two){
          it.appendChild(el('text',t.soft
            ?{x:lx,y:ly+18,'text-anchor':an,'font-size':'14.5',fill:'#64748b'}
            :{x:lx,y:ly+20,'text-anchor':an,'font-size':'17','font-weight':'700',fill:'#1a1a2e',class:'rmap-l1'},t.lines[1]));
        }
        onAct(it,function(){go(id);});
        layer.appendChild(it);
      });
    }

    function render(){
      var n=N[cur()],r=rel(n.id),changed=n.id!==lastId;
      if(exp&&!r[exp].length)exp=null;
      while(layer.firstChild)layer.removeChild(layer.firstChild);
      next={};moved=false;
      layer.appendChild(el('circle',exp?{cx:EX.x,cy:EX.y,r:EX.R+60,fill:'url(#rmap-g-outer)',class:'rmap-bg'}:{cx:C0.x,cy:C0.y+75,r:400,fill:'url(#rmap-g-outer)',class:'rmap-bg'}));
      if(!exp){
        /* default view: three satellites tucked behind the current term.
           on first load they circle the centre once before settling */
        var orbit=el('g',intro?{class:'rmap-orbit'}:{});layer.appendChild(orbit);
        ['up','down','side'].forEach(function(k){
          var g=G[k],ids=r[k],has=ids.length>0;
          var s=disc(k,{x:g.x,y:g.y,r:g.r},ROLE[k],[g.lbl],22,0,g.tx,g.ty,has?'rmap-sat rmap-btn':'rmap-sat rmap-off',false);
          if(has){
            s.setAttribute('tabindex','0');s.setAttribute('role','button');s.setAttribute('aria-label','Expand: '+g.lbl);
            onAct(s,function(){exp=k;render();});
          }
          orbit.appendChild(s);
        });
        var late=intro?2.2:moved?0.4:0.12;
        ['up','down','side'].forEach(function(k){
          var g=G[k],m=r[k].length;
          fan(r[k],g.x,g.y,g.r,g.R,g.a,g.dir,m>1?Math.min(g.step,g.max/(m-1)):0,late);
        });
        disc('c',C0,paint(n),n.lines,22,n.soft,0,0,'rmap-center',changed);
      }else{
        /* expanded view: the satellite opens into a ring; the current term steps aside */
        var ids=r[exp],m=ids.length;
        layer.appendChild(el('line',{x1:SM.x+SM.r,y1:SM.y,x2:EX.x-EX.r,y2:EX.y,stroke:ROLE[exp].line,'stroke-width':'1.5',opacity:'.5',class:'rmap-fade'}));
        var sm=disc('c',SM,paint(n),n.lines,15,n.soft,0,0,'rmap-center rmap-btn',false);
        sm.setAttribute('tabindex','0');sm.setAttribute('role','button');sm.setAttribute('aria-label','Back to '+nm(n));
        onAct(sm,collapse);
        disc(exp,{x:EX.x,y:EX.y,r:EX.r},ROLE[exp],[G[exp].lbl],27,0,0,0,'rmap-sat',false);
        fan(ids,EX.x,EX.y,EX.r,EX.R,0,1,m>1?Math.min(60,300/(m-1)):0,0.4);
        var bk=el('g',{class:'rmap-back rmap-btn rmap-fade',tabindex:'0',role:'button','aria-label':'Back'});
        bk.appendChild(el('line',{x1:SM.x,y1:SM.y+SM.r,x2:SM.x,y2:SM.y+SM.r+34,stroke:'#94a3b8','stroke-width':'1'}));
        bk.appendChild(el('rect',{x:SM.x-52,y:SM.y+SM.r+34,width:104,height:36,rx:18}));
        bk.appendChild(el('text',{x:SM.x,y:SM.y+SM.r+58,'text-anchor':'middle','font-size':'17','font-weight':'600',fill:'#475569'},'Back'));
        onAct(bk,collapse);
        layer.appendChild(bk);
      }
      prev=next;lastId=n.id;
      svg.classList.toggle('rmap-intro',intro);intro=false;

      /* info box */
      var h='<div class="rmap-kick">'+n.kick+'</div><div class="rmap-title">'+nm(n)+'</div>';
      if(n.p){
        var sc=stC(n.p.st);
        h+='<div class="rmap-meta">'+n.p.v+' · '+n.p.y+' <span class="rmap-st" style="background:'+sc+'18;color:'+sc+'">'+n.p.st+'</span></div>';
      }
      h+='<p class="rmap-desc'+(n.k==='strand'?' rmap-desc--sub':'')+'">'+n.d+'</p>';
      if(n.chips){h+='<div>'+n.chips.map(function(x){return '<span class="rmap-chip">'+x+'</span>';}).join('')+'</div>';}
      if(n.p&&n.p.lk){h+='<a class="rmap-link" href="'+n.p.lk+'">View details</a>';}
      box.style.setProperty('--c',n.c);
      box.innerHTML=h;

      /* recent history: latest first, no repeats, current term excluded */
      var seen={},out=[];seen[n.id]=1;
      for(var i=trail.length-2;i>=0&&out.length<6;i--){if(!seen[trail[i]]){seen[trail[i]]=1;out.push(trail[i]);}}
      histEl.innerHTML='';
      out.forEach(function(id){
        var b=document.createElement('button');
        b.type='button';b.className='rmap-hc';b.style.setProperty('--c',N[id].c);
        b.appendChild(document.createElement('i'));
        b.appendChild(document.createTextNode(nm(N[id])));
        b.addEventListener('click',function(){go(id);});
        histEl.appendChild(b);
      });
    }

    function go(id){if(id===cur())return;trail.push(id);exp=null;render();}
    function collapse(){exp=null;render();}

    var fbs=document.querySelectorAll('.rdr-fb[data-filter]');
    fbs.forEach(function(btn){
      btn.addEventListener('click',function(){
        fbs.forEach(function(b){b.classList.remove('rdr-fb--on');});
        btn.classList.add('rdr-fb--on');
        flt=btn.getAttribute('data-filter');
        render();
      });
    });

    render();
 /* hold the opening animation until the map scrolls into view */
    if('IntersectionObserver' in window){
      svg.classList.add('rmap-wait');
      var io=new IntersectionObserver(function(en){if(en[0].isIntersecting){svg.classList.remove('rmap-wait');io.disconnect();}},{threshold:0.4});
      io.observe(svg);
    }
  })();
  </script>
</section>

<!-- ========== METHODOLOGY (interactive pipeline) ========== -->
<section style="margin:1.6rem 0 2.2rem">
  <h2>Methodology</h2>
  <p style="font-size:0.88rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">I combine large-scale evidence synthesis with in-depth qualitative inquiry and iterative design. Each method feeds the next: reviews surface gaps, mixed methods explore them, statistics test claims, and design-based research translates findings into tools educators can actually use.</p>
  <style>
    .meth-wrap{display:flex;gap:14px}
    .meth-card{flex:1;padding:1.4rem 1rem;text-align:center;border-radius:14px;background:#fff;position:relative;cursor:default;
      opacity:0;transform:translateY(20px) scale(.96);transition:opacity .6s ease,transform .6s ease,box-shadow .4s,flex .5s ease}
    .meth-wrap.meth-visible .meth-card{opacity:1;transform:translateY(0) scale(1)}
    .meth-wrap.meth-visible .meth-card:nth-child(1){transition-delay:.1s}
    .meth-wrap.meth-visible .meth-card:nth-child(2){transition-delay:.3s}
    .meth-wrap.meth-visible .meth-card:nth-child(3){transition-delay:.5s}
    .meth-wrap.meth-visible .meth-card:nth-child(4){transition-delay:.7s}
    .meth-card:nth-child(1){box-shadow:0 4px 20px rgba(13,148,136,.12)}
    .meth-card:nth-child(2){box-shadow:0 4px 20px rgba(124,58,237,.12)}
    .meth-card:nth-child(3){box-shadow:0 4px 20px rgba(3,105,161,.12)}
    .meth-card:nth-child(4){box-shadow:0 4px 20px rgba(234,88,12,.12)}
    .meth-card:hover{transform:translateY(-6px) scale(1.03)!important;z-index:10;flex:1.5}
    .meth-card:nth-child(1):hover{box-shadow:0 10px 32px rgba(13,148,136,.22)}
    .meth-card:nth-child(2):hover{box-shadow:0 10px 32px rgba(124,58,237,.22)}
    .meth-card:nth-child(3):hover{box-shadow:0 10px 32px rgba(3,105,161,.22)}
    .meth-card:nth-child(4):hover{box-shadow:0 10px 32px rgba(234,88,12,.22)}
    .meth-num{font-size:1.8rem;font-weight:700;opacity:.35;margin-bottom:.15rem}
    .meth-title{font-size:.82rem;font-weight:700;margin-bottom:.25rem}
    .meth-sub{font-size:.65rem;color:#64748b;line-height:1.4}
    .meth-counter{margin-top:.5rem;font-size:1.05rem;font-weight:700;opacity:.65;font-variant-numeric:tabular-nums}
    .meth-counter-label{font-size:.5rem;text-transform:uppercase;letter-spacing:.06em;color:#94a3b8;font-weight:600}
    .meth-detail{max-height:0;overflow:hidden;transition:max-height .5s ease,opacity .4s ease,margin .4s ease;opacity:0;font-size:.62rem;color:#94a3b8;line-height:1.5;margin-top:0}
    .meth-card:hover .meth-detail{max-height:80px;opacity:1;margin-top:.5rem}
    .meth-dot{width:6px;height:6px;border-radius:50%;margin:8px auto 0;opacity:.4}
  </style>
  <div class="meth-wrap" id="meth-cards">
    <!-- Card 1 -->
    <div class="meth-card">
      <div class="meth-num" style="color:#0D9488">01</div>
      <div class="meth-title" style="color:#0D9488">Systematic Reviews</div>
      <div class="meth-sub">PRISMA · Scoping<br>Meta-analyses</div>
      <div class="meth-counter" style="color:#0D9488">Meta &amp; SLR</div>
      <div class="meth-counter-label">Evidence Synthesis</div>
      <div class="meth-detail">Able to conduct PRISMA-guided systematic literature reviews and multi-level meta-analyses end to end, from search strategy and screening to coding and effect-size synthesis.</div>
      <div class="meth-dot" style="background:#0D9488"></div>
    </div>
    <!-- Card 2 -->
    <div class="meth-card">
      <div class="meth-num" style="color:#7C3AED">02</div>
      <div class="meth-title" style="color:#7C3AED">Mixed Methods</div>
      <div class="meth-sub">Quan + Qual<br>Surveys · Interviews · Interventions</div>
      <div class="meth-counter" style="color:#7C3AED">Convergent</div>
      <div class="meth-counter-label">Design Approach</div>
      <div class="meth-detail">Triangulating surveys, interviews, and multi-week classroom interventions in convergent designs for richer, validated findings.</div>
      <div class="meth-dot" style="background:#7C3AED"></div>
    </div>
    <!-- Card 3 -->
    <div class="meth-card">
      <div class="meth-num" style="color:#0369A1">03</div>
      <div class="meth-title" style="color:#0369A1">Statistics &amp; Learning Analytics</div>
      <div class="meth-sub">R · SPSS · Coh-Metrix<br>ONA · effect sizes</div>
      <div class="meth-counter" style="color:#0369A1">Quant &amp; LA</div>
      <div class="meth-counter-label">Analysis Toolkit</div>
      <div class="meth-detail">From descriptive and inferential statistics to learning analytics: regression and multilevel models in R and SPSS, Ordered Network Analysis (ONA), and text metrics with Coh-Metrix.</div>
      <div class="meth-dot" style="background:#0369A1"></div>
    </div>
    <!-- Card 4 -->
    <div class="meth-card">
      <div class="meth-num" style="color:#EA580C">04</div>
      <div class="meth-title" style="color:#EA580C">Design-Based Research</div>
      <div class="meth-sub">Iterative cycles<br>In-vivo prototyping</div>
      <div class="meth-counter" style="color:#EA580C"><span class="meth-cnt" data-target="4">0</span></div>
      <div class="meth-counter-label">DBR Phases</div>
      <div class="meth-detail">Translating findings into real tools through iterative design-test-refine cycles in authentic classroom contexts.</div>
      <div class="meth-dot" style="background:#EA580C"></div>
    </div>
  </div>
  <script>
  (function(){
    var wrap=document.getElementById('meth-cards');if(!wrap)return;
    function countUp(el){var t=+el.dataset.target,d=Math.max(18,1400/t),n=0;el.textContent='0';var iv=setInterval(function(){n++;el.textContent=n;if(n>=t)clearInterval(iv);},d);}
    var fired=false;
    var obs=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting&&!fired){
          fired=true;
          wrap.classList.add('meth-visible');
          setTimeout(function(){wrap.querySelectorAll('.meth-cnt').forEach(function(c){countUp(c);});},800);
        }
      });
    },{threshold:0.3});
    obs.observe(wrap);
  })();
  </script>
</section>

<h2>Journal Articles &amp; Book Chapters</h2>

<p class="stats">
  <a href="{{ site.author.googlescholar }}">Google Scholar</a> &middot; Citation: {{ site.data.scholar.citations_all }} &middot; h-index: {{ site.data.scholar.h_index_all }}
</p>

<div class="pub-yr"><h3>2026</h3><div>

<a class="pub-item" href="/publication/2026-tutor-not-solver">
  <img class="pub-item__th" src="/images/pubs/petechat-arxiv-positioning.jpg" alt="PeteChat positioning figure">
  <div class="pub-item__bd">
    <p class="pub-item__t">Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat <span class="pub-badge pub-badge--web">arXiv preprint</span></p>
    <p class="pub-item__m">Li, B., <strong>*Tan, L.</strong>, Zakharov, W., Qiu, Q., &amp; Acton, C. &middot; <i>arXiv:2606.09845</i></p>
  </div>
</a>

<a class="pub-item" href="/publication/answer-bot-to-tutor">
  <img class="pub-item__th" src="/images/pubs/answer-bot-to-tutor.png" alt="PeteChat design story">
  <div class="pub-item__bd">
    <p class="pub-item__t">From Answer Bot to Course Tutor: A Practical Design Case of a Guardrailed AI Assistant in Higher Education <span class="pub-badge pub-badge--upcoming">In Press</span></p>
    <p class="pub-item__m">Li, B., <strong>*Tan, L.</strong>, Zakharov, W., Qiu, Q., &amp; Acton, C. &middot; <i>Invited book chapter, Springer</i></p>
  </div>
</a>

<a class="pub-item" href="/publication/2026-doubao-genai-efl">
  <img class="pub-item__th" src="/images/pubs/doubao-model.jpg" alt="AI-Human collaborative model">
  <div class="pub-item__bd">
    <p class="pub-item__t">Doubao as a GenAI Scaffold in Senior High School EFL Writing <span class="pub-badge pub-badge--q2">Q2</span></p>
    <p class="pub-item__m">Wang, S. &amp; <strong>*Tan, L.</strong> &middot; <i>Psicologia Educativa, 14</i>, 19&ndash;33</p>
  </div>
</a>

</div></div>

<div class="pub-yr"><h3>2025</h3><div>

<a class="pub-item" href="/publication/2025-two-years-innovation">
  <img class="pub-item__th" src="/images/pubs/two-years-edu-levels.jpg" alt="Educational levels distribution chart">
  <div class="pub-item__bd">
    <p class="pub-item__t">Two Years of Innovation: A Systematic Review of Empirical GenAI Research in Language Learning <span class="pub-badge pub-badge--q1">Q1 &middot; IF = 23.4</span></p>
    <p class="pub-item__m">Li, B., <strong>*Tan, L.Y.</strong>, Wang, C., &amp; Lowell, V. &middot; <i>Computers and Education: AI, 9</i>, 100445</p>
  </div>
</a>

<a class="pub-item" href="/publication/2025-pointing-to-context">
  <img class="pub-item__th" src="/images/pubs/mjss-cover.jpg" alt="Human vs machine interpreting">
  <div class="pub-item__bd">
    <p class="pub-item__t">Pointing to Context from a Relevance Theory Perspective: Human vs. Machine Interpreting</p>
    <p class="pub-item__m"><strong>*Tan, L.Y.</strong> &amp; Gao, L. &middot; <i>Mediterranean Journal of Social Sciences, 16</i>(3), 1</p>
    <p class="pub-item__note">Earlier version presented at the XXIInd International CALL Conference, Tokyo, Japan (2024).</p>
  </div>
</a>

</div></div>

<div class="pub-yr"><h3>2023</h3><div>

<a class="pub-item" href="/publication/2023-clil-translation">
  <img class="pub-item__th" src="/images/pubs/clil-cover.png" alt="CLIL paper">
  <div class="pub-item__bd">
    <p class="pub-item__t">Study on MTI Talent Cultivation Mode from the Perspective of CLIL</p>
    <p class="pub-item__m">Gao, L. &amp; <strong>*Tan, Y.</strong> &middot; <i>Education Advances, 13</i>(12), 10029&ndash;10034</p>
  </div>
</a>

</div></div>

<h2>Conference Presentations &amp; Invited Talks</h2>

<div class="conf-item">
  <span class="conf-item__y">2026</span>
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--conf">Conf</span> Scaffolding Extramural GAI-mediated Informal Digital Learning of English for Pragmatic Competence: An Epistemic Network Analysis <span class="pub-badge pub-badge--upcoming">Upcoming</span></p>
    <p class="conf-item__m"><strong>*Tan, L.</strong>, Lowell, V., Li, B., &amp; Fei, X. &middot; AECT International Convention, Chicago, IL &middot; Oct 2026</p>
  </div>
</div>

<div class="conf-item">
  <span class="conf-item__y">2026</span>
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--conf">Conf</span> A Design Case of PeteChat: Designing AI Tutors That Teach Students How to Think, Not What to Answer <span class="pub-badge pub-badge--upcoming">Upcoming</span></p>
    <p class="conf-item__m">Li, B., <strong>Tan, L.</strong>, Zakharov, W., Qiu, Q., &amp; Acton, C. &middot; AECT International Convention, Chicago, IL &middot; Oct 2026</p>
  </div>
</div>

<a class="conf-item conf-item--featured" href="/publication/2026-clawdbot-unboxed">
  <span class="conf-item__y">2026</span>
  <img class="pub-item__th pub-item__th--tall" src="/images/pubs/clawdbot-poster.jpg" alt="Clawdbot Unboxed talk poster">
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--talk">Talk</span> Clawdbot Unboxed: What It Does, Why It&rsquo;s Hot, and Where It Breaks</p>
    <p class="conf-item__m"><strong>Tan, L.</strong> &middot; Invited talk, AI Lunch and Learn Series, Purdue College of Education</p>
    <p class="pub-item__note">A hands-on unboxing of Clawdbot for the College of Education AI community &middot; poster and slides on the talk page.</p>
  </div>
</a>

<div class="conf-item">
  <span class="conf-item__y">2025</span>
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--conf">Conf</span> Assessing the Effects of Extramural GAI-mediated IDLE on Pragmatic Competence</p>
    <p class="conf-item__m"><strong>Tan, L.</strong>, Lowell, V. &amp; Li, B. &middot; Purdue AI in P-12 Conference, West Lafayette, IN</p>
  </div>
</div>

<div class="conf-item">
  <span class="conf-item__y">2025</span>
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--conf">Conf</span> Artificial Authenticity and Academic Integrity in an Age of Generative AI</p>
    <p class="conf-item__m">Li, B., Wang, J., &amp; <strong>Tan, L.</strong> &middot; AECT International Convention, Las Vegas, NV</p>
  </div>
</div>

<a class="conf-item" href="/publication/2024-call-context">
  <span class="conf-item__y">2024</span>
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--conf">Conf</span> Pointing to Context from a Relevance Theory Perspective: A Comparative Study of Human and Machine Interpreting</p>
    <p class="conf-item__m"><strong>Tan, L.</strong> &middot; XXIInd International CALL Conference, Tokyo, Japan &middot; Sep 2024</p>
  </div>
</a>

<a class="conf-item" href="/publication/2024-sociocultural-ai">
  <span class="conf-item__y">2024</span>
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--conf">Conf</span> Exploring the Extracurricular Development of AI-Assisted English Learners: A Phenomenological Exploration</p>
    <p class="conf-item__m"><strong>Tan, L.</strong> &amp; Zhang, Y. &middot; 3rd International Conference on Sociocultural Theory and Foreign Language Research, Guangdong, China &middot; May 2024</p>
  </div>
</a>

<!-- ========== RESEARCH TRAINING ========== -->
<section id="research-training" style="margin:1.6rem 0 2.2rem">
  <h2>Research Training</h2>
  <div style="padding:1.3rem 1.4rem;border-radius:14px;background:#fff;border:1px solid #eee9f3;box-shadow:0 4px 20px rgba(124,58,237,.08)">
    <p class="pub-item__t" style="margin:0">Modern Meta-Analysis Research Institute (MMARI) <span class="pub-badge" style="background:#ede9fe;color:#7c3aed">NSF-funded</span></p>
    <p class="pub-item__m" style="margin-top:4px">Chicago, IL &middot; July 2026</p>
    <p style="font-size:.85rem;color:#4a5568;line-height:1.7;margin:.7rem 0 0">Selected participant in an NSF-funded training institute on modern meta-analysis hosted by Georgia State University, learning from <a href="https://scholar.google.com/citations?user=4gzTEBYAAAAJ" target="_blank" rel="noopener">Terri Pigott</a>, <a href="https://scholar.google.com/citations?user=WPYewbEAAAAJ" target="_blank" rel="noopener">Ryan Williams</a>, and <a href="https://scholar.google.com/citations?user=8avc3psAAAAJ" target="_blank" rel="noopener">Elizabeth Tipton</a>, together with the institute&rsquo;s graduate students. The program covered effect-size computation and synthesis workflows in R/RStudio and Open Science practices for transparent, reproducible evidence synthesis. This training directly supports my evidence-synthesis research line.</p>
    <style>
      .mmari-strip{display:flex;gap:8px;margin-top:.9rem}
      .mmari-strip img{flex:1;min-width:0;height:90px;object-fit:cover;border-radius:8px;border:1px solid #eee9f3;transition:transform .3s ease,box-shadow .3s}
      .mmari-strip img:hover{transform:scale(2.2);box-shadow:0 10px 30px rgba(30,27,75,.25);position:relative;z-index:5}
      .mmari-strip img:first-child:hover{transform-origin:left center}
      .mmari-strip img:last-child:hover{transform-origin:right center}
    </style>
    <div class="mmari-strip">
      <img src="/images/mmari/1.jpg" alt="MMARI 2026 cohort, Chicago">
      <img src="/images/mmari/2.jpg" alt="MMARI 2026, Chicago" style="object-position:50% 18%">
      <img src="/images/mmari/3.jpg" alt="MMARI 2026, Chicago" style="object-position:50% 65%">
      <img src="/images/mmari/4.jpg" alt="MMARI 2026, Chicago">
      <img src="/images/mmari/5.jpg" alt="MMARI 2026 working session, Chicago" style="object-position:50% 28%">
    </div>
  </div>
</section>

</div>