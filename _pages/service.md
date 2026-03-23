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
    margin-top: 2.5rem; margin-bottom: 1.2rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #eef4ff;
  }
  .svc-content .philosophy {
    font-style: italic; color: #4a5568;
    border-left: 3px solid #2a7ae2;
    padding: 0.8rem 1.2rem;
    margin-bottom: 2rem;
    background: #f8fafc; border-radius: 0 10px 10px 0;
    line-height: 1.7;
  }

  /* ===== Image + Text Card Layout ===== */
  .svc-card {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid #e8edf5;
    align-items: flex-start;
  }
  .svc-card:last-child { border-bottom: none; }

  .svc-card__img {
    flex-shrink: 0;
    width: 280px;
    height: 200px;
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
    gap: 0.4rem;
    margin-bottom: 0.25rem;
  }
  .svc-card__org {
    font-weight: 650;
    font-size: 1rem;
    color: #1a1a2e;
    line-height: 1.4;
  }
  .svc-card__meta {
    font-size: 0.8rem;
    color: #718096;
    flex-shrink: 0;
    text-align: right;
    white-space: nowrap;
  }
  .svc-card__role {
    font-size: 0.88rem;
    color: #2a7ae2;
    font-weight: 500;
    margin-bottom: 0.5rem;
  }
  .svc-card__desc {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .svc-card__desc li {
    font-size: 0.88rem;
    color: #4a5568;
    line-height: 1.65;
    padding-left: 1.1rem;
    position: relative;
    margin-bottom: 0.3rem;
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

  /* ===== Carousel (for PALDT scrollable images) ===== */
  .svc-carousel {
    flex-shrink: 0;
    width: 280px;
    height: 200px;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    position: relative;
  }
  .svc-carousel__track {
    display: flex;
    height: 100%;
    transition: transform 0.45s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  }
  .svc-carousel__slide {
    min-width: 100%;
    height: 100%;
  }
  .svc-carousel__slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .svc-carousel__btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 28px; height: 28px;
    border-radius: 50%;
    border: none;
    background: rgba(255,255,255,0.85);
    color: #1a1a2e;
    font-size: 0.85rem;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s;
    z-index: 2;
    line-height: 1;
  }
  .svc-carousel__btn:hover { background: #fff; }
  .svc-carousel__btn--prev { left: 6px; }
  .svc-carousel__btn--next { right: 6px; }
  .svc-carousel__dots {
    position: absolute;
    bottom: 8px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 5px;
    z-index: 2;
  }
  .svc-carousel__dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: rgba(255,255,255,0.5);
    border: none;
    padding: 0;
    cursor: pointer;
    transition: background 0.2s;
  }
  .svc-carousel__dot.active { background: #fff; }

  /* Responsive */
  @media (max-width: 640px) {
    .svc-card { flex-direction: column; }
    .svc-card__img, .svc-carousel { width: 100%; height: 200px; }
    .svc-card__meta { text-align: left; }
  }

  /* ===== Awards ===== */
  .svc-content .award-item {
    display: flex; justify-content: space-between;
    align-items: flex-start; flex-wrap: wrap; gap: 0.5rem;
    padding: 0.7rem 0; border-bottom: 1px solid #e8edf5;
  }
  .svc-content .award-item:last-child { border-bottom: none; }
  .svc-content .award-amount {
    font-size: 0.83rem; color: #22c55e; font-weight: 600;
    background: #f0fdf4; padding: 0.15rem 0.5rem; border-radius: 6px;
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

<!-- PALDT (with carousel) -->
<div class="svc-card">
  <div class="svc-carousel" id="paldt-carousel">
    <div class="svc-carousel__track">
      <!-- Add more slides here: copy a svc-carousel__slide div with a new image -->
      <div class="svc-carousel__slide"><img src="/images/service/paldt.jpg" alt="PALDT Newsletter March 2026"></div>
      <!-- <div class="svc-carousel__slide"><img src="/images/service/paldt-2.jpg" alt="PALDT event"></div> -->
      <!-- <div class="svc-carousel__slide"><img src="/images/service/paldt-3.jpg" alt="PALDT workshop"></div> -->
    </div>
    <button class="svc-carousel__btn svc-carousel__btn--prev" aria-label="Previous">&lsaquo;</button>
    <button class="svc-carousel__btn svc-carousel__btn--next" aria-label="Next">&rsaquo;</button>
    <div class="svc-carousel__dots"></div>
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

<!-- AI in P-12 -->
<div class="svc-card">
  <div class="svc-card__img">
    <img src="/images/service/ai-p12.png" alt="Lily Tan presenting at Purdue AI in P-12 Conference">
  </div>
  <div class="svc-card__body">
    <div class="svc-card__header">
      <span class="svc-card__org">Purdue AI in P-12 Conference</span>
      <span class="svc-card__meta">Nov 2025</span>
    </div>
    <div class="svc-card__role">Graduate Judge</div>
    <ul class="svc-card__desc">
      <li>Reviewed and scored conference submissions and offered evaluative feedback.</li>
    </ul>
  </div>
</div>

<h2>Honors, Awards &amp; Recognitions</h2>

<div class="award-item">
  <div><strong>LDT Travel Support Program</strong><br><span style="font-size:0.85rem;color:#718096">Purdue University, Curriculum and Instruction &amp; LDT Programs</span></div>
  <div><span class="award-amount">$250</span><br><span style="font-size:0.78rem;color:#718096">2025</span></div>
</div>

<div class="award-item">
  <div><strong>National Academic Fellowship</strong><br><span style="font-size:0.85rem;color:#718096">Northeastern University, Department of Interpreting</span></div>
  <div><span class="award-amount">$2,000</span><br><span style="font-size:0.78rem;color:#718096">2023&ndash;2024</span></div>
</div>

<div class="award-item">
  <div><strong>Erasmus+ Fund</strong><br><span style="font-size:0.85rem;color:#718096">University of Silesia, Department of Linguistics</span></div>
  <div><span class="award-amount">$5,000</span><br><span style="font-size:0.78rem;color:#718096">2024</span></div>
</div>

<div class="award-item">
  <div><strong>National Undergraduate Award</strong><br><span style="font-size:0.85rem;color:#718096">Southwest University of Science and Technology, Department of Translation</span></div>
  <div><span class="award-amount">$750</span><br><span style="font-size:0.78rem;color:#718096">2019</span></div>
</div>

<h2>Certifications</h2>

<ul>
<li><strong>Quality Matters Rubric Workshop (7th ed.) Certificate</strong> (March 2026)</li>
</ul>

<h2>Professional Memberships</h2>

<ul>
<li>American Educational Research Association (AERA) &mdash; 2025 to Present</li>
<li>Association for Educational Communications and Technology (AECT) &mdash; 2025 to Present</li>
</ul>

</div>

<script>
// Carousel functionality
document.querySelectorAll('.svc-carousel').forEach(function(carousel) {
  var track = carousel.querySelector('.svc-carousel__track');
  var slides = carousel.querySelectorAll('.svc-carousel__slide');
  var prevBtn = carousel.querySelector('.svc-carousel__btn--prev');
  var nextBtn = carousel.querySelector('.svc-carousel__btn--next');
  var dotsContainer = carousel.querySelector('.svc-carousel__dots');
  var current = 0;
  var total = slides.length;

  // Hide controls if only 1 slide
  if (total <= 1) {
    prevBtn.style.display = 'none';
    nextBtn.style.display = 'none';
    return;
  }

  // Create dots
  for (var i = 0; i < total; i++) {
    var dot = document.createElement('button');
    dot.className = 'svc-carousel__dot' + (i === 0 ? ' active' : '');
    dot.setAttribute('aria-label', 'Slide ' + (i + 1));
    dot.dataset.index = i;
    dotsContainer.appendChild(dot);
  }
  var dots = dotsContainer.querySelectorAll('.svc-carousel__dot');

  function goTo(index) {
    current = (index + total) % total;
    track.style.transform = 'translateX(-' + (current * 100) + '%)';
    dots.forEach(function(d, j) {
      d.classList.toggle('active', j === current);
    });
  }

  prevBtn.addEventListener('click', function() { goTo(current - 1); });
  nextBtn.addEventListener('click', function() { goTo(current + 1); });
  dots.forEach(function(dot) {
    dot.addEventListener('click', function() { goTo(parseInt(dot.dataset.index)); });
  });

  // Auto-play every 4 seconds
  setInterval(function() { goTo(current + 1); }, 4000);
});
</script>
