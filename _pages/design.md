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

  /* ===== PALDT Newsletter Carousel ===== */
  .design-card--wide {
    grid-column: 1 / -1;
    flex-direction: row;
    align-items: stretch;
  }
  .design-card--wide .design-card__body {
    flex: 1; min-width: 0;
  }

  .newsletter-carousel {
    position: relative;
    width: 100%;
    height: 320px;
    overflow: hidden;
    border-radius: 14px;
    border: 1px solid #e8edf5;
    background: #f8fafc;
  }
  .newsletter-track {
    display: flex;
    height: 100%;
    transition: transform 0.5s ease;
  }
  .newsletter-track img {
    flex-shrink: 0;
    width: 240px;
    height: 100%;
    object-fit: cover;
    object-position: top;
    border-right: 1px solid #e8edf5;
    cursor: pointer;
    transition: opacity 0.3s;
  }
  .newsletter-track img:hover { opacity: 0.88; }
  .newsletter-track img:last-child { border-right: none; }

  .carousel-btn {
    position: absolute;
    top: 50%; transform: translateY(-50%);
    width: 32px; height: 32px;
    border-radius: 50%;
    background: rgba(255,255,255,0.92);
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    cursor: pointer;
    font-size: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
    transition: background 0.2s;
    color: #374151;
  }
  .carousel-btn:hover { background: #fff; }
  .carousel-btn--prev { left: 8px; }
  .carousel-btn--next { right: 8px; }

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
    .design-card--wide { flex-direction: column; }
    .newsletter-carousel { height: 260px; }
    .newsletter-track img { width: 200px; }
  }
  @media (max-width: 400px) {
    .design-content .philosophy { padding: 1rem; margin-bottom: 1.5rem; }
    .design-card__img { height: 160px; }
    .newsletter-carousel { height: 220px; }
    .newsletter-track img { width: 160px; }
  }
</style>

<div class="design-content">

<div class="philosophy">
I believe great design serves learning. Whether it's a course interface, a conference poster, or a social media graphic, I approach every project with the same goal: make information clear, inviting, and accessible. My design work bridges instructional design thinking with visual communication.
</div>

<h2>Featured Projects</h2>

<div class="design-grid">

<!-- Zotero Tutorial Video -->
<div class="design-card">
  <div class="design-card__video" onclick="window.open('/files/zotero-tutorial.mp4','_blank')">
    <img src="/images/design/zotero-thumb.jpg" alt="Zotero Tutorial Video thumbnail">
    <div class="design-card__play"></div>
  </div>
  <div class="design-card__body">
    <div class="design-card__title">Zotero Reference Manager Tutorial</div>
    <div class="design-card__tags">
      <span class="design-tag design-tag--video">Video</span>
    </div>
    <div class="design-card__desc">A 2-minute instructional video tutorial on using Zotero for academic reference management. Produced as part of an RA project at Purdue Libraries.</div>
    <span class="design-card__link" onclick="window.open('/files/zotero-tutorial.mp4','_blank')">Watch video &rarr;</span>
  </div>
</div>

</div>

<h2>PALDT Newsletters</h2>

<p style="font-size:0.88rem;color:#4a5568;margin-bottom:1rem;">
  Biweekly newsletters designed for the Purdue Association of Learning Design and Technology (PALDT) as Marketing &amp; Design Officer. Created with Publicate, covering announcements, workshops, events, and community spotlights.
</p>

<div class="newsletter-carousel" id="newsletterCarousel">
  <div class="newsletter-track" id="newsletterTrack">
    <img src="/images/design/paldt-mar22.jpg" alt="PALDT Newsletter Mar 22, 2026" onclick="openLightbox(this.src)">
    <img src="/images/design/paldt-mar09.jpg" alt="PALDT Newsletter Mar 9, 2026" onclick="openLightbox(this.src)">
    <img src="/images/design/paldt-jan26.jpg" alt="PALDT Newsletter Jan 26, 2026" onclick="openLightbox(this.src)">
    <img src="/images/design/paldt-w3.jpg" alt="PALDT Newsletter W3" onclick="openLightbox(this.src)">
    <img src="/images/design/paldt-oct06.jpg" alt="PALDT Newsletter Oct 6, 2025" onclick="openLightbox(this.src)">
    <img src="/images/design/paldt-sep22.jpg" alt="PALDT Newsletter Sep 22, 2025" onclick="openLightbox(this.src)">
    <img src="/images/design/paldt-sep08.jpg" alt="PALDT Newsletter Sep 8, 2025" onclick="openLightbox(this.src)">
  </div>
  <button class="carousel-btn carousel-btn--prev" onclick="scrollCarousel(-1)">&lsaquo;</button>
  <button class="carousel-btn carousel-btn--next" onclick="scrollCarousel(1)">&rsaquo;</button>
</div>

<div class="design-lightbox" id="designLightbox" onclick="this.classList.remove('active')">
  <img src="" alt="Newsletter full view" id="lightboxImg">
</div>

</div>

<script>
// Newsletter carousel
var track = document.getElementById('newsletterTrack');
var carousel = document.getElementById('newsletterCarousel');
var pos = 0;

function scrollCarousel(dir) {
  var step = 260;
  var maxScroll = track.scrollWidth - carousel.offsetWidth;
  pos = Math.max(0, Math.min(pos + dir * step, maxScroll));
  track.style.transform = 'translateX(-' + pos + 'px)';
}

// Lightbox
function openLightbox(src) {
  var lb = document.getElementById('designLightbox');
  document.getElementById('lightboxImg').src = src;
  lb.classList.add('active');
}

// Close on Escape
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    document.getElementById('designLightbox').classList.remove('active');
  }
});
</script>
