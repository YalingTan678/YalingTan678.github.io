---
title: "Clawdbot Unboxed: What It Does, Why It's Hot, and Where It Breaks"
collection: publications
permalink: /publication/2026-clawdbot-unboxed
excerpt: 'An invited talk examining the capabilities, appeal, and limitations of conversational AI tools in educational contexts.'
date: 2026-02-18
venue: 'AI Lunch and Learn Series, College of Education, Purdue University'
location: 'West Lafayette, IN'
publication_type: "talk"
authors: '<strong>Tan, L.</strong>'
---

## Event Poster

![Clawdbot Unboxed poster](/images/pubs/clawdbot-poster.jpg)

---

## Presentation Slides (21 slides)

<div id="slide-viewer" style="position:relative;max-width:100%;background:#0f172a;border-radius:12px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,0.15)">
  <div style="position:relative;overflow:hidden">
    <img id="slide-img" src="/images/pubs/slides/slide-01-01.jpg" alt="Slide 1 of 21" style="width:100%;display:block;transition:opacity 0.3s">
  </div>
  <div style="display:flex;align-items:center;justify-content:space-between;padding:0.6rem 1rem;background:#1e293b">
    <button onclick="prevSlide()" style="border:none;background:#334155;color:#e2e8f0;width:32px;height:32px;border-radius:8px;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:background 0.2s" onmouseover="this.style.background='#475569'" onmouseout="this.style.background='#334155'">&#9664;</button>
    <span id="slide-counter" style="color:#94a3b8;font-size:0.8rem;font-weight:600">1 / 21</span>
    <button onclick="nextSlide()" style="border:none;background:#334155;color:#e2e8f0;width:32px;height:32px;border-radius:8px;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:background 0.2s" onmouseover="this.style.background='#475569'" onmouseout="this.style.background='#334155'">&#9654;</button>
  </div>
  <div style="display:flex;gap:3px;padding:0 1rem 0.6rem;background:#1e293b;overflow-x:auto">
    <div id="slide-dots" style="display:flex;gap:3px;margin:0 auto"></div>
  </div>
</div>

<script>
(function(){
  var current = 1, total = 21;
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
      img.src='/images/pubs/slides/slide-'+pad(n)+'-'+pad(n)+'.jpg';
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

*[Download full slides (PPTX)](/files/clawdbot-slides.pptx)*

---

## The Signal in the Noise: Why OpenClaw Matters Now

A 50-minute invited presentation at the **AI Lunch and Learn Series**, College of Education, Purdue University (February 18, 2026, BRNG 6138). This talk went beyond the hype to examine what makes OpenClaw/Clawdbot a fundamentally different kind of AI tool.

---

## Standard LLM vs. OpenClaw Agent

| | Standard LLM (e.g., ChatGPT) | OpenClaw Agent |
|:--|:---|:---|
| **Mode** | Passive — waits for input | Active — operates 24/7 |
| **Memory** | Amnesic — session-based | Persistent — remembers your habits |
| **Autonomy** | Responds to prompts | Monitors, triggers, and runs tasks |
| **Scope** | Text conversation | Controls your screen and apps |

---

## How It Works: The Agent Loop

```
┌─────────────┐     ┌──────────────────┐     ┌──────────────┐
│ INPUT LAYER │────▶│   THE AGENT LOOP │────▶│ OUTPUT LAYER │
│             │     │                  │     │              │
│ • Screen    │     │  Observe ──────┐ │     │ • Actions    │
│ • Commands  │     │       ▲        │ │     │ • Files      │
│ • Triggers  │     │       │        ▼ │     │ • Messages   │
│ • Schedule  │     │  Act ◀──── Plan  │     │ • Reports    │
│             │     │                  │     │              │
└─────────────┘     └──────────────────┘     └──────────────┘
```

---

## Presentation Flow (21 Slides)

| Section | Slides | Content |
|:--------|:-------|:--------|
| **Opening** | 1–2 | "The Signal in the Noise" — why OpenClaw is different from chatbots |
| **The Hype** | 3–5 | GitHub star history, founder story, viral adoption |
| **Architecture** | 6–8 | LLM vs. Agent comparison, the Agent Loop diagram |
| **Hands-On** | 9–13 | Step-by-step installation walkthrough: download, config, ignition |
| **Live Demos** | 14–18 | Practical use cases: 24/7 monitoring, automated workflows |
| **Reflection** | 19–21 | Limitations, ethical concerns, Q&A |

---

## Workshop: Zero to Agent

> *"We are moving beyond chatting. Build an agent that remembers your habits, works 24/7, and operates your screen."*

The talk included a hands-on workshop segment where attendees:
- Installed OpenClaw on their own machines
- Configured API keys and system prompts
- Built a basic agent that runs autonomously

---

## Resources

| | |
|:--|:--|
| **Slides** | [Download Presentation (PPTX)](/files/clawdbot-slides.pptx) — 21 slides, 12 MB |
| **Recording** | [Watch on Zoom](https://purdue-edu.zoom.us/rec/share/zsYwqkKqPnDXAYdZWcfFF-MA9vEN0ZJluSVeucFsQC5-xm8u8KBl0NW4yK9Qq1JA.jRD32DqZkMxWRcdH) — Passcode: `64drqp6%` |
