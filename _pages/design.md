---
layout: single
title: "Design Portfolio"
permalink: /design/
author_profile: true
---

<style>
  .design-content { font-size: 0.95rem; line-height: 1.75; }
  .design-content h2 {
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #2a7ae2;
    margin-top: 2.2rem; margin-bottom: 1rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #eef4ff;
  }
  .design-content .philosophy {
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
  .design-content .philosophy:hover {
    box-shadow: 0 4px 24px rgba(99,102,241,.1);
    border-color: rgba(139,92,246,.2);
  }
  .design-content .philosophy::before {
    content: "\201C";
    position: absolute;
    top: -0.1rem; left: 0.8rem;
    font-size: 3.5rem;
    font-family: Georgia, serif;
    color: rgba(139,92,246,.12);
    line-height: 1;
  }
  .design-content .philosophy::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899, #f59e0b);
    border-radius: 0 0 14px 14px;
    opacity: 0;
    transition: opacity .4s;
  }
  .design-content .philosophy:hover::after {
    opacity: 1;
  }

  /* ===== Portfolio Grid ===== */
  .design-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.4rem;
    margin-top: 1rem;
  }

  .design-card {
    display: flex;
    flex-direction: column;
    border: 1px solid #e8edf5;
    border-radius: 14px;
    background: #fff;
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
    cursor: pointer;
  }
  .design-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
    border-color: #2a7ae2;
    color: inherit;
    text-decoration: none;
  }

  .design-card__img {
    width: 100%;
    height: 200px;
    overflow: hidden;
    background: linear-gradient(135deg, #eef4ff, #f8fafc);
  }
  .design-card__img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }
  .design-card:hover .design-card__img img {
    transform: scale(1.05);
  }
  .design-card__img--placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    color: #94a3b8;
  }

  .design-card__body {
    padding: 1rem 1.2rem 1.2rem;
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  .design-card__title {
    font-weight: 650;
    font-size: 0.95rem;
    color: #1a1a2e;
    line-height: 1.4;
    margin-bottom: 0.2rem;
  }
  .design-card__tags {
    display: flex;
    gap: 0.3rem;
    flex-wrap: wrap;
    margin-bottom: 0.5rem;
  }
  .design-tag {
    font-size: 0.65rem;
    font-weight: 600;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    white-space: nowrap;
  }
  .design-tag--figma    { background: #fce7f3; color: #be185d; }
  .design-tag--canva    { background: #dbeafe; color: #2563eb; }
  .design-tag--video    { background: #ede9fe; color: #7c3aed; }
  .design-tag--web      { background: #d1fae5; color: #059669; }
  .design-tag--print    { background: #fef3c7; color: #d97706; }
  .design-tag--branding { background: #fee2e2; color: #dc2626; }

  .design-card__desc {
    font-size: 0.84rem;
    color: #4a5568;
    line-height: 1.6;
    flex: 1;
  }
  .design-card__link {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.78rem;
    color: #2a7ae2;
    margin-top: 0.6rem;
    font-weight: 500;
  }

  /* ===== Featured Project (horizontal) ===== */
  .featured-project {
    display: flex;
    gap: 1.5rem;
    padding: 1.2rem;
    border: 1px solid #e8edf5;
    border-radius: 14px;
    background: #fff;
    align-items: stretch;
    transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
  }
  .featured-project:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    border-color: #2a7ae2;
  }
  .featured-project__video {
    position: relative;
    flex-shrink: 0;
    width: 340px;
    min-height: 220px;
    border-radius: 10px;
    overflow: hidden;
    background: #000;
    cursor: pointer;
  }
  .featured-project__video img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.85;
    transition: transform 0.4s, opacity 0.3s;
  }
  .featured-project:hover .featured-project__video img {
    transform: scale(1.05);
    opacity: 1;
  }
  .featured-project__info {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* ===== Dark Featured Project ===== */
  .featured-project--dark {
    background: #0f0f17;
    border-color: rgba(255,255,255,0.08);
    text-decoration: none;
    color: inherit;
  }
  .featured-project--dark:hover {
    border-color: #818cf8;
    color: inherit;
    text-decoration: none;
  }
  .featured-project--dark .design-card__title { color: #f1f5f9; }
  .featured-project--dark .design-card__desc { color: #94a3b8; }
  .featured-project--dark ul { color: #94a3b8; }
  .featured-project--dark .design-card__link { color: #818cf8; }

  .featured-project__preview {
    flex-shrink: 0;
    width: 340px;
    min-height: 220px;
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Mini hero mock of the Interview Prep site */
  .ips-hero-mock {
    width: 100%;
    height: 100%;
    background: radial-gradient(ellipse at 50% 50%, rgba(99,102,241,0.2) 0%, #0a0a0f 70%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 1.5rem;
    gap: 0.6rem;
  }
  .ips-hero-mock .ips-tag {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 999px;
    font-size: 0.6rem;
    font-weight: 500;
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.05);
    color: #94a3b8;
  }
  .ips-hero-mock .ips-title {
    font-size: 1.3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0.3rem 0;
  }
  .ips-hero-mock .ips-stats {
    display: flex;
    gap: 1.2rem;
    font-size: 0.75rem;
    color: #64748b;
  }
  .ips-hero-mock .ips-stats strong {
    font-size: 1.1rem;
    font-weight: 800;
    background: linear-gradient(135deg, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: block;
    text-align: center;
  }

  /* ===== Video Card ===== */
  .design-card__video {
    position: relative;
    width: 100%;
    height: 200px;
    overflow: hidden;
    background: #000;
    cursor: pointer;
  }
  .design-card__video img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
    opacity: 0.85;
  }
  .design-card:hover .design-card__video img {
    transform: scale(1.05);
    opacity: 1;
  }
  .design-card__play {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 48px; height: 48px;
    border-radius: 50%;
    background: rgba(255,255,255,0.92);
    box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  .design-card:hover .design-card__play {
    transform: translate(-50%, -50%) scale(1.1);
    box-shadow: 0 6px 24px rgba(0,0,0,0.3);
  }
  .design-card__play::after {
    content: '';
    display: block;
    width: 0; height: 0;
    border-style: solid;
    border-width: 8px 0 8px 14px;
    border-color: transparent transparent transparent #2a7ae2;
    margin-left: 3px;
  }

  /* ===== PALDT Newsletter Row with hover-scroll ===== */
  .newsletter-row {
    display: flex;
    gap: 1rem;
    overflow-x: auto;
    padding-bottom: 0.8rem;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
  }
  .newsletter-row::-webkit-scrollbar {
    height: 6px;
  }
  .newsletter-row::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 3px;
  }
  .newsletter-row::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
  }

  .nl-scroll-card {
    flex-shrink: 0;
    width: 220px;
    height: 320px;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #e8edf5;
    background: #fff;
    position: relative;
    cursor: pointer;
    scroll-snap-align: start;
    transition: box-shadow 0.3s, border-color 0.3s;
  }
  .nl-scroll-card:hover {
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    border-color: #2a7ae2;
  }
  .nl-scroll-card img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
    object-position: top;
    transition: transform 3s ease-in-out;
    transform: translateY(0);
  }
  .nl-scroll-card:hover img {
    transform: translateY(var(--scroll-y, -70%));
  }
  /* Date label */
  .nl-scroll-card__label {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    padding: 0.4rem 0.6rem;
    background: linear-gradient(transparent, rgba(0,0,0,0.6));
    color: #fff;
    font-size: 0.72rem;
    font-weight: 600;
    text-align: center;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.3s;
  }
  .nl-scroll-card:hover .nl-scroll-card__label {
    opacity: 1;
  }
  /* Scroll hint icon */
  .nl-scroll-card::before {
    content: '\2195';
    position: absolute;
    top: 8px; right: 8px;
    width: 22px; height: 22px;
    border-radius: 6px;
    background: rgba(0,0,0,0.4);
    color: #fff;
    font-size: 0.65rem;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
    opacity: 0.7;
    transition: opacity 0.3s;
  }
  .nl-scroll-card:hover::before {
    opacity: 0;
  }
  /* Fade hint at bottom */
  .nl-scroll-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 40px;
    background: linear-gradient(transparent, rgba(255,255,255,0.65));
    pointer-events: none;
    transition: opacity 0.3s;
  }
  .nl-scroll-card:hover::after {
    opacity: 0;
  }

  /* ===== Lightbox ===== */
  .design-lightbox {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.85);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  .design-lightbox.active { display: flex; }
  .design-lightbox img {
    max-height: 90vh;
    max-width: 90vw;
    border-radius: 8px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.4);
  }

  /* Responsive */
  @media (max-width: 768px) {
    .design-content { font-size: 0.9rem; }
    .design-content .philosophy { padding: 1.2rem 1.3rem; font-size: 0.9rem; }
    .design-grid { grid-template-columns: 1fr; }
    .featured-project { flex-direction: column; }
    .featured-project__video { width: 100%; min-height: 200px; }
    .featured-project__preview { width: 100%; min-height: 180px; }
    .nl-scroll-card { width: 180px; height: 270px; }
  }
  @media (max-width: 400px) {
    .design-content .philosophy { padding: 1rem; margin-bottom: 1.5rem; }
    .design-card__img { height: 160px; }
    .nl-scroll-card { width: 150px; height: 230px; }
  }
</style>

<div class="design-content">

<div class="philosophy">
I believe great design serves learning. Whether it's a course interface, a conference poster, or a social media graphic, I approach every project with the same goal: make information clear, inviting, and accessible. My design work bridges instructional design thinking with visual communication.
</div>

<h2>Featured Projects</h2>

<!-- Purdue Libraries RA Video Series -->
<div class="featured-project">
  <div class="featured-project__video" onclick="window.open('/files/zotero-tutorial.mp4','_blank')">
    <img src="/images/design/zotero-thumb.jpg" alt="Zotero Tutorial Video thumbnail">
    <div class="design-card__play"></div>
  </div>
  <div class="featured-project__info">
    <div class="design-card__title" style="font-size:1.05rem;">Purdue Libraries Instructional Video Series</div>
    <div class="design-card__tags" style="margin-top:0.3rem;">
      <span class="design-tag design-tag--video">Video</span>
      <span class="design-tag design-tag--web">Coding</span>
    </div>
    <div class="design-card__desc" style="margin-top:0.6rem;">
      As a Research Assistant at Purdue University Libraries &amp; School of Information Studies, I design and produce short instructional videos to support graduate students across the College of Education. This series aims to lower the barrier to essential research skills, covering topics such as:
    </div>
    <ul style="font-size:0.84rem; color:#4a5568; line-height:1.7; padding-left:1.2rem; margin:0.5rem 0 0;">
      <li><strong>Zotero</strong> &mdash; reference management &amp; citation workflows</li>
      <li><strong>Research Guides</strong> &mdash; navigating library databases &amp; resources</li>
      <li><strong>Systematic Writing</strong> &mdash; structuring literature reviews &amp; academic papers</li>
      <li><strong>Data Management</strong> &mdash; organizing research data for reproducibility</li>
    </ul>
    <span class="design-card__link" style="margin-top:0.8rem;" onclick="window.open('/files/zotero-tutorial.mp4','_blank')">Watch Zotero tutorial &rarr;</span>
  </div>
</div>

<!-- Interview Prep Skills -->
<a class="featured-project featured-project--dark" href="https://github.com/YalingTan678/interview-prep-skills" target="_blank">
  <div class="featured-project__preview">
    <div class="ips-hero-mock">
      <span class="ips-tag">Undergrad</span>
      <span class="ips-tag">Master's</span>
      <span class="ips-tag">PhD</span>
      <span class="ips-tag">Claude Code Skill</span>
      <div class="ips-title">Interview Prep Skills</div>
      <div class="ips-stats">
        <span><strong>11</strong> Skills</span>
        <span><strong>3</strong> Workflows</span>
        <span><strong>4</strong> Frameworks</span>
      </div>
    </div>
  </div>
  <div class="featured-project__info">
    <div class="design-card__title" style="font-size:1.05rem;">Interview Prep Skills</div>
    <div class="design-card__tags" style="margin-top:0.3rem;">
      <span class="design-tag design-tag--web">Web</span>
      <span class="design-tag" style="background:#ede9fe;color:#7c3aed;">Claude Code</span>
    </div>
    <div class="design-card__desc" style="margin-top:0.6rem;">
      A systematic, framework-driven interview preparation system designed for university students. Built as a Claude Code skill suite with 11 interactive skills covering the full interview lifecycle:
    </div>
    <ul style="font-size:0.84rem; color:#4a5568; line-height:1.7; padding-left:1.2rem; margin:0.5rem 0 0;">
      <li><strong>Role Investigator</strong> &mdash; decode job descriptions &amp; identify key competencies</li>
      <li><strong>Resume Tailor</strong> &mdash; customize resumes per role with keyword alignment</li>
      <li><strong>Mock Interview</strong> &mdash; AI-powered practice with real-time feedback</li>
      <li><strong>Value Proposition</strong> &mdash; craft compelling personal narratives</li>
      <li><strong>Thank-You Note</strong> &mdash; generate personalized follow-ups</li>
    </ul>
    <span class="design-card__link" style="margin-top:0.8rem;">View on GitHub &rarr;</span>
  </div>
</a>

<h2 style="margin-top:1.5rem;">PALDT Newsletters</h2>

<p style="font-size:0.88rem;color:#4a5568;margin-bottom:1rem;">
  Biweekly newsletters designed for the Purdue Association of Learning Design and Technology (PALDT) as Marketing &amp; Design Officer. Created with Publicate, covering announcements, workshops, events, and community spotlights.
</p>

<div class="newsletter-row">
  <div class="nl-scroll-card" onclick="openLightbox('/images/design/paldt-mar22.jpg')">
    <img src="/images/design/paldt-mar22.jpg" alt="PALDT Newsletter Mar 22, 2026">
    <span class="nl-scroll-card__label">Mar 22, 2026</span>
  </div>
  <div class="nl-scroll-card" onclick="openLightbox('/images/design/paldt-mar09.jpg')">
    <img src="/images/design/paldt-mar09.jpg" alt="PALDT Newsletter Mar 9, 2026">
    <span class="nl-scroll-card__label">Mar 9, 2026</span>
  </div>
  <div class="nl-scroll-card" onclick="openLightbox('/images/design/paldt-jan26.jpg')">
    <img src="/images/design/paldt-jan26.jpg" alt="PALDT Newsletter Jan 26, 2026">
    <span class="nl-scroll-card__label">Jan 26, 2026</span>
  </div>
  <div class="nl-scroll-card" onclick="openLightbox('/images/design/paldt-w3.jpg')">
    <img src="/images/design/paldt-w3.jpg" alt="PALDT Newsletter W3">
    <span class="nl-scroll-card__label">Fall 2025 W3</span>
  </div>
  <div class="nl-scroll-card" onclick="openLightbox('/images/design/paldt-oct06.jpg')">
    <img src="/images/design/paldt-oct06.jpg" alt="PALDT Newsletter Oct 6, 2025">
    <span class="nl-scroll-card__label">Oct 6, 2025</span>
  </div>
  <div class="nl-scroll-card" onclick="openLightbox('/images/design/paldt-sep22.jpg')">
    <img src="/images/design/paldt-sep22.jpg" alt="PALDT Newsletter Sep 22, 2025">
    <span class="nl-scroll-card__label">Sep 22, 2025</span>
  </div>
  <div class="nl-scroll-card" onclick="openLightbox('/images/design/paldt-sep08.jpg')">
    <img src="/images/design/paldt-sep08.jpg" alt="PALDT Newsletter Sep 8, 2025">
    <span class="nl-scroll-card__label">Sep 8, 2025</span>
  </div>
</div>

<div class="design-lightbox" id="designLightbox" onclick="this.classList.remove('active')">
  <img src="" alt="Newsletter full view" id="lightboxImg">
</div>

</div>

<script>
// Hover-scroll: calculate scroll distance for each newsletter card
document.querySelectorAll('.nl-scroll-card').forEach(function(card) {
  var img = card.querySelector('img');
  function calcScroll() {
    if (!img.naturalHeight) return;
    var cardH = card.offsetHeight;
    var imgH = (img.naturalWidth > 0) ? (card.offsetWidth / img.naturalWidth) * img.naturalHeight : img.naturalHeight;
    if (imgH > cardH) {
      var scrollDist = imgH - cardH;
      card.style.setProperty('--scroll-y', '-' + scrollDist + 'px');
      var duration = Math.max(2, Math.min(8, scrollDist / 150));
      img.style.transitionDuration = duration + 's';
    }
  }
  if (img.complete) { calcScroll(); } else { img.addEventListener('load', calcScroll); }
  window.addEventListener('resize', calcScroll);
});

// Lightbox
function openLightbox(src) {
  var lb = document.getElementById('designLightbox');
  document.getElementById('lightboxImg').src = src;
  lb.classList.add('active');
}
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') document.getElementById('designLightbox').classList.remove('active');
});
</script>
