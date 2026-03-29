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
  .rdr-lbl{cursor:pointer;transition:opacity .3s,transform .3s ease}
  .rdr-lbl:hover{transform:scale(1.06)}
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
      {id:'genai',l:'GenAI Review \u00b7 CAEAI \'25',s:'literacy',r:155,t:'publication',v:'CAEAI',y:2025,st:'Published',lk:'/publication/2025-two-years-innovation',d:'Systematic review of empirical GenAI research in language learning and teaching.'},
      {id:'pete',l:'PeteChat Design Case',s:'literacy',r:215,t:'progress',v:'Under Review',y:2026,st:'Revising',lk:'/publication/ur-tutor-not-solver',d:'Building a safety-aware LLM tutoring system for university contexts.'},
      {id:'claw',l:'Clawdbot \u00b7 Talk \'26',s:'literacy',r:95,t:'talk',v:'Conference Talk',y:2026,st:'Upcoming',lk:'/publication/2026-clawdbot-unboxed',d:'What Clawdbot does, why it\'s hot, and where it breaks.'},
      {id:'tpxj',l:'TPACK Xinjiang Study',s:'tpack',r:160,t:'progress',v:'Education Sciences',y:2026,st:'In Review',lk:'/publication/ur-tpack-xinjiang',d:'How ethnic and cultural context shapes technology integration knowledge among trainee teachers in Western China.'},
      {id:'idle-r',l:'IDLE Literature Review',s:'idle',r:165,t:'progress',v:'In Progress',y:2026,st:'In Progress',lk:null,d:'Comprehensive literature review of informal digital learning of English (IDLE) research.'},
      {id:'doubao',l:'Doubao \u00b7 PE (Q2) \'26',s:'equity',r:145,t:'publication',v:'Practical English',y:2026,st:'Published',lk:'/publication/2026-doubao-genai-efl',d:'Doubao as a GenAI scaffold in senior high school EFL writing.'},
      {id:'nontrad',l:'NonTrad \u00d7 ChatGPT \u00b7 BJET \'25',cs:['literacy','idle'],a:225,r:185,t:'publication',v:'BJET',y:2025,st:'Published',lk:null,d:'Exploring non-traditional learners\' engagement with ChatGPT for informal language learning.'},
      {id:'lowinc',l:'Low-Income & ChatGPT \u00b7 Lang. \'23',cs:['idle','equity'],a:135,r:185,t:'publication',v:'Language',y:2023,st:'Published',lk:null,d:'Investigating ChatGPT usage patterns among low-income language learners.'},
      {id:'global',l:'Global Learners Study',cs:['equity','tpack'],a:45,r:185,t:'progress',v:'In Progress',y:2026,st:'In Progress',lk:null,d:'Study examining technology access and outcomes for global learners across diverse contexts.'}
    ];

    /* helpers */
    function pol(a,r){return{x:CX+r*Math.cos(a*RAD),y:CY+r*Math.sin(a*RAD)};}
    function el(tag,at){var e=document.createElementNS('http://www.w3.org/2000/svg',tag);for(var k in at)e.setAttribute(k,at[k]);return e;}
    function pPos(p){return pol(p.cs?p.a:sMap[p.s].a,p.r);}
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
      {id:'grad-lit',cx:'50%',cy:'35%',stops:[['0%','#99f6e4',0.55],['45%','#5eead4',0.30],['100%','#0D9488',0.10]]},
      {id:'grad-tpack',cx:'35%',cy:'50%',stops:[['0%','#ddd6fe',0.55],['45%','#a78bfa',0.30],['100%','#7C3AED',0.10]]},
      {id:'grad-eq',cx:'50%',cy:'35%',stops:[['0%','#fed7aa',0.55],['45%','#fb923c',0.30],['100%','#EA580C',0.10]]},
      {id:'grad-idle',cx:'65%',cy:'50%',stops:[['0%','#bae6fd',0.55],['45%','#38bdf8',0.30],['100%','#0369A1',0.10]]}
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
      dots.forEach(function(d){
        var own=(d.p.s===sid)||(d.p.cs&&d.p.cs.indexOf(sid)!==-1);
        d.el.classList.toggle('dim',!own);
        if(own){
          var lx,la;
          if(d.pos.x<CX-50){lx=d.pos.x-14;la='end';}else{lx=d.pos.x+14;la='start';}
          var t=el('text',{x:lx,y:d.pos.y-3,'text-anchor':la,'font-size':'9','font-weight':'600',fill:d.c,class:'rdr-mini rdr-mini-anim'});
          t.textContent=d.p.l;svg.appendChild(t);miniEls.push(t);
          var t2=el('text',{x:lx,y:d.pos.y+8,'text-anchor':la,'font-size':'7.5',fill:'#64748b',class:'rdr-mini rdr-mini-anim',style:'animation-delay:.08s'});
          t2.textContent=d.p.v+' \u00b7 '+d.p.y;svg.appendChild(t2);miniEls.push(t2);
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
  <div style="display:flex;align-items:stretch;gap:0;background:linear-gradient(135deg,#f8fafc 0%,#f1f5f9 50%,#ede9fe 100%);border-radius:16px;overflow:hidden;position:relative;border:1px solid rgba(124,58,237,0.08);box-shadow:0 4px 20px rgba(0,0,0,0.04)">
    <!-- Connecting line -->
    <div style="position:absolute;top:50%;left:0;right:0;height:2px;background:linear-gradient(90deg,#93c5fd,#c4b5fd,#86efac,#fcd34d);z-index:1;opacity:0.4"></div>
    <!-- Card 1 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;border-right:1px solid rgba(124,58,237,0.06);cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(59,130,246,0.08)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#3b82f6,#60a5fa);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(59,130,246,0.25);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(5deg)';this.style.boxShadow='0 8px 25px rgba(59,130,246,0.35)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(59,130,246,0.25)'">&#128269;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#1e293b;margin-bottom:0.3rem">Systematic Reviews</div>
      <div style="font-size:0.68rem;color:#64748b;line-height:1.5">PRISMA · Scoping<br>Meta-analyses</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#3b82f6;font-weight:600;letter-spacing:0.05em">144 ARTICLES SCREENED</div>
    </div>
    <!-- Arrow -->
    <div style="display:flex;align-items:center;color:rgba(124,58,237,0.2);font-size:1.2rem;z-index:2">&#10132;</div>
    <!-- Card 2 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;border-right:1px solid rgba(124,58,237,0.06);cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(139,92,246,0.08)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#8b5cf6,#a78bfa);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(139,92,246,0.25);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(-5deg)';this.style.boxShadow='0 8px 25px rgba(139,92,246,0.35)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(139,92,246,0.25)'">&#128300;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#1e293b;margin-bottom:0.3rem">Mixed Methods</div>
      <div style="font-size:0.68rem;color:#64748b;line-height:1.5">Quan + Qual<br>Surveys · Interviews</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#7c3aed;font-weight:600;letter-spacing:0.05em">CONVERGENT DESIGN</div>
    </div>
    <!-- Arrow -->
    <div style="display:flex;align-items:center;color:rgba(124,58,237,0.2);font-size:1.2rem;z-index:2">&#10132;</div>
    <!-- Card 3 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;border-right:1px solid rgba(124,58,237,0.06);cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(34,197,94,0.08)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#22c55e,#4ade80);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(34,197,94,0.25);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(5deg)';this.style.boxShadow='0 8px 25px rgba(34,197,94,0.35)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(34,197,94,0.25)'">&#128200;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#1e293b;margin-bottom:0.3rem">Statistical Analysis</div>
      <div style="font-size:0.68rem;color:#64748b;line-height:1.5">SPSS · Prism<br>ANOVA · Coh-Metrix</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#16a34a;font-weight:600;letter-spacing:0.05em">108 INDICES TESTED</div>
    </div>
    <!-- Arrow -->
    <div style="display:flex;align-items:center;color:rgba(124,58,237,0.2);font-size:1.2rem;z-index:2">&#10132;</div>
    <!-- Card 4 -->
    <div style="flex:1;padding:1.5rem 1.2rem;text-align:center;position:relative;z-index:2;cursor:default;transition:background 0.4s" onmouseover="this.style.background='rgba(245,158,11,0.08)'" onmouseout="this.style.background='transparent'">
      <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#f59e0b,#fbbf24);margin:0 auto 0.7rem;display:flex;align-items:center;justify-content:center;font-size:1.4rem;box-shadow:0 4px 15px rgba(245,158,11,0.25);transition:transform 0.4s,box-shadow 0.4s" onmouseover="this.style.transform='scale(1.15) rotate(-5deg)';this.style.boxShadow='0 8px 25px rgba(245,158,11,0.35)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 15px rgba(245,158,11,0.25)'">&#127919;</div>
      <div style="font-size:0.82rem;font-weight:700;color:#1e293b;margin-bottom:0.3rem">Design-Based Research</div>
      <div style="font-size:0.68rem;color:#64748b;line-height:1.5">Iterative cycles<br>In-vivo prototyping</div>
      <div style="margin-top:0.6rem;font-size:0.6rem;color:#d97706;font-weight:600;letter-spacing:0.05em">4 DBR PHASES</div>
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

