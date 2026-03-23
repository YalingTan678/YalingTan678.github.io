---
layout: single
title: "EDCI 612: AI and Multilingual Learners"
permalink: /teaching/edci612/
author_profile: true
---

<style>
  .talk-page { font-size: 0.95rem; line-height: 1.75; }
  .talk-page h2 {
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #2a7ae2;
    margin-top: 2.2rem; margin-bottom: 1rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #eef4ff;
  }
  .talk-meta {
    display: flex; flex-wrap: wrap; gap: 1.5rem;
    font-size: 0.88rem; color: #4a5568;
    margin-bottom: 2rem;
    padding: 1rem 1.4rem;
    background: #f8fafc;
    border-radius: 12px;
    border: 1px solid #e8edf5;
  }
  .talk-meta strong { color: #1a1a2e; }
  .talk-speakers {
    display: flex; flex-wrap: wrap; gap: 1rem;
    margin: 1rem 0 2rem;
  }
  .talk-speaker {
    display: flex; align-items: center; gap: 0.6rem;
    padding: 0.5rem 1rem;
    background: #f0f4ff;
    border-radius: 10px;
    font-size: 0.85rem;
    color: #2d3748;
  }
  .talk-desc {
    color: #4a5568;
    margin-bottom: 2rem;
  }
  .talk-desc li {
    margin-bottom: 0.5rem;
  }
</style>

<div class="talk-page">

<div class="talk-meta">
  <div><strong>Course:</strong> EDCI 612 &mdash; AI and Multilingual Learners</div>
  <div><strong>Institution:</strong> Purdue University</div>
  <div><strong>Date:</strong> February 2026</div>
  <div><strong>Role:</strong> Guest Lecturer</div>
</div>

<h2>Description</h2>

<div class="talk-desc">

This guest lecture was part of EDCI 612, a graduate seminar exploring the intersection of artificial intelligence and multilingual education. The session, titled **"GenAI Research and Language Education,"** was co-presented with Dr. Victoria Lowell and Belle Li.

The presentation covered three interconnected themes:

- **Learning Analytics for Multilingual Learners** — How AI-powered tools can track and support language development through data-driven insights, enabling instructors to personalize learning pathways for students with diverse linguistic backgrounds.
- **AI Tutors and Self-Directed Language Learning** — Examining the role of conversational AI (e.g., ChatGPT, Doubao) as scaffolding tools for informal digital learning of English (IDLE), and how students use these tools for autonomous language practice beyond the classroom.
- **Instructional Design Implications** — Frameworks for integrating GenAI into language curricula while maintaining pedagogical rigor, addressing issues of AI literacy, academic integrity, and equitable access for multilingual populations.

The lecture engaged doctoral students in critical discussions about the promises and limitations of GenAI in language education, drawing on recent empirical studies including systematic reviews of 144+ GenAI research articles in language learning.

</div>

<h2>Speakers</h2>

<div class="talk-speakers">
  <div class="talk-speaker"><strong>Lily Tan</strong> &mdash; PhD Student, Learning Design & Technology</div>
  <div class="talk-speaker"><strong>Belle Li</strong> &mdash; PhD Candidate, Learning Design & Technology</div>
  <div class="talk-speaker"><strong>Dr. Victoria Lowell</strong> &mdash; Clinical Professor, Learning Design & Technology</div>
</div>

<h2>Presentation Slides (31 slides)</h2>

<div id="slide-viewer" style="position:relative;max-width:100%;background:#0f172a;border-radius:12px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.15)">
  <div style="position:relative;overflow:hidden">
    <img id="slide-img" src="/images/teaching/edci612-slides/slide-01.jpg" alt="Slide 1 of 31" style="width:100%;display:block;transition:opacity 0.3s">
  </div>
  <div style="display:flex;align-items:center;justify-content:space-between;padding:0.6rem 1rem;background:#1e293b">
    <button onclick="prevSlide()" style="border:none;background:#334155;color:#e2e8f0;width:32px;height:32px;border-radius:8px;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:background 0.2s" onmouseover="this.style.background='#475569'" onmouseout="this.style.background='#334155'">&#9664;</button>
    <span id="slide-counter" style="color:#94a3b8;font-size:0.8rem;font-weight:600">1 / 31</span>
    <button onclick="nextSlide()" style="border:none;background:#334155;color:#e2e8f0;width:32px;height:32px;border-radius:8px;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:background 0.2s" onmouseover="this.style.background='#475569'" onmouseout="this.style.background='#334155'">&#9654;</button>
  </div>
  <div style="display:flex;gap:3px;padding:0 1rem 0.6rem;background:#1e293b;overflow-x:auto">
    <div id="slide-dots" style="display:flex;gap:3px;margin:0 auto"></div>
  </div>
</div>

<script>
(function(){
  var current = 1, total = 31;
  var img = document.getElementById('slide-img');
  var counter = document.getElementById('slide-counter');
  var dotsC = document.getElementById('slide-dots');
  for(var i=1;i<=total;i++){
    var d=document.createElement('button');
    d.style.cssText='width:8px;height:8px;border-radius:50%;border:none;padding:0;cursor:pointer;transition:all 0.2s;'+(i===1?'background:#60a5fa;transform:scale(1.3)':'background:#475569');
    d.dataset.i=i;
    d.onclick=function(){goTo(parseInt(this.dataset.i))};
    dotsC.appendChild(d);
  }
  function pad(n){return n<10?'0'+n:''+n}
  function goTo(n){
    current=n;
    img.style.opacity='0.5';
    setTimeout(function(){
      img.src='/images/teaching/edci612-slides/slide-'+pad(n)+'.jpg';
      img.alt='Slide '+n+' of '+total;
      img.style.opacity='1';
    },150);
    counter.textContent=n+' / '+total;
    var dots=dotsC.children;
    for(var j=0;j<dots.length;j++){
      dots[j].style.background=j===n-1?'#60a5fa':'#475569';
      dots[j].style.transform=j===n-1?'scale(1.3)':'scale(1)';
    }
  }
  window.prevSlide=function(){goTo(current<=1?total:current-1)};
  window.nextSlide=function(){goTo(current>=total?1:current+1)};
  document.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight')nextSlide();
    if(e.key==='ArrowLeft')prevSlide();
  });
})();
</script>

*[Download full slides (PPTX)](/files/edci612-slides.pptx)*

</div>
