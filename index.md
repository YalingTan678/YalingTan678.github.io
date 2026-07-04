---
layout: home
author_profile: false
---

<!-- ========== JOURNEY (Swimlane + Compact) ========== -->
<section class="lt-section lt-fade-in">
  <h2 class="lt-section__title">Journey</h2>
  <p style="font-size:0.88rem;color:#4a5568;line-height:1.7;margin-bottom:1rem">From translation studies to AI-mediated learning design, every step has brought me closer to one goal: becoming an instructional designer who harnesses AI to create equitable, human-centered learning experiences at scale.</p>
  <style>
    .jny-filters{display:flex;gap:.4rem;margin-bottom:1rem;flex-wrap:wrap}
    .jny-fbtn{border:none;padding:.3rem .7rem;border-radius:6px;font-size:.7rem;font-weight:600;cursor:pointer;transition:all .2s}
    .jny-fbtn.active{color:#fff!important;background:#1a1a2e!important}
    .jny-wrap{-webkit-overflow-scrolling:touch;position:relative}
    .jny-table{width:100%;border-collapse:collapse}
    .jny-table th{font-size:.7rem;font-weight:700;padding:.6rem .4rem;text-align:center;border-bottom:2px solid #e2e8f0;color:#94a3b8;position:sticky;top:0;background:#fff;z-index:2}
    .jny-table th.jny-now{color:#5b21b6;position:relative}
    .jny-table th.jny-now::after{content:'';position:absolute;bottom:-2px;left:20%;right:20%;height:3px;background:#8b5cf6;border-radius:2px}
    .jny-table td{padding:.4rem .3rem;vertical-align:middle;border-bottom:1px solid #f1f5f9;transition:background .3s}
    .jny-table tr:hover td{background:rgba(0,0,0,.015)}
    .jny-table tr.jny-dimmed td{opacity:.12;transition:opacity .4s}
    .jny-cat{font-size:.7rem;font-weight:700;white-space:nowrap;padding-right:.6rem}
    .jny-cat-dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:middle}
    .jny-tipwrap{position:relative;display:inline-block}
    .jny-chip{display:inline-block;border-radius:8px;padding:.4rem .6rem;font-size:.7rem;font-weight:600;color:#1a1a2e;line-height:1.3;cursor:default;transition:transform .25s,box-shadow .25s;margin:2px 0;text-decoration:none;background:#fff;border:1px solid #e2e8f0;position:relative;overflow:hidden}
    .jny-chip::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px}
    .jny-chip:hover{transform:translateY(-2px);box-shadow:0 4px 14px rgba(0,0,0,.08)}
    .jny-chip small{display:block;font-size:.58rem;font-weight:400;color:#94a3b8;margin-top:.1rem}
    .jny-chip.highlight{border-width:2px;font-size:.72rem}
    .jny-chip.upcoming{border-style:dashed}
    .jny-chip.c-edu::after{background:#8b5cf6} .jny-chip.c-pub::after{background:#3b82f6}
    .jny-chip.c-talk::after{background:#f59e0b} .jny-chip.c-work::after{background:#14b8a6}
    .jny-chip.c-award::after{background:#ec4899}
    .jny-tag{display:inline-block;font-size:.5rem;font-weight:700;padding:.1rem .35rem;border-radius:4px;margin-left:.3rem;vertical-align:middle;letter-spacing:.03em}
    .jny-tip{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) scale(.9);opacity:0;pointer-events:none;background:#fff;color:#475569;font-size:.62rem;line-height:1.5;padding:.55rem .75rem;border-radius:10px;white-space:nowrap;z-index:20;transition:opacity .25s,transform .25s;box-shadow:0 4px 20px rgba(0,0,0,.12);border:1px solid #e2e8f0}
    .jny-tip::after{content:'';position:absolute;bottom:100%;left:50%;transform:translateX(-50%);border:5px solid transparent;border-bottom-color:#fff}
    .jny-tip strong{color:#1a1a2e}
    .jny-tipwrap:hover .jny-tip{opacity:1;transform:translateX(-50%) scale(1)}
    .jny-frame{background:#fff;border-radius:16px;padding:1.2rem;box-shadow:0 2px 16px rgba(0,0,0,.06);border:1px solid #e2e8f0;position:relative;overflow:hidden}
    .jny-frame::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,#0D9488,#7C3AED,#0369A1,#EA580C,#ec4899)}
  </style>
  <!-- Filter buttons -->
  <div class="jny-filters">
    <button class="jny-fbtn active" onclick="jnyFilter('all',this)">All</button>
    <button class="jny-fbtn" style="background:#f5f3ff;color:#8b5cf6" onclick="jnyFilter('edu',this)">Education</button>
    <button class="jny-fbtn" style="background:#eff6ff;color:#3b82f6" onclick="jnyFilter('pub',this)">Publications</button>
    <button class="jny-fbtn" style="background:#f0fdfa;color:#14b8a6" onclick="jnyFilter('work',this)">Experience</button>
    <button class="jny-fbtn" style="background:#fffbeb;color:#d97706" onclick="jnyFilter('talk',this)">Talks</button>
    <button class="jny-fbtn" style="background:#fdf2f8;color:#ec4899" onclick="jnyFilter('award',this)">Awards</button>
  </div>
  <div class="jny-frame">
  <div class="jny-wrap">
    <table class="jny-table">
      <thead><tr><th></th><th>2022</th><th>2023</th><th>2024</th><th class="jny-now">2025</th><th>2026</th></tr></thead>
      <tbody>
        <tr data-cat="edu">
          <td class="jny-cat" style="color:#8b5cf6"><span class="jny-cat-dot" style="background:#8b5cf6"></span>Education</td>
          <td><span class="jny-tipwrap"><span class="jny-chip c-edu">B.A. Translation<small>SWUST, China</small></span><span class="jny-tip"><strong>B.A. in Translation</strong><br>Southwest University of Science &amp; Technology<br>Mianyang, China</span></span></td>
          <td></td>
          <td><span class="jny-tipwrap"><span class="jny-chip c-edu">M.A. Dual Degree<small>NEU + Silesia</small></span><span class="jny-tip"><strong>M.A. Interpreting</strong> (Northeastern U., China)<br><strong>M.A. Philology</strong> (U. of Silesia, Poland)<br>Erasmus+ Double-Degree Program</span></span></td>
          <td><span class="jny-tipwrap"><span class="jny-chip highlight c-edu" style="border:2px solid #a78bfa;color:#5b21b6">Ph.D. Purdue<small style="color:#7c3aed">Learning Design &amp; Tech</small></span><span class="jny-tip"><strong>Doctor of Philosophy</strong><br>Learning Design and Technology<br>Advisor: Dr. Victoria Lowell</span></span></td>
          <td></td>
        </tr>
        <tr data-cat="pub">
          <td class="jny-cat" style="color:#3b82f6"><span class="jny-cat-dot" style="background:#3b82f6"></span>Publications</td>
          <td></td>
          <td><span class="jny-tipwrap"><a href="/publication/2023-clil-translation" class="jny-chip c-pub">CLIL<small>Ed. Advances</small></a><span class="jny-tip"><strong>Gao &amp; Tan (2023)</strong><br>MTI talent cultivation from CLIL perspective<br>Education Advances, 13(12)</span></span></td>
          <td></td>
          <td><span class="jny-tipwrap"><a href="/publication/2025-two-years-innovation" class="jny-chip c-pub">CAEAI<span class="jny-tag" style="background:#dcfce7;color:#16a34a">Q1</span><small>IF = 23.4</small></a><span class="jny-tip"><strong>Li, Tan, Wang &amp; Lowell (2025)</strong><br>Systematic review of empirical GenAI research<br>Computers &amp; Education: AI, 9, 100445</span></span> <span class="jny-tipwrap"><span class="jny-chip c-pub">MJSS<small>Tan &amp; Gao</small></span><span class="jny-tip"><strong>Tan &amp; Gao (2025)</strong><br>Human vs. machine interpreting<br>Mediterranean J. of Social Sciences, 16(3)</span></span></td>
          <td><span class="jny-tipwrap"><a href="/publication/2026-doubao-genai-efl" class="jny-chip c-pub">Doubao<span class="jny-tag" style="background:#dbeafe;color:#2563eb">Q2</span><small>Wang &amp; Tan</small></a><span class="jny-tip"><strong>Wang &amp; Tan (2026)</strong><br>GenAI scaffold in EFL writing<br>Psicologia Educativa, 14, 19-33</span></span> <span class="jny-tipwrap"><a href="/publication/answer-bot-to-tutor" class="jny-chip c-pub">PeteChat<span class="jny-tag" style="background:#ede9fe;color:#7c3aed">In Press</span><small>Springer</small></a><span class="jny-tip"><strong>Li, Tan, Zakharov, Qiu &amp; Acton (in press)</strong><br>From answer bot to course tutor: guardrailed AI assistant<br>Invited book chapter, Springer · arXiv:2606.09845</span></span> <span class="jny-tipwrap"><span class="jny-chip c-pub">3 Under Review<small>ERR · APER · Ed. Sci.</small></span><span class="jny-tip"><strong>Comparison Matters</strong> · Educational Research Review<br><strong>TPACK Xinjiang</strong> · Asia-Pacific Ed. Researcher<br><strong>Authorship &amp; AI</strong> · Education Science</span></span></td>
        </tr>
        <tr data-cat="work">
          <td class="jny-cat" style="color:#14b8a6"><span class="jny-cat-dot" style="background:#14b8a6"></span>Experience</td>
          <td></td><td></td>
          <td><span class="jny-tipwrap"><span class="jny-chip c-work">U. of Silesia<small>Lecturer · 200+</small></span><span class="jny-tip"><strong>Lecturer</strong>, Institute of Linguistics<br>Spoken Chinese &amp; Academic Writing<br>200+ international students · 2023–2024</span></span></td>
          <td><span class="jny-tipwrap"><a href="/service/" class="jny-chip c-work">RA + PALDT + GESC<small>Purdue University</small></a><span class="jny-tip"><strong>Research Assistant</strong>, Purdue Library &amp; SIS<br><strong>PALDT</strong> Marketing &amp; Design Officer<br><strong>GESC</strong> Committee Member</span></span></td>
          <td><span class="jny-tipwrap"><span class="jny-chip c-work">Guest Lecturer<small>EDCI 612</small></span><span class="jny-tip"><strong>Guest Lecturer</strong>, EDCI 612<br>AI and Multilingual Learners<br>Co-presented with Dr. Lowell &amp; Belle Li</span></span></td>
        </tr>
        <tr data-cat="talk">
          <td class="jny-cat" style="color:#f59e0b"><span class="jny-cat-dot" style="background:#f59e0b"></span>Talks</td>
          <td></td><td></td>
          <td><span class="jny-tipwrap"><a href="/publication/2024-call-context" class="jny-chip c-talk">CALL Tokyo<small>Interpreting</small></a><span class="jny-tip"><strong>XXIInd Int'l CALL Conference</strong><br>Human vs. machine interpreting<br>Tokyo, Japan · Sep 2024</span></span> <span class="jny-tipwrap"><span class="jny-chip c-talk">SCT + IPC<small>2 conferences</small></span><span class="jny-tip"><strong>3rd SCT Conference</strong>, Guangdong<br><strong>10th IPC Conference</strong>, Pisa<br>May–Jun 2024</span></span></td>
          <td><span class="jny-tipwrap"><a href="/publication/2025-aect-authenticity" class="jny-chip c-talk">AECT + P-12<small>Las Vegas + Purdue</small></a><span class="jny-tip"><strong>AECT Convention</strong>, Las Vegas<br><strong>Purdue AI in P-12</strong> Conference<br>Oct–Nov 2025</span></span></td>
          <td><span class="jny-tipwrap"><a href="/publication/2026-clawdbot-unboxed" class="jny-chip c-talk">Clawdbot<small>AI Lunch &amp; Learn</small></a><span class="jny-tip"><strong>Clawdbot Unboxed</strong><br>AI Lunch &amp; Learn Series<br>Purdue CoE · Feb 2026</span></span> <span class="jny-tipwrap"><span class="jny-chip upcoming c-talk" style="border:2px dashed #fbbf24">AECT<span class="jny-tag" style="background:#fef3c7;color:#d97706">Upcoming</span><small>Chicago</small></span><span class="jny-tip"><strong>AECT 2026 Convention</strong><br>IDLE pragmatics (ENA) &amp; PeteChat design case<br>Chicago, IL · Oct 2026</span></span></td>
        </tr>
        <tr data-cat="award">
          <td class="jny-cat" style="color:#ec4899"><span class="jny-cat-dot" style="background:#ec4899"></span>Awards</td>
          <td></td><td></td>
          <td><span class="jny-tipwrap"><span class="jny-chip c-award">Fellowship + Erasmus+<small>$2K + $5K</small></span><span class="jny-tip"><strong>National Academic Fellowship</strong> $2K<br>Northeastern University<br><strong>Erasmus+ Fund</strong> $5K · U. of Silesia</span></span></td>
          <td><span class="jny-tipwrap"><span class="jny-chip c-award">LDT Travel<small>$250</small></span><span class="jny-tip"><strong>LDT Travel Support Program</strong><br>Curriculum &amp; Instruction<br>Purdue University</span></span> <span class="jny-tipwrap"><span class="jny-chip c-award">Data Stewardship<span class="jny-tag" style="background:#fce7f3;color:#db2777">Finalist</span><small>Purdue Libraries</small></span><span class="jny-tip"><strong>Data Stewardship Award — Finalist</strong><br>Purdue Libraries (NSF-funded)<br>For PeteChat · AY 2025</span></span></td>
          <td><span class="jny-tipwrap"><span class="jny-chip c-award">Summer Research Grant<small>GRA + tuition</small></span><span class="jny-tip"><strong>Summer Research Grant</strong> (2026)<br>Dept. of Curriculum &amp; Instruction, Purdue<br>.50 FTE GRA + tuition remission · College of Education</span></span> <span class="jny-tipwrap"><span class="jny-chip c-award">WDEA Top 10 AIED<small>Best Practices</small></span><span class="jny-tip"><strong>Top 10 Best Practices in AIED</strong> (2026)<br>World Digital Education Alliance<br>For PeteChat: guardrailed AI assistant</span></span></td>
        </tr>
      </tbody>
    </table>
  </div>
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


