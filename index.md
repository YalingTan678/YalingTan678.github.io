---
layout: home
author_profile: false
---

<!-- ========== RESEARCH STRANDS RADAR ========== -->
<section class="lt-section lt-fade-in" style="padding-top:0">
  <h2 class="lt-section__title">Research Strands</h2>
  <p style="font-size:0.92rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">My work moves across four interconnected strands. Hover over each area to see how they relate:</p>

  <div style="display:flex;justify-content:center;gap:0.4rem;margin-bottom:1.2rem;flex-wrap:wrap">
    <button class="rdr-fb rdr-fb--on" data-filter="all">All</button>
    <button class="rdr-fb" data-filter="publication">Publications</button>
    <button class="rdr-fb" data-filter="talk">Talks</button>
    <button class="rdr-fb" data-filter="progress">In Progress</button>
  </div>

  <div id="rdr-wrap" style="position:relative;max-width:860px;margin:0 auto;-webkit-user-select:none;user-select:none">
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
      {id:'literacy',lbl:['AI Literacy &','Learning Design'],sub:'Design principles & environments',c:'#0D9488',a:270,lx:450,ly:65,an:'middle'},
      {id:'tpack',lbl:['TPACK &','Teacher Ed'],sub:'Technology integration & diversity',c:'#7C3AED',a:0,lx:740,ly:370,an:'start'},
      {id:'equity',lbl:['Equity &','Assessment'],sub:'Authenticity & evaluative judgment',c:'#EA580C',a:90,lx:450,ly:695,an:'middle'},
      {id:'idle',lbl:['IDLE &','Pragmatics'],sub:'AI chatbots & self-directed learning',c:'#0369A1',a:180,lx:160,ly:370,an:'end'}
    ];
    var sMap={};S.forEach(function(s){sMap[s.id]=s;});

    var P=[
      {id:'genai',l:'GenAI Review \u00b7 CAEAI \'25',s:'literacy',a:255,r:155,t:'publication',v:'CAEAI (Q1)',y:2025,st:'Published',lk:'/publication/2025-two-years-innovation',d:'Two years of innovation: systematic review of empirical GenAI research in language learning and teaching.'},
      {id:'pete',l:'PeteChat Design Case',s:'literacy',a:285,r:215,t:'progress',v:'Under Review',y:2026,st:'Revising',lk:'/publication/ur-tutor-not-solver',d:'Tutor, not solver: designing a guardrailed AI assistant for learning in higher education.'},
      {id:'claw',l:'Clawdbot \u00b7 Talk \'26',s:'literacy',r:95,t:'talk',v:'AI Lunch & Learn',y:2026,st:'Presented',lk:'/publication/2026-clawdbot-unboxed',d:'Clawdbot Unboxed: What It Does, Why It\'s Hot, and Where It Breaks.'},
      {id:'tpxj',l:'TPACK Xinjiang Study',s:'tpack',a:15,r:160,t:'progress',v:'Asia-Pacific Ed. Researcher',y:2026,st:'In Review',lk:'/publication/ur-tpack-xinjiang',d:'Pre-service teachers\' TPACK in Xinjiang: examining culture diversity as context.'},
      {id:'clil',l:'CLIL \u00b7 Ed. Adv. \'23',s:'tpack',a:345,r:100,t:'publication',v:'Education Advances',y:2023,st:'Published',lk:'/publication/2023-clil-translation',d:'Study on MTI talent cultivation mode from the perspective of CLIL.'},
      {id:'idle-gai',l:'IDLE & GAI \u00b7 Talk \'25',cs:['idle','equity'],a:160,r:165,t:'talk',v:'Purdue AI in P-12',y:2025,st:'Presented',lk:null,d:'Assessing effects of extramural GAI-mediated IDLE on pragmatic and communicative competence of Chinese undergraduates.'},
      {id:'mjss',l:'Interpreting \u00b7 MJSS \'25',cs:['idle','literacy'],a:210,r:135,t:'publication',v:'MJSS',y:2025,st:'Published',lk:null,d:'Pointing to context from a relevance theory perspective: a comparative study of human and machine interpreting.'},
      {id:'doubao',l:'Doubao \u00b7 PE (Q2) \'26',s:'equity',a:100,r:145,t:'publication',v:'Psicologia Educativa',y:2026,st:'Published',lk:'/publication/2026-doubao-genai-efl',d:'Doubao as a GenAI scaffold in senior high school EFL writing.'},
      {id:'aera',l:'AERA Meta \u00b7 \'26',s:'equity',a:70,r:90,t:'talk',v:'AERA Convention',y:2026,st:'Upcoming',lk:null,d:'Meta-analysis on the achievement of technology on students from low-income families.'},
      {id:'auth',l:'Authorship & AI',cs:['literacy','equity'],a:132,r:210,t:'progress',v:'Education Science',y:2026,st:'In Review',lk:null,d:'How higher education instructors navigate authenticity in student writing in an age of generative AI.'}
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
    // defs (shadow filter)
    var defs=el('defs',{});
    var filt=el('filter',{id:'rdr-shd',x:'-30%',y:'-30%',width:'160%',height:'160%'});
    filt.appendChild(el('feGaussianBlur',{in:'SourceAlpha',stdDeviation:'3',result:'b'}));
    filt.appendChild(el('feOffset',{dy:'2',result:'o'}));
    filt.appendChild(el('feFlood',{'flood-opacity':'0.1',result:'c'}));
    filt.appendChild(el('feComposite',{in:'c',in2:'o',operator:'in',result:'s'}));
    var mg=el('feMerge',{});mg.appendChild(el('feMergeNode',{in:'s'}));mg.appendChild(el('feMergeNode',{in:'SourceGraphic'}));
    filt.appendChild(mg);defs.appendChild(filt);

    // radial gradients for strand ellipses
    var gradData=[
      {id:'grad-lit',cx:'50%',cy:'35%',stops:[['0%','#5eead4',0.75],['45%','#2dd4bf',0.45],['100%','#0D9488',0.12]]},
      {id:'grad-tpack',cx:'35%',cy:'50%',stops:[['0%','#c4b5fd',0.75],['45%','#8b5cf6',0.45],['100%','#7C3AED',0.12]]},
      {id:'grad-eq',cx:'50%',cy:'35%',stops:[['0%','#fdba74',0.75],['45%','#f97316',0.45],['100%','#EA580C',0.12]]},
      {id:'grad-idle',cx:'65%',cy:'50%',stops:[['0%','#7dd3fc',0.75],['45%','#0ea5e9',0.45],['100%','#0369A1',0.12]]}
    ];
    gradData.forEach(function(gd){
      var rg=el('radialGradient',{id:gd.id,cx:gd.cx,cy:gd.cy,r:'70%'});
      gd.stops.forEach(function(s){rg.appendChild(el('stop',{offset:s[0],'stop-color':s[1],'stop-opacity':s[2]}));});
      defs.appendChild(rg);
    });
    // outer glow gradient
    var outerGrad=el('radialGradient',{id:'grad-outer',cx:'50%',cy:'50%',r:'50%'});
    outerGrad.appendChild(el('stop',{offset:'0%','stop-color':'#f0f4ff','stop-opacity':'0.5'}));
    outerGrad.appendChild(el('stop',{offset:'70%','stop-color':'#e8ecf4','stop-opacity':'0.25'}));
    outerGrad.appendChild(el('stop',{offset:'100%','stop-color':'#dde3ee','stop-opacity':'0.08'}));
    defs.appendChild(outerGrad);
    svg.appendChild(defs);

    // large background circle (slow rotation)
    var outerCircle=el('circle',{cx:CX,cy:CY,r:RINGS[2]+40,fill:'url(#grad-outer)',stroke:'#e2e8f0','stroke-width':'.5','stroke-dasharray':'8 5',opacity:'.6',class:'rdr-outer'});
    svg.appendChild(outerCircle);

    // four gradient ellipses behind each strand
    var ellipseData=[
      {grad:'grad-lit',cx:CX,cy:CY-120,rx:240,ry:250},       // literacy (up)
      {grad:'grad-tpack',cx:CX+140,cy:CY,rx:260,ry:210},     // tpack (right)
      {grad:'grad-eq',cx:CX,cy:CY+120,rx:240,ry:250},        // equity (down)
      {grad:'grad-idle',cx:CX-140,cy:CY,rx:260,ry:210}       // idle (left)
    ];
    var strandEllipses={};
    var sIds=['literacy','tpack','equity','idle'];
    ellipseData.forEach(function(ed,i){
      var ell=el('ellipse',{cx:ed.cx,cy:ed.cy,rx:ed.rx,ry:ed.ry,fill:'url(#'+ed.grad+')',opacity:'0',class:'rdr-ellipse-breathe',style:'pointer-events:none;transition:opacity .4s ease;--base-op:.75'});
      svg.appendChild(ell);
      strandEllipses[sIds[i]]=ell;
    });

    // sectors (highlight on strand hover)
    var sectors={};
    S.forEach(function(s){
      var p=el('path',{d:secP(s.a-45,s.a+45,RINGS[2]),fill:s.c,opacity:'0',class:'rdr-sector','data-s':s.id});
      svg.appendChild(p);sectors[s.id]=p;
    });

    // concentric rings
    var ringEls=[];
    RINGS.forEach(function(r){
      var g=el('g',{class:'rdr-ring',style:'opacity:0;transform:scale(0)'});
      g.appendChild(el('circle',{cx:CX,cy:CY,r:r,fill:'none',stroke:'#d1d5db','stroke-width':'1','stroke-dasharray':'6 4',opacity:'.45'}));
      svg.appendChild(g);ringEls.push(g);
    });

    // axes
    var axEls={};
    S.forEach(function(s){
      var end=pol(s.a,ALEN);
      var g=el('g',{class:'rdr-axis','data-s':s.id,style:'opacity:0'});
      g.appendChild(el('line',{x1:CX,y1:CY,x2:end.x.toFixed(1),y2:end.y.toFixed(1),stroke:'#cbd5e1','stroke-width':'.8',opacity:'.6'}));
      svg.appendChild(g);axEls[s.id]=g;
    });

    // center badge
    var badge=el('g',{style:'opacity:0'});
    badge.appendChild(el('circle',{cx:CX,cy:CY,r:38,fill:'#fff',stroke:'#e2e8f0','stroke-width':'1.5',filter:'url(#rdr-shd)'}));
    var ct1=el('text',{x:CX,y:CY-6,'text-anchor':'middle','font-size':'12','font-weight':'700',fill:'#1e1b4b',opacity:'.8'});
    ct1.textContent='AI \u00d7 Education';
    var ct2=el('text',{x:CX,y:CY+10,'text-anchor':'middle','font-size':'9',fill:'#64748b',opacity:'.6'});
    ct2.textContent='Shared foundation';
    badge.appendChild(ct1);badge.appendChild(ct2);svg.appendChild(badge);

    // connection line (dot-to-center on hover)
    var conn=el('line',{x1:CX,y1:CY,x2:CX,y2:CY,stroke:'transparent','stroke-width':'1.5','stroke-dasharray':'4 3',class:'rdr-conn',opacity:'0'});
    svg.appendChild(conn);

    // strand labels
    var lblEls={};
    S.forEach(function(s){
      var g=el('g',{class:'rdr-lbl','data-s':s.id,style:'opacity:0'});
      // invisible hit area for easier hover/click
      var hitW=200,hitH=75;
      var hitX=s.an==='middle'?s.lx-hitW/2:s.an==='start'?s.lx-10:s.lx-hitW+10;
      var hitY=s.ly-18;
      g.appendChild(el('rect',{x:hitX,y:hitY,width:hitW,height:hitH,fill:'transparent',style:'cursor:pointer'}));
      s.lbl.forEach(function(line,j){
        var t=el('text',{x:s.lx,y:s.ly+j*22,'text-anchor':s.an,'font-size':'17','font-weight':'800',fill:s.c});
        t.textContent=line;g.appendChild(t);
      });
      var sub=el('text',{x:s.lx,y:s.ly+s.lbl.length*22+2,'text-anchor':s.an,'font-size':'10',fill:s.c,opacity:'.55','font-style':'italic'});
      sub.textContent=s.sub;g.appendChild(sub);
      svg.appendChild(g);lblEls[s.id]=g;
    });

    // paper dots
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

    // web lines connecting dots
    var webLinks=[
      ['claw','genai'],['genai','pete'],           // literacy chain
      ['pete','auth'],['auth','doubao'],            // literacy → cross → equity
      ['mjss','idle-gai'],['idle-gai','auth'],      // idle → cross
      ['doubao','aera'],['clil','tpxj'],            // equity → tpack
      ['mjss','doubao'],['auth','tpxj']             // cross connections
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
      // ellipses bloom in first
      sIds.forEach(function(id,i){
        setTimeout(function(){strandEllipses[id].style.transition='opacity .8s ease';strandEllipses[id].style.opacity='.75';},i*120);
      });
      // then rings expand
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
      // web lines fade in after dots
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
      var ownIdx=0;
      dots.forEach(function(d){
        var own=(d.p.s===sid)||(d.p.cs&&d.p.cs.indexOf(sid)!==-1);
        d.el.classList.toggle('dim',!own);
        if(own){
          // alternate left/right to avoid overlap on same axis
          var lx,la;
          var dx=d.pos.x-CX,dy=d.pos.y-CY;
          if(Math.abs(dx)<60){
            // vertical axis — alternate sides
            if(ownIdx%2===0){lx=d.pos.x+16;la='start';}else{lx=d.pos.x-16;la='end';}
          }else if(dx<0){lx=d.pos.x-16;la='end';}
          else{lx=d.pos.x+16;la='start';}
          // background rect for readability
          var bg=el('rect',{x:la==='start'?lx-2:lx-160,y:d.pos.y-18,width:162,height:32,rx:4,fill:'#fff',opacity:'.85',class:'rdr-mini'});
          svg.appendChild(bg);miniEls.push(bg);
          var t=el('text',{x:lx,y:d.pos.y-5,'text-anchor':la,'font-size':'12','font-weight':'700',fill:d.c,class:'rdr-mini rdr-mini-anim'});
          t.textContent=d.p.l;svg.appendChild(t);miniEls.push(t);
          var t2=el('text',{x:lx,y:d.pos.y+10,'text-anchor':la,'font-size':'9.5',fill:'#64748b',class:'rdr-mini rdr-mini-anim',style:'animation-delay:.08s'});
          t2.textContent=d.p.v+' \u00b7 '+d.p.y;svg.appendChild(t2);miniEls.push(t2);
          ownIdx++;
        }
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
        // ripple effect
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

    // tap background to dismiss on mobile
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
      // recalculate dot positions
      dots.forEach(function(d){
        var origA=d.p.cs?d.p.a:sMap[d.p.s].a;
        var newA=origA+rot;
        var np=pol(newA,d.p.r);
        d.pos={x:np.x,y:np.y};
        var circles=d.el.querySelectorAll('circle');
        circles[0].setAttribute('cx',np.x.toFixed(1));circles[0].setAttribute('cy',np.y.toFixed(1));
        circles[1].setAttribute('cx',np.x.toFixed(1));circles[1].setAttribute('cy',np.y.toFixed(1));
      });
      // move labels
      S.forEach(function(s){
        var newA=s.a+rot;
        var lp=pol(newA,ALEN+50);
        var g=lblEls[s.id];
        var texts=g.querySelectorAll('text');
        var an=lp.x>CX+30?'start':lp.x<CX-30?'end':'middle';
        for(var i=0;i<texts.length;i++){
          texts[i].setAttribute('x',lp.x.toFixed(1));
          texts[i].setAttribute('y',(lp.y-20+i*((i<s.lbl.length)?22:24)).toFixed(1));
          texts[i].setAttribute('text-anchor',an);
        }
      });
    }
  })();
  </script>
</section>

<!-- ========== METHODOLOGY (interactive pipeline) ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Methodology</h2>
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
      <div class="meth-counter" style="color:#0D9488"><span class="meth-cnt" data-target="144">0</span></div>
      <div class="meth-counter-label">Articles Screened</div>
      <div class="meth-detail">Synthesizing evidence across 144 articles to identify research gaps and emerging patterns in AI-assisted learning.</div>
      <div class="meth-dot" style="background:#0D9488"></div>
    </div>
    <!-- Card 2 -->
    <div class="meth-card">
      <div class="meth-num" style="color:#7C3AED">02</div>
      <div class="meth-title" style="color:#7C3AED">Mixed Methods</div>
      <div class="meth-sub">Quan + Qual<br>Surveys · Interviews</div>
      <div class="meth-counter" style="color:#7C3AED">Convergent</div>
      <div class="meth-counter-label">Design Approach</div>
      <div class="meth-detail">Triangulating survey data with interview insights using convergent mixed-methods design for richer, validated findings.</div>
      <div class="meth-dot" style="background:#7C3AED"></div>
    </div>
    <!-- Card 3 -->
    <div class="meth-card">
      <div class="meth-num" style="color:#0369A1">03</div>
      <div class="meth-title" style="color:#0369A1">Statistical Analysis</div>
      <div class="meth-sub">SPSS · Prism<br>ANOVA · Coh-Metrix</div>
      <div class="meth-counter" style="color:#0369A1"><span class="meth-cnt" data-target="108">0</span></div>
      <div class="meth-counter-label">Indices Tested</div>
      <div class="meth-detail">Rigorous quantitative analysis using 108 linguistic and performance indices across multiple datasets.</div>
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

<!-- ========== JOURNEY (Swimlane + Compact) ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Journey</h2>
  <p style="font-size:0.88rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">From translation studies to AI-mediated learning design, every step has brought me closer to one goal: becoming an instructional designer who harnesses AI to create equitable, human-centered learning experiences at scale.</p>
  <style>
    .jny-filters{display:flex;gap:.4rem;margin-bottom:1rem;flex-wrap:wrap}
    .jny-fbtn{border:none;padding:.3rem .7rem;border-radius:6px;font-size:.7rem;font-weight:600;cursor:pointer;transition:all .2s}
    .jny-fbtn.active{color:#fff!important;background:#1a1a2e!important}
    .jny-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
    .jny-table{width:100%;min-width:560px;border-collapse:collapse}
    .jny-table th{font-size:.7rem;font-weight:700;padding:.6rem .4rem;text-align:center;border-bottom:2px solid #e2e8f0;color:#94a3b8;position:sticky;top:0;background:#fff;z-index:2}
    .jny-table th.jny-now{color:#5b21b6;position:relative}
    .jny-table th.jny-now::after{content:'';position:absolute;bottom:-2px;left:20%;right:20%;height:3px;background:#8b5cf6;border-radius:2px}
    .jny-table td{padding:.4rem .3rem;vertical-align:middle;border-bottom:1px solid #f1f5f9;transition:background .3s}
    .jny-table tr:hover td{background:rgba(0,0,0,.015)}
    .jny-table tr.jny-dimmed td{opacity:.12;transition:opacity .4s}
    .jny-cat{font-size:.7rem;font-weight:700;white-space:nowrap;padding-right:.6rem}
    .jny-cat-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:middle}
    .jny-tipwrap{position:relative;display:inline-block}
    .jny-chip{display:inline-block;border-radius:8px;padding:.4rem .6rem;font-size:.7rem;font-weight:600;color:#1a1a2e;line-height:1.3;cursor:default;transition:transform .25s,box-shadow .25s;margin:2px 0;text-decoration:none}
    .jny-chip:hover{transform:translateY(-2px);box-shadow:0 4px 14px rgba(0,0,0,.08)}
    .jny-chip small{display:block;font-size:.58rem;font-weight:400;color:#94a3b8;margin-top:.1rem}
    .jny-chip.highlight{border-width:2px;font-size:.72rem}
    .jny-chip.upcoming{border-style:dashed}
    .jny-tag{display:inline-block;font-size:.5rem;font-weight:700;padding:.1rem .35rem;border-radius:4px;margin-left:.3rem;vertical-align:middle;letter-spacing:.03em}
    .jny-tip{position:absolute;bottom:calc(100% + 8px);left:50%;transform:translateX(-50%) scale(.9);opacity:0;pointer-events:none;background:#fff;color:#475569;font-size:.62rem;line-height:1.5;padding:.55rem .75rem;border-radius:10px;white-space:nowrap;z-index:20;transition:opacity .25s,transform .25s;box-shadow:0 4px 20px rgba(0,0,0,.12);border:1px solid #e2e8f0}
    .jny-tip::after{content:'';position:absolute;top:100%;left:50%;transform:translateX(-50%);border:5px solid transparent;border-top-color:#fff}
    .jny-tip strong{color:#1a1a2e}
    .jny-tipwrap:hover .jny-tip{opacity:1;transform:translateX(-50%) scale(1)}
  </style>
  <!-- Filter buttons -->
  <div class="jny-filters">
    <button class="jny-fbtn active" onclick="jnyFilter('all',this)">All</button>
    <button class="jny-fbtn" style="background:#f5f3ff;color:#8b5cf6" onclick="jnyFilter('edu',this)">Education</button>
    <button class="jny-fbtn" style="background:#eff6ff;color:#3b82f6" onclick="jnyFilter('pub',this)">Publications</button>
    <button class="jny-fbtn" style="background:#fffbeb;color:#d97706" onclick="jnyFilter('talk',this)">Talks</button>
    <button class="jny-fbtn" style="background:#f0fdfa;color:#14b8a6" onclick="jnyFilter('work',this)">Experience</button>
    <button class="jny-fbtn" style="background:#fdf2f8;color:#ec4899" onclick="jnyFilter('award',this)">Awards</button>
  </div>
  <div class="jny-wrap">
    <table class="jny-table">
      <thead><tr><th></th><th>2022</th><th>2023</th><th>2024</th><th class="jny-now">2025</th><th>2026</th></tr></thead>
      <tbody>
        <tr data-cat="edu">
          <td class="jny-cat" style="color:#8b5cf6"><span class="jny-cat-dot" style="background:#8b5cf6"></span>Education</td>
          <td><span class="jny-tipwrap"><span class="jny-chip" style="background:#f5f3ff;border:1px solid #ddd6fe">B.A. Translation<small>SWUST, China</small></span><span class="jny-tip"><strong>B.A. in Translation</strong><br>Southwest University of Science &amp; Technology<br>Mianyang, China</span></span></td>
          <td></td>
          <td><span class="jny-tipwrap"><span class="jny-chip" style="background:#f5f3ff;border:1px solid #ddd6fe">M.A. Dual Degree<small>NEU + Silesia</small></span><span class="jny-tip"><strong>M.A. Interpreting</strong> (Northeastern U., China)<br><strong>M.A. Philology</strong> (U. of Silesia, Poland)<br>Erasmus+ Double-Degree Program</span></span></td>
          <td><span class="jny-tipwrap"><span class="jny-chip highlight" style="background:linear-gradient(135deg,#f5f3ff,#ede9fe);border:2px solid #a78bfa;color:#5b21b6">Ph.D. Purdue<small style="color:#7c3aed">Learning Design &amp; Tech</small></span><span class="jny-tip"><strong>Doctor of Philosophy</strong><br>Learning Design and Technology<br>Advisor: Dr. Victoria Lowell</span></span></td>
          <td></td>
        </tr>
        <tr data-cat="pub">
          <td class="jny-cat" style="color:#3b82f6"><span class="jny-cat-dot" style="background:#3b82f6"></span>Publications</td>
          <td></td>
          <td><span class="jny-tipwrap"><a href="/publication/2023-clil-translation" class="jny-chip" style="background:#eff6ff;border:1px solid #bfdbfe">CLIL<small>Ed. Advances</small></a><span class="jny-tip"><strong>Gao &amp; Tan (2023)</strong><br>MTI talent cultivation from CLIL perspective<br>Education Advances, 13(12)</span></span></td>
          <td></td>
          <td><span class="jny-tipwrap"><a href="/publication/2025-two-years-innovation" class="jny-chip" style="background:#eff6ff;border:1px solid #bfdbfe">CAEAI<span class="jny-tag" style="background:#dcfce7;color:#16a34a">Q1</span><small>IF ≈ 10.5</small></a><span class="jny-tip"><strong>Li, Tan, Wang &amp; Lowell (2025)</strong><br>Systematic review of empirical GenAI research<br>Computers &amp; Education: AI, 9, 100445</span></span> <span class="jny-tipwrap"><span class="jny-chip" style="background:#eff6ff;border:1px solid #bfdbfe">MJSS<small>Tan &amp; Gao</small></span><span class="jny-tip"><strong>Tan &amp; Gao (2025)</strong><br>Human vs. machine interpreting<br>Mediterranean J. of Social Sciences, 16(3)</span></span></td>
          <td><span class="jny-tipwrap"><a href="/publication/2026-doubao-genai-efl" class="jny-chip" style="background:#eff6ff;border:1px solid #bfdbfe">Doubao<span class="jny-tag" style="background:#dbeafe;color:#2563eb">Q2</span><small>Wang &amp; Tan</small></a><span class="jny-tip"><strong>Wang &amp; Tan (2026)</strong><br>GenAI scaffold in EFL writing<br>Psicologia Educativa, 14, 19-33</span></span></td>
        </tr>
        <tr data-cat="talk">
          <td class="jny-cat" style="color:#f59e0b"><span class="jny-cat-dot" style="background:#f59e0b"></span>Talks</td>
          <td></td><td></td>
          <td><span class="jny-tipwrap"><a href="/publication/2024-call-context" class="jny-chip" style="background:#fffbeb;border:1px solid #fde68a">CALL Tokyo<small>Interpreting</small></a><span class="jny-tip"><strong>XXIInd Int'l CALL Conference</strong><br>Human vs. machine interpreting<br>Tokyo, Japan · Sep 2024</span></span> <span class="jny-tipwrap"><span class="jny-chip" style="background:#fffbeb;border:1px solid #fde68a">SCT + IPC<small>2 conferences</small></span><span class="jny-tip"><strong>3rd SCT Conference</strong>, Guangdong<br><strong>10th IPC Conference</strong>, Pisa<br>May–Jun 2024</span></span></td>
          <td><span class="jny-tipwrap"><a href="/publication/2025-aect-authenticity" class="jny-chip" style="background:#fffbeb;border:1px solid #fde68a">AECT + P-12<small>Las Vegas + Purdue</small></a><span class="jny-tip"><strong>AECT Convention</strong>, Las Vegas<br><strong>Purdue AI in P-12</strong> Conference<br>Oct–Nov 2025</span></span></td>
          <td><span class="jny-tipwrap"><a href="/publication/2026-clawdbot-unboxed" class="jny-chip" style="background:#fffbeb;border:1px solid #fde68a">Clawdbot<small>AI Lunch &amp; Learn</small></a><span class="jny-tip"><strong>Clawdbot Unboxed</strong><br>AI Lunch &amp; Learn Series<br>Purdue CoE · Feb 2026</span></span> <span class="jny-tipwrap"><span class="jny-chip upcoming" style="background:linear-gradient(135deg,#fffbeb,#fef3c7);border:2px dashed #fbbf24">AERA<span class="jny-tag" style="background:#fef3c7;color:#d97706">Upcoming</span><small>Los Angeles</small></span><span class="jny-tip"><strong>AERA 2026 Convention</strong><br>Meta-analysis on technology &amp; low-income families<br>Los Angeles, CA · Apr 2026</span></span></td>
        </tr>
        <tr data-cat="work">
          <td class="jny-cat" style="color:#14b8a6"><span class="jny-cat-dot" style="background:#14b8a6"></span>Experience</td>
          <td></td><td></td>
          <td><span class="jny-tipwrap"><span class="jny-chip" style="background:#f0fdfa;border:1px solid #99f6e4">U. of Silesia<small>Lecturer · 200+</small></span><span class="jny-tip"><strong>Lecturer</strong>, Institute of Linguistics<br>Spoken Chinese &amp; Academic Writing<br>200+ international students · 2023–2024</span></span></td>
          <td><span class="jny-tipwrap"><a href="/service/" class="jny-chip" style="background:#f0fdfa;border:1px solid #99f6e4">RA + PALDT + GESC<small>Purdue University</small></a><span class="jny-tip"><strong>Research Assistant</strong>, Purdue Library &amp; SIS<br><strong>PALDT</strong> Marketing &amp; Design Officer<br><strong>GESC</strong> Committee Member</span></span></td>
          <td><span class="jny-tipwrap"><span class="jny-chip" style="background:#f0fdfa;border:1px solid #99f6e4">Guest Lecturer<small>EDCI 612</small></span><span class="jny-tip"><strong>Guest Lecturer</strong>, EDCI 612<br>AI and Multilingual Learners<br>Co-presented with Dr. Lowell &amp; Belle Li</span></span></td>
        </tr>
        <tr data-cat="award">
          <td class="jny-cat" style="color:#ec4899"><span class="jny-cat-dot" style="background:#ec4899"></span>Awards</td>
          <td></td><td></td>
          <td><span class="jny-tipwrap"><span class="jny-chip" style="background:#fdf2f8;border:1px solid #fbcfe8">Fellowship + Erasmus+<small>$2K + $5K</small></span><span class="jny-tip"><strong>National Academic Fellowship</strong> $2K<br>Northeastern University<br><strong>Erasmus+ Fund</strong> $5K · U. of Silesia</span></span></td>
          <td><span class="jny-tipwrap"><span class="jny-chip" style="background:#fdf2f8;border:1px solid #fbcfe8">LDT Travel<small>$250</small></span><span class="jny-tip"><strong>LDT Travel Support Program</strong><br>Curriculum &amp; Instruction<br>Purdue University</span></span></td>
          <td></td>
        </tr>
      </tbody>
    </table>
  </div>
  <script>
  function jnyFilter(cat,btn){
    document.querySelectorAll('.jny-fbtn').forEach(function(b){b.classList.remove('active');});
    btn.classList.add('active');
    document.querySelectorAll('.jny-table tr[data-cat]').forEach(function(r){
      if(cat==='all'||r.dataset.cat===cat){r.classList.remove('jny-dimmed');}else{r.classList.add('jny-dimmed');}
    });
  }
  </script>
</section>

<!-- ========== NEWS & ACTIVITY ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">News &amp; Activity</h2>

  <!-- Scrolling ticker -->
  <div class="lt-news-ticker">
    <div class="lt-news-ticker__track">
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127908;</span><span class="lt-news-ticker__text">Presenting at <strong>AERA</strong> Los Angeles</span><span class="lt-news-ticker__date">Apr 2026</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#128220;</span><span class="lt-news-ticker__text">Published in <strong>Psicologia Educativa</strong></span><span class="lt-news-ticker__date">2026</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127908;</span><span class="lt-news-ticker__text"><strong>Clawdbot Unboxed</strong> at Purdue</span><span class="lt-news-ticker__date">Feb 2026</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#128220;</span><span class="lt-news-ticker__text">Published in <strong>Computers &amp; Education: AI</strong></span><span class="lt-news-ticker__date">2025</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127793;</span><span class="lt-news-ticker__text">Joined <strong>PALDT</strong> &amp; <strong>GESC</strong></span><span class="lt-news-ticker__date">Sep 2025</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127942;</span><span class="lt-news-ticker__text"><strong>Erasmus+</strong> $5,000</span><span class="lt-news-ticker__date">2024</span></div>
      <!-- duplicate for seamless loop -->
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127908;</span><span class="lt-news-ticker__text">Presenting at <strong>AERA</strong> Los Angeles</span><span class="lt-news-ticker__date">Apr 2026</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#128220;</span><span class="lt-news-ticker__text">Published in <strong>Psicologia Educativa</strong></span><span class="lt-news-ticker__date">2026</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127908;</span><span class="lt-news-ticker__text"><strong>Clawdbot Unboxed</strong> at Purdue</span><span class="lt-news-ticker__date">Feb 2026</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#128220;</span><span class="lt-news-ticker__text">Published in <strong>Computers &amp; Education: AI</strong></span><span class="lt-news-ticker__date">2025</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127793;</span><span class="lt-news-ticker__text">Joined <strong>PALDT</strong> &amp; <strong>GESC</strong></span><span class="lt-news-ticker__date">Sep 2025</span></div>
      <div class="lt-news-ticker__item"><span class="lt-news-ticker__icon">&#127942;</span><span class="lt-news-ticker__text"><strong>Erasmus+</strong> $5,000</span><span class="lt-news-ticker__date">2024</span></div>
    </div>
  </div>

  <!-- Detailed list -->
  <ul class="lt-news__list">
    <li class="lt-news__item">
      <div class="lt-news__badge lt-news__badge--talk">&#127908;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">Apr 2026 (upcoming)</div>
        <div class="lt-news__text">Presenting at <strong>AERA</strong>, Los Angeles — Meta-analysis on technology &amp; low-income students.</div>
      </div>
    </li>
    <li class="lt-news__item">
      <div class="lt-news__badge lt-news__badge--paper">&#128220;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">2026</div>
        <div class="lt-news__text">Wang &amp; <strong>Tan</strong> published in <em>Psicologia Educativa</em> (Q2) — GenAI scaffolds in EFL writing.</div>
      </div>
    </li>
    <li class="lt-news__item">
      <div class="lt-news__badge lt-news__badge--talk">&#127908;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">Feb 2026</div>
        <div class="lt-news__text"><em>Clawdbot Unboxed</em> at <strong>AI Lunch &amp; Learn</strong>, Purdue College of Education.</div>
      </div>
    </li>
    <li class="lt-news__item">
      <div class="lt-news__badge lt-news__badge--paper">&#128220;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">2025</div>
        <div class="lt-news__text">Li, <strong>Tan</strong> et al. in <em>Computers &amp; Education: AI</em> (Q1, IF&asymp;10.5) — GenAI systematic review.</div>
      </div>
    </li>
    <li class="lt-news__item">
      <div class="lt-news__badge lt-news__badge--service">&#127793;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">Sep 2025</div>
        <div class="lt-news__text">Joined <strong>PALDT</strong> (Marketing) and <strong>GESC</strong> (Committee Member) at Purdue.</div>
      </div>
    </li>
    <li class="lt-news__item">
      <div class="lt-news__badge lt-news__badge--award">&#127942;</div>
      <div class="lt-news__body">
        <div class="lt-news__date">2024</div>
        <div class="lt-news__text"><strong>Erasmus+ Fund</strong> ($5,000) — University of Silesia, Poland.</div>
      </div>
    </li>
  </ul>
</section>

