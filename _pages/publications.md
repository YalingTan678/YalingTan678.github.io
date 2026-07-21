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


<!-- ========== RESEARCH STRANDS RADAR ========== -->
<section style="margin:2.2rem 0 1rem">
  <h2>Research Strands</h2>
  <p style="font-size:0.92rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">My work moves across three interconnected strands. Hover over each area to see how they relate:</p>

  <div style="display:flex;justify-content:center;gap:0.4rem;margin-bottom:1.2rem;flex-wrap:wrap">
    <button class="rdr-fb rdr-fb--on" data-filter="all">All</button>
    <button class="rdr-fb" data-filter="publication">Publications</button>
    <button class="rdr-fb" data-filter="talk">Talks</button>
    <button class="rdr-fb" data-filter="progress">In Progress</button>
  </div>

  <!-- ========== TAGLINE ========== -->
  <p style="font-size:clamp(1.25rem,3.4vw,1.75rem);font-weight:700;line-height:1.35;margin:1.6rem 0 0.4rem;text-align:center;letter-spacing:-0.01em;background:linear-gradient(90deg,#6366f1,#8b5cf6,#ec4899);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#8b5cf6">Educators define learning, for people and for machines.</p>

  <div id="rdr-wrap" style="position:relative;max-width:740px;margin:0 auto;-webkit-user-select:none;user-select:none">
    <svg id="rdr-svg" viewBox="0 0 900 760" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;overflow:visible;display:block"></svg>
    <div id="rdr-tip"></div>
  </div>

  <div id="rdr-modal">
    <div id="rdr-modal-card">
      <button id="rdr-modal-x">&times;</button>
      <div id="rdr-modal-body"></div>
    </div>
  </div>

  <style>
  .rdr-fb{font-size:.78rem;padding:.35rem .9rem;border-radius:20px;border:1px solid #cbd5e1;background:#fff;color:#475569;cursor:pointer;transition:all .25s;font-weight:500;font-family:inherit}
  .rdr-fb:hover{border-color:#94a3b8;background:#f8fafc;transform:translateY(-1px)}
  .rdr-fb--on{background:#1e293b;color:#fff;border-color:#1e293b;box-shadow:0 2px 8px rgba(30,41,59,.3)}
  #rdr-tip{display:none;position:absolute;pointer-events:none;background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:.65rem .9rem;box-shadow:0 4px 24px rgba(0,0,0,.14);z-index:10;max-width:250px;font-size:.8rem;line-height:1.5;backdrop-filter:blur(8px)}
  #rdr-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:100;justify-content:center;align-items:center}
  #rdr-modal-card{background:#fff;border-radius:14px;padding:1.4rem 1.8rem;max-width:400px;width:90%;box-shadow:0 8px 40px rgba(0,0,0,.15);position:relative;animation:rdr-modalIn .3s ease}
  @keyframes rdr-modalIn{from{opacity:0;transform:scale(.92) translateY(10px)}to{opacity:1;transform:scale(1) translateY(0)}}
  #rdr-modal-x{position:absolute;top:.5rem;right:.8rem;background:none;border:none;font-size:1.5rem;cursor:pointer;color:#94a3b8;line-height:1;transition:color .2s}
  #rdr-modal-x:hover{color:#475569}
  .rdr-ring{transform-origin:450px 380px}
  .rdr-ring circle{animation:rdr-ringSpin 60s linear infinite}
  @keyframes rdr-ringSpin{to{stroke-dashoffset:-100}}
  .rdr-outer{transform-origin:450px 380px;animation:rdr-outerSpin 90s linear infinite}
  @keyframes rdr-outerSpin{to{transform:rotate(360deg)}}
  .rdr-axis line{transition:opacity .3s,stroke-width .3s,stroke .3s}
  .rdr-axis-glow line{animation:rdr-axGlow 1.2s ease-in-out infinite;stroke-width:2px!important}
  @keyframes rdr-axGlow{0%,100%{opacity:.7}50%{opacity:1}}
  .rdr-dot{transform-box:fill-box;transform-origin:center;cursor:pointer;transition:transform .25s ease,opacity .3s ease,filter .3s ease}
  .rdr-dot:hover{transform:scale(1.6)!important;filter:drop-shadow(0 0 8px currentColor)}
  .rdr-dot.dim{opacity:.1!important}
  .rdr-dot.off{opacity:0!important;pointer-events:none}
  .rdr-dot-pulse{animation:rdr-dotPulse 2s ease-in-out infinite}
  @keyframes rdr-dotPulse{0%,100%{opacity:.25}50%{opacity:.55}}
  .rdr-dot-float{animation:rdr-float var(--dur,3s) ease-in-out infinite var(--del,0s)}
  @keyframes rdr-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
  .rdr-lbl{cursor:pointer;transition:opacity .3s}
  .rdr-lbl.dim{opacity:.15}
  .rdr-sector{transition:opacity .4s}
  .rdr-conn{pointer-events:none;transition:opacity .3s}
  .rdr-conn-anim{animation:rdr-dash .8s linear infinite}
  @keyframes rdr-dash{to{stroke-dashoffset:-14}}
  .rdr-mini{pointer-events:none}
  .rdr-mini-anim{animation:rdr-miniIn .3s ease both}
  @keyframes rdr-miniIn{from{opacity:0;transform:translateX(6px)}to{opacity:1;transform:translateX(0)}}
  .rdr-ripple{pointer-events:none}
  .rdr-ripple circle{animation:rdr-rippleOut .6s ease-out forwards}
  @keyframes rdr-rippleOut{from{r:9;opacity:.5}to{r:28;opacity:0}}
  .rdr-ellipse-breathe{animation:rdr-breathe 4s ease-in-out infinite}
  @keyframes rdr-breathe{0%,100%{opacity:var(--base-op,.75)}50%{opacity:calc(var(--base-op,.75) - .06)}}
  @media(max-width:640px){.rdr-fb{font-size:.72rem;padding:.25rem .65rem}}
  @media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
  </style>

  <script>
  (function(){
    var CX=450,CY=380,RINGS=[80,160,240],ALEN=280,RAD=Math.PI/180;
    var svg=document.getElementById('rdr-svg');
    var tip=document.getElementById('rdr-tip');
    var wrap=document.getElementById('rdr-wrap');
    var modal=document.getElementById('rdr-modal');
    var mBody=document.getElementById('rdr-modal-body');

    var S=[
      {id:'lang',lbl:['GenAI &','Language Learning'],sub:'IDLE \u00b7 informal & self-directed learning',c:'#0369A1',a:270,lx:450,ly:65,an:'middle'},
      {id:'hai',lbl:['Human-AI Interaction &','Learning Design'],sub:'LLM tutors \u00b7 guardrails \u00b7 design cases',c:'#7C3AED',a:30,lx:735,ly:640,an:'start'},
      {id:'evid',lbl:['Evidence, Equity &','Integrity'],sub:'Meta-analysis \u00b7 authenticity \u00b7 contexts',c:'#EA580C',a:150,lx:165,ly:640,an:'end'}
    ];
    var sMap={};S.forEach(function(s){sMap[s.id]=s;});

    var P=[
      {id:'genai',l:'GenAI Review \u00b7 CAEAI (Q1) \u201925',s:'lang',a:243,r:140,t:'publication',v:'Computers & Education: AI',y:2025,st:'Published',lk:'/publication/2025-two-years-innovation',d:'Systematic review of empirical GenAI research in language learning and teaching (2023\u20132024).'},
      {id:'doubao',l:'Doubao \u00b7 PE (Q2) \u201926',s:'lang',a:296,r:170,t:'publication',v:'Psicologia Educativa',y:2026,st:'Published',lk:'/publication/2026-doubao-genai-efl',d:'Doubao as a GenAI scaffold in senior high school EFL writing.'},
      {id:'mjss',l:'Interpreting \u00b7 MJSS \u201925',s:'lang',a:305,r:210,t:'publication',v:'MJSS',y:2025,st:'Published',lk:'/publication/2025-pointing-to-context',d:'Human vs. machine interpreting from a relevance theory perspective.'},
      {id:'idle-gai',l:'IDLE & GAI \u00b7 Talk \u201925',s:'lang',a:232,r:215,t:'talk',v:'Purdue AI in P-12',y:2025,st:'Presented',lk:null,d:'Extramural GAI-mediated IDLE and pragmatic competence of Chinese undergraduates.'},
      {id:'clil',l:'CLIL \u00b7 Ed. Adv. \u201923',s:'lang',a:268,r:235,t:'publication',v:'Education Advances',y:2023,st:'Published',lk:'/publication/2023-clil-translation',d:'MTI talent cultivation from the perspective of CLIL.'},
      {id:'pete',l:'PeteChat Design Case \u00b7 Springer',s:'hai',a:20,r:160,t:'publication',v:'Springer (in press)',y:2026,st:'Upcoming',lk:'/publication/answer-bot-to-tutor',d:'From answer bot to course tutor: a guardrailed AI assistant design case.'},
      {id:'claw',l:'Clawdbot Unboxed \u00b7 Talk \u201926',s:'hai',a:48,r:205,t:'talk',v:'AI Lunch & Learn, Purdue',y:2026,st:'Presented',lk:'/publication/2026-clawdbot-unboxed',d:'Invited talk: what Clawdbot does, why it\u2019s hot, and where it breaks.'},
      {id:'aera',l:'Meta-analysis \u00b7 AERA \u201926',s:'evid',a:160,r:150,t:'talk',v:'AERA Convention',y:2026,st:'Upcoming',lk:null,d:'Meta-analysis on technology and the achievement of students from low-income families.'},
      {id:'auth',l:'Authorship & AI',s:'evid',a:130,r:205,t:'progress',v:'Under review',y:2026,st:'In Review',lk:null,d:'Faculty perspectives on originality and AI-mediated composition.'},
      {id:'tpxj',l:'TPACK & Culture',s:'evid',a:175,r:225,t:'progress',v:'Under review',y:2026,st:'In Review',lk:null,d:'Cultural context and technology integration knowledge among trainee teachers.'}
    ];
    /* helpers */
    function pol(a,r){return{x:CX+r*Math.cos(a*RAD),y:CY+r*Math.sin(a*RAD)};}
    function el(tag,at){var e=document.createElementNS('http://www.w3.org/2000/svg',tag);for(var k in at)e.setAttribute(k,at[k]);return e;}
    function pPos(p){return pol(p.a!=null?p.a:sMap[p.s].a,p.r);}
    function pClr(p){if(!p.cs)return sMap[p.s].c;var a=sMap[p.cs[0]].c,b=sMap[p.cs[1]].c;return bHex(a,b);}
    function bHex(a,b){var r=(parseInt(a.slice(1,3),16)+parseInt(b.slice(1,3),16))>>1,g=(parseInt(a.slice(3,5),16)+parseInt(b.slice(3,5),16))>>1,l=(parseInt(a.slice(5,7),16)+parseInt(b.slice(5,7),16))>>1;return'#'+((1<<24)|(r<<16)|(g<<8)|l).toString(16).slice(1);}
    function secP(sa,ea,r){var sp=pol(sa,r),ep=pol(ea,r),sw=((ea-sa+360)%360);return'M '+CX+' '+CY+' L '+sp.x.toFixed(1)+' '+sp.y.toFixed(1)+' A '+r+' '+r+' 0 '+(sw>180?1:0)+' 1 '+ep.x.toFixed(1)+' '+ep.y.toFixed(1)+' Z';}
    function stC(st){return st==='Published'?'#059669':st==='Upcoming'?'#d97706':'#6366f1';}

    /* build SVG */
 /* defs (shadow filter) */
    var defs=el('defs',{});
    var filt=el('filter',{id:'rdr-shd',x:'-30%',y:'-30%',width:'160%',height:'160%'});
    filt.appendChild(el('feGaussianBlur',{in:'SourceAlpha',stdDeviation:'3',result:'b'}));
    filt.appendChild(el('feOffset',{dy:'2',result:'o'}));
    filt.appendChild(el('feFlood',{'flood-opacity':'0.1',result:'c'}));
    filt.appendChild(el('feComposite',{in:'c',in2:'o',operator:'in',result:'s'}));
    var mg=el('feMerge',{});mg.appendChild(el('feMergeNode',{in:'s'}));mg.appendChild(el('feMergeNode',{in:'SourceGraphic'}));
    filt.appendChild(mg);defs.appendChild(filt);

 /* radial gradients for strand ellipses */
    var gradData=[
      {id:'grad-lang',cx:'50%',cy:'35%',stops:[['0%','#7dd3fc',0.75],['45%','#0ea5e9',0.45],['100%','#0369A1',0.12]]},
      {id:'grad-hai',cx:'65%',cy:'60%',stops:[['0%','#c4b5fd',0.75],['45%','#8b5cf6',0.45],['100%','#7C3AED',0.12]]},
      {id:'grad-evid',cx:'35%',cy:'60%',stops:[['0%','#fdba74',0.75],['45%','#f97316',0.45],['100%','#EA580C',0.12]]}
    ];
    gradData.forEach(function(gd){
      var rg=el('radialGradient',{id:gd.id,cx:gd.cx,cy:gd.cy,r:'70%'});
      gd.stops.forEach(function(s){rg.appendChild(el('stop',{offset:s[0],'stop-color':s[1],'stop-opacity':s[2]}));});
      defs.appendChild(rg);
    });
 /* outer glow gradient */
    var outerGrad=el('radialGradient',{id:'grad-outer',cx:'50%',cy:'50%',r:'50%'});
    outerGrad.appendChild(el('stop',{offset:'0%','stop-color':'#f0f4ff','stop-opacity':'0.5'}));
    outerGrad.appendChild(el('stop',{offset:'70%','stop-color':'#e8ecf4','stop-opacity':'0.25'}));
    outerGrad.appendChild(el('stop',{offset:'100%','stop-color':'#dde3ee','stop-opacity':'0.08'}));
    defs.appendChild(outerGrad);
    svg.appendChild(defs);

 /* large background circle (slow rotation) */
    var outerCircle=el('circle',{cx:CX,cy:CY,r:RINGS[2]+40,fill:'url(#grad-outer)',stroke:'#e2e8f0','stroke-width':'.5','stroke-dasharray':'8 5',opacity:'.6',class:'rdr-outer'});
    svg.appendChild(outerCircle);

 /* four gradient ellipses behind each strand */
    var ellipseData=[
      {grad:'grad-lang',cx:CX,cy:CY-130,rx:250,ry:240},
      {grad:'grad-hai',cx:CX+130,cy:CY+110,rx:250,ry:230},
      {grad:'grad-evid',cx:CX-130,cy:CY+110,rx:250,ry:230}
    ];
    var strandEllipses={};
    var sIds=['lang','hai','evid'];
    ellipseData.forEach(function(ed,i){
      var ell=el('ellipse',{cx:ed.cx,cy:ed.cy,rx:ed.rx,ry:ed.ry,fill:'url(#'+ed.grad+')',opacity:'0',class:'rdr-ellipse-breathe',style:'pointer-events:none;transition:opacity .4s ease;--base-op:.75'});
      svg.appendChild(ell);
      strandEllipses[sIds[i]]=ell;
    });

 /* sectors (highlight on strand hover) */
    var sectors={};
    S.forEach(function(s){
      var p=el('path',{d:secP(s.a-60,s.a+60,RINGS[2]),fill:s.c,opacity:'0',class:'rdr-sector','data-s':s.id});
      svg.appendChild(p);sectors[s.id]=p;
    });

 /* concentric rings */
    var ringEls=[];
    RINGS.forEach(function(r){
      var g=el('g',{class:'rdr-ring',style:'opacity:0;transform:scale(0)'});
      g.appendChild(el('circle',{cx:CX,cy:CY,r:r,fill:'none',stroke:'#d1d5db','stroke-width':'1','stroke-dasharray':'6 4',opacity:'.45'}));
      svg.appendChild(g);ringEls.push(g);
    });

 /* axes */
    var axEls={};
    S.forEach(function(s){
      var end=pol(s.a,ALEN);
      var g=el('g',{class:'rdr-axis','data-s':s.id,style:'opacity:0'});
      g.appendChild(el('line',{x1:CX,y1:CY,x2:end.x.toFixed(1),y2:end.y.toFixed(1),stroke:'#cbd5e1','stroke-width':'.8',opacity:'.6'}));
      svg.appendChild(g);axEls[s.id]=g;
    });

 /* center badge */
    var badge=el('g',{style:'opacity:0'});
    badge.appendChild(el('circle',{cx:CX,cy:CY,r:70,fill:'#fff',stroke:'#e2e8f0','stroke-width':'1.5',filter:'url(#rdr-shd)'}));
    var ct1=el('text',{x:CX,y:CY-6,'text-anchor':'middle','font-size':'15.5','font-weight':'700',fill:'#1e1b4b',opacity:'.8'});
    ct1.textContent='AI \u00d7 Education';
    var ct2=el('text',{x:CX,y:CY+16,'text-anchor':'middle','font-size':'11.5','font-weight':'700',fill:'#4a5568',opacity:'.85'});
    ct2.textContent='Shared foundation';
    badge.appendChild(ct1);badge.appendChild(ct2);svg.appendChild(badge);

 /* connection line (dot-to-center on hover) */
    var conn=el('line',{x1:CX,y1:CY,x2:CX,y2:CY,stroke:'transparent','stroke-width':'1.5','stroke-dasharray':'4 3',class:'rdr-conn',opacity:'0'});
    svg.appendChild(conn);

 /* strand labels as cards (Venn stays untouched behind) */
    var lblEls={};
    var CARD={
      lang:{x:289,y:18},
      hai:{x:572,y:592},
      evid:{x:6,y:592}
    };
    var CHIPS={
      lang:['language use','IDLE','GenAI tools'],
      hai:['design','agency','systems'],
      evid:['review','measurement','ethics']
    };
    S.forEach(function(s){
      var g=el('g',{class:'rdr-lbl','data-s':s.id,style:'opacity:0'});
      var cw=322, ch=112, cx=CARD[s.id].x, cy=CARD[s.id].y;
      g.appendChild(el('rect',{x:cx,y:cy,width:cw,height:ch,rx:16,fill:'#ffffff','fill-opacity':'0.94',
        stroke:s.c,'stroke-opacity':'0.28','stroke-width':'1.2',filter:'url(#rdr-shd)',style:'cursor:pointer'}));
 /* plus icon */
      g.appendChild(el('circle',{cx:cx+28,cy:cy+32,r:12,fill:s.c,'fill-opacity':'0.14'}));
      var plus=el('text',{x:cx+28,y:cy+37,'text-anchor':'middle','font-size':'15','font-weight':'700',fill:s.c});
      plus.textContent='+';g.appendChild(plus);
 /* title lines */
      s.lbl.forEach(function(line,j){
        var t=el('text',{x:cx+48,y:cy+28+j*20,'font-size':'16.5','font-weight':'800',fill:'#1a1a2e'});
        t.textContent=line;g.appendChild(t);
      });
 /* subtitle */
      var subY=cy+28+s.lbl.length*20+3;
      var sub=el('text',{x:cx+48,y:subY,'font-size':'13',fill:'#8a86a0','font-style':'italic'});
      sub.textContent=s.sub;g.appendChild(sub);
 /* chips */
      var chipX=cx+48;
      CHIPS[s.id].forEach(function(cName){
        var w=cName.length*7+20;
        g.appendChild(el('rect',{x:chipX,y:subY+9,width:w,height:19,rx:9.5,fill:s.c,'fill-opacity':'0.10'}));
        var t=el('text',{x:chipX+w/2,y:subY+22.5,'text-anchor':'middle','font-size':'11.5',fill:s.c,'font-weight':'700'});
        t.textContent=cName;g.appendChild(t);
        chipX+=w+7;
      });
      svg.appendChild(g);lblEls[s.id]=g;
    });

 /* paper dots */
    var dots=[];
    P.forEach(function(p){
      var pos=pPos(p),c=pClr(p);
      var floatDur=(2.5+Math.random()*1.5).toFixed(1);
      var floatDel=(Math.random()*2).toFixed(1);
      var g=el('g',{class:'rdr-dot rdr-dot-float','data-p':p.id,'data-t':p.t,style:'opacity:0;--dur:'+floatDur+'s;--del:'+floatDel+'s'});
      g.appendChild(el('circle',{cx:pos.x.toFixed(1),cy:pos.y.toFixed(1),r:'9',fill:'#fff',stroke:c,'stroke-width':'2.5'}));
      g.appendChild(el('circle',{cx:pos.x.toFixed(1),cy:pos.y.toFixed(1),r:'3.5',fill:c,opacity:'.4',class:'rdr-dot-pulse'}));
      svg.appendChild(g);
      dots.push({el:g,p:p,pos:pos,c:c});
    });

 /* web lines connecting dots */
    var webLinks=[
      ['genai','doubao'],['doubao','idle-gai'],['mjss','idle-gai'],['clil','mjss'],
      ['genai','pete'],['pete','claw'],
      ['aera','auth'],['auth','tpxj'],
      ['doubao','auth'],['idle-gai','tpxj']
    ];
    var dotMap={};dots.forEach(function(d){dotMap[d.p.id]=d;});
    var webEls=[];
    webLinks.forEach(function(pair){
      var a=dotMap[pair[0]],b=dotMap[pair[1]];
      if(!a||!b)return;
      var ln=el('line',{x1:a.pos.x.toFixed(1),y1:a.pos.y.toFixed(1),x2:b.pos.x.toFixed(1),y2:b.pos.y.toFixed(1),
        stroke:'#475569','stroke-width':'1.2','stroke-dasharray':'6 4',opacity:'.5',style:'pointer-events:none;transition:opacity .5s'});
      svg.insertBefore(ln,dots[0].el);
      webEls.push(ln);
    });

    /* ---- entry animation ---- */
    var entered=false;
    function runEntry(){
      if(entered)return;entered=true;
      var ease='cubic-bezier(0.34,1.56,0.64,1)';
 /* ellipses bloom in first */
      sIds.forEach(function(id,i){
        setTimeout(function(){strandEllipses[id].style.transition='opacity .8s ease';strandEllipses[id].style.opacity='.75';},i*120);
      });
 /* then rings expand */
      ringEls.forEach(function(r,i){
        setTimeout(function(){r.style.transition='opacity .7s ease,transform .7s '+ease;r.style.opacity='1';r.style.transform='scale(1)';},300+i*150);
      });
      var sids=Object.keys(axEls);
      sids.forEach(function(k,i){setTimeout(function(){axEls[k].style.transition='opacity .5s ease';axEls[k].style.opacity='1';},650+i*80);});
      setTimeout(function(){badge.style.transition='opacity .5s ease';badge.style.opacity='1';},750);
      dots.forEach(function(d,i){
        setTimeout(function(){d.el.style.transition='opacity .35s ease,transform .35s '+ease;d.el.style.opacity='1';d.el.style.transform='scale(1)';},850+i*65);
      });
      S.forEach(function(s,i){setTimeout(function(){lblEls[s.id].style.transition='opacity .5s ease';lblEls[s.id].style.opacity='1';},1200+i*70);});
 /* web lines fade in after dots */
      webEls.forEach(function(ln,i){
        setTimeout(function(){ln.setAttribute('opacity','.45');},1100+i*50);
      });
    }
    var obs=new IntersectionObserver(function(en){if(en[0].isIntersecting){runEntry();obs.disconnect();}},{threshold:.15});
    obs.observe(svg);

    /* ---- strand hover ---- */
    var miniEls=[];
    function clrMini(){miniEls.forEach(function(e){if(e.parentNode)e.parentNode.removeChild(e);});miniEls=[];}

    function hiStrand(sid){
      S.forEach(function(s){sectors[s.id].setAttribute('opacity',s.id===sid?'.22':'0');});
      S.forEach(function(s){
        var ln=axEls[s.id].querySelector('line');
        if(s.id===sid){ln.setAttribute('opacity','1');ln.setAttribute('stroke-width','1.5');ln.setAttribute('stroke',s.c);axEls[s.id].classList.add('rdr-axis-glow');}
        else{ln.setAttribute('opacity','.12');ln.setAttribute('stroke-width','.8');ln.setAttribute('stroke','#cbd5e1');axEls[s.id].classList.remove('rdr-axis-glow');}
      });
      S.forEach(function(s){lblEls[s.id].classList.toggle('dim',s.id!==sid);});
      S.forEach(function(s){
        if(strandEllipses[s.id]){
          strandEllipses[s.id].setAttribute('opacity',s.id===sid?'1':'.12');
          strandEllipses[s.id].style.animationPlayState=s.id===sid?'paused':'running';
        }
      });
      clrMini();
      var ownDots=[];
      dots.forEach(function(d){
        var own=(d.p.s===sid)||(d.p.cs&&d.p.cs.indexOf(sid)!==-1);
        d.el.classList.toggle('dim',!own);
        if(own) ownDots.push(d);
      });
 /* sort by angle so nearby dots get alternating sides */
      ownDots.sort(function(a,b){
        var aa=a.p.a!=null?a.p.a:(sMap[a.p.s]?sMap[a.p.s].a:0);
        var ba=b.p.a!=null?b.p.a:(sMap[b.p.s]?sMap[b.p.s].a:0);
        return aa-ba;
      });
      var placed=[];
      ownDots.forEach(function(d,ownIdx){
        var line1=d.p.l, line2=d.p.v+' \u00b7 '+d.p.y;
        var W=Math.max(line1.length*7.4, line2.length*6.1)+22; /* fit-to-text plate */
        var dx=d.pos.x-CX,dy=d.pos.y-CY;
        var sides=dx<0?[{lx:d.pos.x-16,la:'end'},{lx:d.pos.x+16,la:'start'}]:[{lx:d.pos.x+16,la:'start'},{lx:d.pos.x-16,la:'end'}];
        if(Math.abs(dx)<60){sides=ownIdx%2===0?[{lx:d.pos.x+16,la:'start'},{lx:d.pos.x-16,la:'end'}]:[{lx:d.pos.x-16,la:'end'},{lx:d.pos.x+16,la:'start'}];}
        var chosen=sides[0], chosenOff=0, found=false;
        [0,46,-46,92].forEach(function(off){
          if(found)return;
          sides.forEach(function(sd){
            if(found)return;
            var rx=sd.la==='start'?sd.lx-4:sd.lx-(W-4);
            var ry=d.pos.y-21+off;
            var collision=false;
            for(var pi=0;pi<placed.length;pi++){
              var p=placed[pi];
              if(rx<p.x+p.w&&rx+W+4>p.x&&ry<p.y+p.h&&ry+44>p.y){collision=true;break;}
            }
            if(!collision){chosen=sd;chosenOff=off;found=true;}
          });
        });
        var lx=chosen.lx,la=chosen.la,oy=d.pos.y+chosenOff;
        var bgX=la==='start'?lx-4:lx-(W-4);
        placed.push({x:bgX,y:oy-23,w:W+4,h:44});
        var bg=el('rect',{x:bgX,y:oy-21,width:W,height:40,rx:5,fill:'#fff',opacity:'.92',class:'rdr-mini'});
        svg.appendChild(bg);miniEls.push(bg);
        var t=el('text',{x:lx,y:oy-4,'text-anchor':la,'font-size':'14','font-weight':'700',fill:d.c,class:'rdr-mini rdr-mini-anim'});
        t.textContent=line1;svg.appendChild(t);miniEls.push(t);
        var t2=el('text',{x:lx,y:oy+13,'text-anchor':la,'font-size':'11.5',fill:'#64748b',class:'rdr-mini rdr-mini-anim',style:'animation-delay:.08s'});
        t2.textContent=line2;svg.appendChild(t2);miniEls.push(t2);
      });
    }

    function resetHi(){
      S.forEach(function(s){
        sectors[s.id].setAttribute('opacity','0');
        var ln=axEls[s.id].querySelector('line');
        ln.setAttribute('opacity','.6');ln.setAttribute('stroke-width','.8');ln.setAttribute('stroke','#cbd5e1');
        axEls[s.id].classList.remove('rdr-axis-glow');
        lblEls[s.id].classList.remove('dim');
        if(strandEllipses[s.id]){strandEllipses[s.id].setAttribute('opacity','.75');strandEllipses[s.id].style.animationPlayState='';}
      });
      dots.forEach(function(d){d.el.classList.remove('dim');});
      clrMini();
      tip.style.display='none';
      conn.setAttribute('stroke','transparent');conn.setAttribute('opacity','0');conn.classList.remove('rdr-conn-anim');
    }

    S.forEach(function(s){
      [lblEls[s.id],axEls[s.id]].forEach(function(elem){
        elem.addEventListener('mouseenter',function(){hiStrand(s.id);});
        elem.addEventListener('mouseleave',resetHi);
        elem.addEventListener('touchstart',function(e){e.preventDefault();hiStrand(s.id);},{passive:false});
      });
    });

    /* ---- dot hover / tooltip ---- */
    function showTip(d){
      var wr=wrap.getBoundingClientRect(),sr=svg.getBoundingClientRect();
      var tx=sr.left+(d.pos.x/900)*sr.width-wr.left;
      var ty=sr.top+(d.pos.y/760)*sr.height-wr.top;
      var sc=stC(d.p.st);
      tip.innerHTML='<div style="font-weight:700;color:#1e293b;margin-bottom:2px">'+d.p.l+'</div>'+
        '<div style="color:#64748b;font-size:.73rem">'+d.p.v+' \u00b7 '+d.p.y+'</div>'+
        '<div style="margin-top:3px"><span style="display:inline-block;padding:1px 7px;border-radius:10px;font-size:.68rem;font-weight:600;background:'+sc+'18;color:'+sc+'">'+d.p.st+'</span></div>';
      tip.style.display='block';
      var left=tx+15,top=ty-10;
      if(left+260>wr.offsetWidth)left=tx-265;
      if(top<0)top=ty+15;
      tip.style.left=left+'px';tip.style.top=top+'px';
      conn.setAttribute('x2',d.pos.x.toFixed(1));conn.setAttribute('y2',d.pos.y.toFixed(1));
      conn.setAttribute('stroke',d.c);conn.setAttribute('opacity','.5');conn.classList.add('rdr-conn-anim');
      if(d.p.cs){
        S.forEach(function(s){
          var ln=axEls[s.id].querySelector('line');
          if(d.p.cs.indexOf(s.id)!==-1){ln.setAttribute('opacity','1');ln.setAttribute('stroke-width','1.5');}
          else{ln.setAttribute('opacity','.12');ln.setAttribute('stroke-width','.8');}
        });
      }
    }

    function hideTip(){
      tip.style.display='none';
      conn.setAttribute('stroke','transparent');conn.setAttribute('opacity','0');conn.classList.remove('rdr-conn-anim');
      S.forEach(function(s){
        var ln=axEls[s.id].querySelector('line');
        ln.setAttribute('opacity','.6');ln.setAttribute('stroke-width','.8');
      });
    }

    dots.forEach(function(d){
      d.el.addEventListener('mouseenter',function(){showTip(d);});
      d.el.addEventListener('mouseleave',hideTip);
      d.el.addEventListener('click',function(){
 /* ripple effect */
        var rip=el('g',{class:'rdr-ripple'});
        rip.appendChild(el('circle',{cx:d.pos.x.toFixed(1),cy:d.pos.y.toFixed(1),r:'9',fill:'none',stroke:d.c,'stroke-width':'2'}));
        svg.appendChild(rip);
        setTimeout(function(){if(rip.parentNode)rip.parentNode.removeChild(rip);},650);
        if(d.p.lk){window.location.href=d.p.lk;}
        else{
          var sc=stC(d.p.st);
          mBody.innerHTML='<div style="display:flex;align-items:center;gap:.5rem;margin-bottom:.5rem">'+
            '<div style="width:10px;height:10px;border-radius:50%;background:'+d.c+'"></div>'+
            '<span style="font-size:1.05rem;font-weight:700;color:#1e293b">'+d.p.l+'</span></div>'+
            '<div style="color:#64748b;font-size:.83rem;margin-bottom:.5rem">'+d.p.v+' \u00b7 '+d.p.y+
            ' <span style="display:inline-block;padding:1px 7px;border-radius:10px;font-size:.7rem;font-weight:600;background:'+sc+'18;color:'+sc+';margin-left:3px">'+d.p.st+'</span></div>'+
            '<p style="color:#475569;font-size:.88rem;line-height:1.6;margin:0">'+d.p.d+'</p>';
          modal.style.display='flex';
        }
      });
      d.el.addEventListener('touchstart',function(e){e.preventDefault();showTip(d);},{passive:false});
    });

 /* tap background to dismiss on mobile */
    svg.addEventListener('touchstart',function(e){
      if(!e.target.closest('.rdr-dot,.rdr-lbl,.rdr-axis'))resetHi();
    });

    /* ---- modal ---- */
    document.getElementById('rdr-modal-x').addEventListener('click',function(){modal.style.display='none';});
    modal.addEventListener('click',function(e){if(e.target===modal)modal.style.display='none';});

    /* ---- filters ---- */
    var fbs=document.querySelectorAll('.rdr-fb');
    fbs.forEach(function(btn){
      btn.addEventListener('click',function(){
        fbs.forEach(function(b){b.classList.remove('rdr-fb--on');});
        btn.classList.add('rdr-fb--on');
        var f=btn.getAttribute('data-filter');
        dots.forEach(function(d){d.el.classList.toggle('off',f!=='all'&&d.p.t!==f);});
      });
    });

    /* ---- drag to rotate (optional) ---- */
    var rot=0,dragging=false,dragA=0;
    svg.addEventListener('mousedown',function(e){
      if(e.target.closest('.rdr-dot,.rdr-lbl,.rdr-axis'))return;
      dragging=true;
      var rect=svg.getBoundingClientRect();
      var mx=(e.clientX-rect.left)*(900/rect.width),my=(e.clientY-rect.top)*(760/rect.height);
      dragA=Math.atan2(my-CY,mx-CX)/RAD-rot;
      svg.style.cursor='grabbing';
    });
    window.addEventListener('mousemove',function(e){
      if(!dragging)return;
      var rect=svg.getBoundingClientRect();
      var mx=(e.clientX-rect.left)*(900/rect.width),my=(e.clientY-rect.top)*(760/rect.height);
      rot=Math.atan2(my-CY,mx-CX)/RAD-dragA;
      applyRot();
    });
    window.addEventListener('mouseup',function(){if(dragging){dragging=false;svg.style.cursor='';}});

    function applyRot(){
      var tr='rotate('+rot.toFixed(1)+' '+CX+' '+CY+')';
      ringEls.forEach(function(r){r.querySelector('circle').setAttribute('transform',tr);});
      S.forEach(function(s){
        axEls[s.id].querySelector('line').setAttribute('transform',tr);
        sectors[s.id].setAttribute('transform',tr);
      });
      conn.setAttribute('transform',tr);
 /* recalculate dot positions */
      dots.forEach(function(d){
        var origA=d.p.cs?d.p.a:sMap[d.p.s].a;
        var newA=origA+rot;
        var np=pol(newA,d.p.r);
        d.pos={x:np.x,y:np.y};
        var circles=d.el.querySelectorAll('circle');
        circles[0].setAttribute('cx',np.x.toFixed(1));circles[0].setAttribute('cy',np.y.toFixed(1));
        circles[1].setAttribute('cx',np.x.toFixed(1));circles[1].setAttribute('cy',np.y.toFixed(1));
      });
 /* labels are fixed cards; they do not rotate */
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

<!-- ========== RESEARCH TRAINING ========== -->
<section id="research-training" style="margin:1.6rem 0 2.2rem">
  <h2>Research Training</h2>
  <div style="padding:1.3rem 1.4rem;border-radius:14px;background:#fff;border:1px solid #eee9f3;box-shadow:0 4px 20px rgba(124,58,237,.08)">
    <p class="pub-item__t" style="margin:0">Modern Meta-Analysis Research Institute (MMARI) <span class="pub-badge" style="background:#ede9fe;color:#7c3aed">NSF-funded</span></p>
    <p class="pub-item__m" style="margin-top:4px">Chicago, IL &middot; July 2026</p>
    <p style="font-size:.85rem;color:#4a5568;line-height:1.7;margin:.7rem 0 0">Selected participant in an NSF-funded training institute on modern meta-analysis. The program covered effect-size computation and synthesis workflows in R/RStudio and Open Science practices for transparent, reproducible evidence synthesis. This training directly supports my evidence-synthesis research line, including <a href="#under-review">a meta-analysis currently under review</a>.</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:.9rem">
      <img src="/images/mmari/1.jpg" alt="MMARI 2026 cohort, Chicago" style="grid-column:1/-1;width:100%;height:240px;object-fit:cover;border-radius:10px;border:1px solid #eee9f3" onerror="this.style.display='none'">
      <img src="/images/mmari/2.jpg" alt="MMARI 2026, Chicago" style="width:100%;height:170px;object-fit:cover;border-radius:10px;border:1px solid #eee9f3" onerror="this.style.display='none'">
      <img src="/images/mmari/3.jpg" alt="MMARI 2026, Chicago" style="width:100%;height:170px;object-fit:cover;border-radius:10px;border:1px solid #eee9f3" onerror="this.style.display='none'">
      <img src="/images/mmari/4.jpg" alt="MMARI 2026, Chicago" style="width:100%;height:170px;object-fit:cover;border-radius:10px;border:1px solid #eee9f3" onerror="this.style.display='none'">
      <img src="/images/mmari/5.jpg" alt="MMARI 2026 working session, Chicago" style="width:100%;height:170px;object-fit:cover;border-radius:10px;border:1px solid #eee9f3" onerror="this.style.display='none'">
    </div>
  </div>
</section>

<h2>Journal Articles &amp; Book Chapters</h2>

<p class="stats">
  <a href="{{ site.author.googlescholar }}">Google Scholar</a> &middot; Citation: {{ site.data.scholar.citations_all }} &middot; h-index: {{ site.data.scholar.h_index_all }}
</p>

<div class="pub-yr"><h3>2026</h3><div>

<a class="pub-item" href="/publication/answer-bot-to-tutor">
  <img class="pub-item__th" src="/images/pubs/answer-bot-to-tutor.png" alt="PeteChat design story">
  <div class="pub-item__bd">
    <p class="pub-item__t">From Answer Bot to Course Tutor: A Practical Design Case of a Guardrailed AI Assistant in Higher Education <span class="pub-badge pub-badge--upcoming">In Press</span> <span class="pub-badge pub-badge--web">arXiv</span></p>
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

<h2 id="under-review">Under Review</h2>


<div class="pub-item">
  <div class="pub-item__icon">&#128202;</div>
  <div class="pub-item__bd">
    <p class="pub-item__t">A Meta-analysis on the Achievement of Technology on Students from Low-income Families <span class="pub-badge pub-badge--ur">Under Review</span></p>
    <p class="pub-item__m"><strong>*Tan, L.</strong>, Wang, C., Li, B., Lowell, V., &amp; Fei, X.</p>
  </div>
</div>

<div class="pub-item">
  <img class="pub-item__th" src="/images/pubs/tpack-model.png" alt="TPACK framework">
  <div class="pub-item__bd">
    <p class="pub-item__t">How Ethnic and Cultural Context Shapes Technology Integration Knowledge Among Trainee Teachers in Western China <span class="pub-badge pub-badge--ur">Under Review</span></p>
    <p class="pub-item__m">Liu, H. &amp; <strong>*Tan, L.</strong></p>
  </div>
</div>

<div class="pub-item">
  <img class="pub-item__th" src="/images/pubs/authorship-ai-loop.png" alt="AI authenticity loop">
  <div class="pub-item__bd">
    <p class="pub-item__t">Whose Words Are These? University Faculty Perspectives on Originality and AI-Mediated Composition <span class="pub-badge pub-badge--ur">Under Review</span></p>
    <p class="pub-item__m">Li, B. &amp; <strong>*Tan, L.</strong></p>
  </div>
</div>

<h2>Conference Presentations &amp; Invited Talks</h2>

<div class="conf-item">
  <span class="conf-item__y">2026</span>
  <div class="conf-item__bd">
    <p class="conf-item__t"><span class="pub-badge pub-badge--conf">Conf</span> A Meta-analysis on the Achievement of Technology on Students from Low-income Families <span class="pub-badge pub-badge--upcoming">Upcoming</span></p>
    <p class="conf-item__m"><strong>*Tan, L.</strong>, Lowell, V. &amp; Li, B. &middot; AERA International Convention, Los Angeles, CA</p>
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

</div>