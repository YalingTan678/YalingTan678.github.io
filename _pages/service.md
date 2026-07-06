---
layout: single
title: "Service & Leadership"
permalink: /service/
author_profile: true
---

<style>
  .svc-content { font-size: 0.95rem; line-height: 1.75; }
  .svc-content h2 {
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #2a7ae2;
    margin-top: 1.6rem; margin-bottom: 0.8rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #eef4ff;
  }
  .svc-content .philosophy {
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
  .svc-content .philosophy:hover {
    box-shadow: 0 4px 24px rgba(99,102,241,.1);
    border-color: rgba(139,92,246,.2);
  }
  .svc-content .philosophy::before {
    content: "\201C";
    position: absolute;
    top: -0.1rem; left: 0.8rem;
    font-size: 3.5rem;
    font-family: Georgia, serif;
    color: rgba(139,92,246,.12);
    line-height: 1;
  }
  .svc-content .philosophy::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899, #f59e0b);
    border-radius: 0 0 14px 14px;
    opacity: 0;
    transition: opacity .4s;
  }
  .svc-content .philosophy:hover::after {
    opacity: 1;
  }

  /* ===== Image + Text Card Layout ===== */
  .svc-card {
    display: flex;
    gap: 1.1rem;
    margin-bottom: 1.1rem;
    padding-bottom: 1.1rem;
    border-bottom: 1px solid #e8edf5;
    align-items: flex-start;
  }
  .svc-card:last-child { border-bottom: none; }

  .svc-card__img {
    flex-shrink: 0;
    width: 190px;
    height: 132px;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
  }
  .svc-card__img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }
  .svc-card:hover .svc-card__img img {
    transform: scale(1.04);
  }

  .svc-card__body { flex: 1; min-width: 0; }
  .svc-card__header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-bottom: 0.15rem;
  }
  .svc-card__org {
    font-weight: 650;
    font-size: 0.88rem;
    color: #1a1a2e;
    line-height: 1.3;
  }
  .svc-card__meta {
    font-size: 0.76rem;
    color: #718096;
    flex-shrink: 0;
    text-align: right;
    white-space: nowrap;
  }
  .svc-card__role {
    font-size: 0.78rem;
    color: #2a7ae2;
    font-weight: 500;
    margin-bottom: 0.18rem;
  }
  .svc-card__desc {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .svc-card__desc li {
    font-size: 0.76rem;
    color: #4a5568;
    line-height: 1.4;
    padding-left: 1rem;
    position: relative;
    margin-bottom: 0.08rem;
  }
  .svc-card__desc li::before {
    content: '';
    position: absolute;
    left: 0; top: 0.6em;
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #2a7ae2;
    opacity: 0.45;
  }

  /* ===== Hover-scroll long image (PALDT newsletter) ===== */
  .svc-scroll-img {
    flex-shrink: 0;
    width: 190px;
    height: 132px;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    position: relative;
    cursor: pointer;
  }
  .svc-scroll-img img {
    width: 100%;
    height: auto;
    object-fit: cover;
    object-position: top;
    display: block;
    transition: transform 3s ease-in-out;
    transform: translateY(0);
  }
  .svc-scroll-img:hover img {
    /* JS will handle the exact translateY based on image height */
    transform: translateY(var(--scroll-y, -70%));
  }
  /* Fade hint at bottom to show it's scrollable */
  .svc-scroll-img::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 40px;
    background: linear-gradient(transparent, rgba(255,255,255,0.7));
    pointer-events: none;
    transition: opacity 0.3s;
  }
  .svc-scroll-img:hover::after {
    opacity: 0;
  }
  /* Small scroll hint icon */
  .svc-scroll-img::before {
    content: '\2195';
    position: absolute;
    top: 8px; right: 8px;
    width: 24px; height: 24px;
    border-radius: 6px;
    background: rgba(0,0,0,0.45);
    color: #fff;
    font-size: 0.7rem;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
    opacity: 0.8;
    transition: opacity 0.3s;
  }
  .svc-scroll-img:hover::before {
    opacity: 0;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .svc-content { font-size: 0.9rem; }
    .svc-content .philosophy { padding: 1.2rem 1.3rem; font-size: 0.9rem; }
    .svc-content .philosophy::before { font-size: 3.5rem; }
    .svc-card__img, .svc-scroll-img { width: 200px; height: 150px; }
    .svc-card { gap: 1rem; }
  }
  @media (max-width: 600px) {
    .svc-card { flex-direction: column; }
    .svc-card__img, .svc-scroll-img { width: 100%; height: 200px; }
    .svc-card__header { flex-direction: column; }
    .svc-card__meta { text-align: left; white-space: normal; }
    .svc-content .award-item { flex-direction: column; align-items: flex-start; gap: 0.3rem; }
    .svc-content .award-right { text-align: left; min-width: auto; }
  }
  @media (max-width: 400px) {
    .svc-content .philosophy { padding: 1rem; margin-bottom: 1.5rem; }
    .svc-card__img, .svc-scroll-img { height: 160px; }
    .svc-card__org { font-size: 0.9rem; }
    .svc-card__desc li { font-size: 0.82rem; }
  }

  /* ===== Awards ===== */
  .svc-content .award-item {
    display: flex; justify-content: space-between;
    align-items: center; gap: 0.5rem;
    padding: 0.4rem 0; border-bottom: 1px solid #e8edf5;
    line-height: 1.5;
  }
  .svc-content .award-item strong { font-size: 0.88rem; }
  .svc-content > ul li, .svc-content .page__content ul li {
    font-size: 0.88rem;
    margin-bottom: 0.15rem;
  }
  .svc-content .award-item:last-child { border-bottom: none; }
  .svc-content .award-right {
    text-align: right; flex-shrink: 0; min-width: 90px;
  }
  .svc-content .award-amount {
    font-size: 0.78rem; color: #22c55e; font-weight: 600;
    background: #f0fdf4; padding: 0.1rem 0.45rem; border-radius: 6px;
    display: inline-block;
  }
</style>

<div class="svc-content">

<div class="philosophy">
My service philosophy is to strengthen academic communities through reliable and design-minded support. I focus on making opportunities visible, communication clear, and events smooth. I also prioritize inclusive mentoring by connecting people thoughtfully and fostering supportive, sustainable relationships. I serve consistently, listen first, and improve systems based on real needs.
</div>

<h2>Service &amp; Leadership</h2>

<!-- Lunar New Year Celebration -->
<div class="svc-card">
  <div class="svc-card__img">
    <img src="/images/service/lunar-new-year.jpg" alt="Purdue Lunar New Year Celebration booth">
  </div>
  <div class="svc-card__body">
    <div class="svc-card__header">
      <span class="svc-card__org">Purdue Lunar New Year Celebration, Asian American and Asian Resource and Cultural Center (AAARCC)</span>
      <span class="svc-card__meta">Feb 2026</span>
    </div>
    <div class="svc-card__role">Cultural Exhibit Contributor</div>
    <ul class="svc-card__desc">
      <li>Represented the College of Education; designed and hosted a cultural exhibit booth for 1,200+ attendees.</li>
    </ul>
  </div>
</div>

<!-- PALDT (hover-scroll long newsletter) -->
<div class="svc-card">
  <div class="svc-scroll-img" id="paldt-scroll">
    <img src="/images/service/paldt.jpg" alt="PALDT Newsletter March 2026">
  </div>
  <div class="svc-card__body">
    <div class="svc-card__header">
      <span class="svc-card__org">PALDT (Purdue Association of Learning Design and Technology)</span>
      <span class="svc-card__meta">Sep 2025 &ndash; Present</span>
    </div>
    <div class="svc-card__role">Marketing &amp; Design Officer</div>
    <ul class="svc-card__desc">
      <li>Manage PALDT's online presence and social media weekly; design promotional materials for events and announcements biweekly.</li>
      <li>Support technology needs for PALDT functions and meetings.</li>
    </ul>
  </div>
</div>

<!-- GESC -->
<div class="svc-card">
  <div class="svc-card__img">
    <img src="/images/service/gesc.png" alt="Purdue GSEC">
  </div>
  <div class="svc-card__body">
    <div class="svc-card__header">
      <span class="svc-card__org">GESC (Purdue Graduate Student Education Council)</span>
      <span class="svc-card__meta">Sep 2025 &ndash; Present</span>
    </div>
    <div class="svc-card__role">Committee Member</div>
    <ul class="svc-card__desc">
      <li>Collaborate with committee members to design and coordinate mentorship initiatives.</li>
      <li>Match mentors and mentees based on research interests, career goals, and program needs to foster meaningful connections.</li>
    </ul>
  </div>
</div>

<h2>Honors, Awards &amp; Recognitions</h2>

<div class="award-item">
  <div style="flex:1"><strong>Summer Research Grant</strong><br><span style="font-size:0.85rem;color:#718096">Department of Curriculum &amp; Instruction, College of Education, Purdue University &middot; .50 FTE GRA with tuition remission</span></div>
  <div class="award-right"><span class="award-amount">$4,695.68</span><br><span style="font-size:0.78rem;color:#718096">2026</span></div>
</div>

<div class="award-item">
  <span style="flex-shrink:0;cursor:pointer" title="View certificate" onclick="openSvcLightbox('/images/service/wdea-cert.jpg')">
    <img src="/images/service/wdea-cert.jpg" alt="WDEA Top 10 Best Practices in AIED certificate" style="width:88px;height:auto;display:block;border-radius:6px;border:1px solid #e8edf5;box-shadow:0 3px 10px rgba(15,23,42,.12);transition:transform .25s" onmouseover="this.style.transform='scale(1.6)'" onmouseout="this.style.transform='scale(1)'">
  </span>
  <div style="flex:1"><strong>Top 10 Best Practices in AIED</strong><br><span style="font-size:0.85rem;color:#718096">World Digital Education Alliance (WDEA), for the PeteChat guardrailed AI assistant</span></div>
  <div class="award-right"><span class="award-amount">Top 10</span><br><span style="font-size:0.78rem;color:#718096">2026</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>Seeding Solutions Phase 1 Award</strong><br><span style="font-size:0.85rem;color:#718096">ShahLab.AI, Purdue University &middot; VIP AI for Education Team &middot; Graduate Assistant</span></div>
  <div class="award-right"><span class="award-amount">$2,000</span><br><span style="font-size:0.78rem;color:#718096">2026</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>Data Stewardship Award &mdash; Finalist</strong><br><span style="font-size:0.85rem;color:#718096">Purdue Libraries (NSF-funded initiative), for PeteChat</span></div>
  <div class="award-right"><span class="award-amount">Finalist</span><br><span style="font-size:0.78rem;color:#718096">AY 2025</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>LDT Travel Support Program</strong><br><span style="font-size:0.85rem;color:#718096">Curriculum &amp; Instruction and LDT Programs, Purdue University</span></div>
  <div class="award-right"><span class="award-amount">$250</span><br><span style="font-size:0.78rem;color:#718096">2025</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>Erasmus+ Scholarship</strong><br><span style="font-size:0.85rem;color:#718096">University of Silesia, Department of Linguistics</span></div>
  <div class="award-right"><span class="award-amount">$5,000</span><br><span style="font-size:0.78rem;color:#718096">2024</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>National Academic Fellowship</strong><br><span style="font-size:0.85rem;color:#718096">Northeastern University, Department of Interpreting</span></div>
  <div class="award-right"><span class="award-amount">$2,000</span><br><span style="font-size:0.78rem;color:#718096">2023&ndash;2024</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>National Undergraduate Award</strong><br><span style="font-size:0.85rem;color:#718096">Southwest University of Science and Technology, Department of Translation</span></div>
  <div class="award-right"><span class="award-amount">$750</span><br><span style="font-size:0.78rem;color:#718096">2019</span></div>
</div>

<h2>Peer Review</h2>

<div class="award-item">
  <div style="flex:1"><strong>Ad-hoc Reviewer</strong><br><span style="font-size:0.85rem;color:#718096">ACM Transactions on Computing Education (TOCE) &middot; 2026</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>Proposal Reviewer</strong><br><span style="font-size:0.85rem;color:#718096">AECT International Convention &middot; 2026</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>Graduate Judge</strong><br><span style="font-size:0.85rem;color:#718096">Purdue AI in P-12 Conference &middot; reviewed and scored conference submissions &middot; Nov 2025</span></div>
</div>

<h2>Certifications</h2>

<div class="award-item">
  <span style="flex-shrink:0;cursor:pointer" title="View certificate" onclick="openSvcLightbox('/images/service/qm-appqmr-cert.jpg')">
    <img src="/images/service/qm-appqmr-cert.jpg" alt="Independent Applying the QM Rubric (APPQMR) certificate" style="width:88px;height:auto;display:block;border-radius:6px;border:1px solid #e8edf5;box-shadow:0 3px 10px rgba(15,23,42,.12);transition:transform .25s" onmouseover="this.style.transform='scale(1.6)'" onmouseout="this.style.transform='scale(1)'">
  </span>
  <div style="flex:1"><strong>Independent Applying the QM Rubric (APPQMR)</strong><br><span style="font-size:0.85rem;color:#718096">Quality Matters &middot; October 2025</span></div>
</div>

<h2>Professional Memberships</h2>

<div class="award-item">
  <div style="flex:1"><strong>American Educational Research Association (AERA)</strong><br><span style="font-size:0.85rem;color:#718096">Member &middot; 2025 &ndash; Present</span></div>
</div>

<div class="award-item">
  <div style="flex:1"><strong>Association for Educational Communications and Technology (AECT)</strong><br><span style="font-size:0.85rem;color:#718096">Member &middot; 2025 &ndash; Present</span></div>
</div>

</div>

<script>
/* Calculate scroll distance based on actual image height */
document.querySelectorAll('.svc-scroll-img').forEach(function(container) {
  var img = container.querySelector('img');

  function calcScroll() {
    if (!img.naturalHeight) return;
    var containerH = container.offsetHeight;
    var imgH = (img.naturalWidth > 0) ? (container.offsetWidth / img.naturalWidth) * img.naturalHeight : img.naturalHeight;
    if (imgH > containerH) {
      var scrollDist = imgH - containerH;
      container.style.setProperty('--scroll-y', '-' + scrollDist + 'px');
      /* Adjust transition speed */
      var duration = Math.max(2, Math.min(6, scrollDist / 200));
      img.style.transitionDuration = duration + 's';
    }
  }

  if (img.complete) {
    calcScroll();
  } else {
    img.addEventListener('load', calcScroll);
  }
  /* Recalculate on resize */
  window.addEventListener('resize', calcScroll);
});
</script>

<div id="svcLightbox" onclick="this.style.display='none'" style="display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.85);z-index:9999;align-items:center;justify-content:center;cursor:pointer">
  <img id="svcLightboxImg" src="" alt="Full view" style="max-height:92vh;max-width:94vw;border-radius:8px;box-shadow:0 8px 40px rgba(0,0,0,.4)">
</div>
<script>
function openSvcLightbox(src){
  var lb=document.getElementById('svcLightbox');
  document.getElementById('svcLightboxImg').src=src;
  lb.style.display='flex';
}
document.addEventListener('keydown',function(e){
  if(e.key==='Escape')document.getElementById('svcLightbox').style.display='none';
});
</script>
