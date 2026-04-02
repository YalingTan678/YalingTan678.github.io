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

  /* Responsive */
  @media (max-width: 768px) {
    .design-content { font-size: 0.9rem; }
    .design-content .philosophy { padding: 1.2rem 1.3rem; font-size: 0.9rem; }
    .design-grid { grid-template-columns: 1fr; }
  }
  @media (max-width: 400px) {
    .design-content .philosophy { padding: 1rem; margin-bottom: 1.5rem; }
    .design-card__img { height: 160px; }
  }
</style>

<div class="design-content">

<div class="philosophy">
I believe great design serves learning. Whether it's a course interface, a conference poster, or a social media graphic, I approach every project with the same goal: make information clear, inviting, and accessible. My design work bridges instructional design thinking with visual communication.
</div>

<h2>Featured Projects</h2>

<div class="design-grid">

<!-- Example card 1 — replace with your real project -->
<div class="design-card">
  <div class="design-card__img design-card__img--placeholder">
    <!-- Replace with: <img src="/images/design/your-image.jpg" alt="..."> -->
    &#x1f3a8;
  </div>
  <div class="design-card__body">
    <div class="design-card__title">PALDT Social Media Graphics</div>
    <div class="design-card__tags">
      <span class="design-tag design-tag--canva">Canva</span>
      <span class="design-tag design-tag--branding">Branding</span>
    </div>
    <div class="design-card__desc">Designed promotional materials for PALDT events and announcements, maintaining consistent visual identity across platforms.</div>
  </div>
</div>

<!-- Example card 2 — replace with your real project -->
<div class="design-card">
  <div class="design-card__img design-card__img--placeholder">
    &#x1f4d0;
  </div>
  <div class="design-card__body">
    <div class="design-card__title">Conference Poster Design</div>
    <div class="design-card__tags">
      <span class="design-tag design-tag--figma">Figma</span>
      <span class="design-tag design-tag--print">Print</span>
    </div>
    <div class="design-card__desc">Academic poster designs for AERA, AECT, and other conference presentations.</div>
  </div>
</div>

<!-- Example card 3 — replace with your real project -->
<div class="design-card">
  <div class="design-card__img design-card__img--placeholder">
    &#x1f310;
  </div>
  <div class="design-card__body">
    <div class="design-card__title">Personal Academic Website</div>
    <div class="design-card__tags">
      <span class="design-tag design-tag--web">Web</span>
    </div>
    <div class="design-card__desc">Designed and built this academic portfolio site using Jekyll and GitHub Pages.</div>
  </div>
</div>

<!-- Add more cards below as needed -->

</div>

</div>
