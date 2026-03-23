---
layout: single
title: "Teaching"
permalink: /teaching/
author_profile: true
---

<style>
  .teach-content { font-size: 0.95rem; line-height: 1.75; }
  .teach-content h2 {
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #2a7ae2;
    margin-top: 2.2rem; margin-bottom: 1rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #eef4ff;
  }
  .teach-content .philosophy {
    position: relative;
    color: #2d3748;
    padding: 1.5rem 1.8rem;
    margin-bottom: 2.5rem;
    background: linear-gradient(135deg, #f0f4ff 0%, #e8f4f8 40%, #fdf2f8 100%);
    border-radius: 16px;
    line-height: 1.8;
    font-size: 0.95rem;
    border: 1px solid rgba(99, 102, 241, 0.08);
    box-shadow: 0 4px 24px rgba(99, 102, 241, 0.06), 0 1px 4px rgba(0, 0, 0, 0.03);
    overflow: hidden;
  }
  .teach-content .philosophy::before {
    content: "\201C";
    position: absolute;
    top: -0.15rem; left: 1rem;
    font-size: 4.5rem;
    font-family: Georgia, serif;
    background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    opacity: 0.25;
    line-height: 1;
  }
  .teach-content .philosophy::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899, #f59e0b);
    border-radius: 0 0 16px 16px;
  }

  /* ===== Teaching Card Layout (matches Service page) ===== */
  .teach-card {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 1.2rem;
    padding: 1.2rem;
    border: 1px solid #e8edf5;
    border-radius: 14px;
    background: #fff;
    align-items: flex-start;
    text-decoration: none;
    color: inherit;
    transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
    cursor: pointer;
  }
  .teach-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
    border-color: #2a7ae2;
    color: inherit;
    text-decoration: none;
  }

  .teach-card__img {
    flex-shrink: 0;
    width: 200px;
    height: 150px;
    border-radius: 10px;
    overflow: hidden;
    background: linear-gradient(135deg, #eef4ff, #f8fafc);
  }
  .teach-card__img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }
  .teach-card:hover .teach-card__img img {
    transform: scale(1.05);
  }
  /* Placeholder icon for cards without images */
  .teach-card__img--icon {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    color: #94a3b8;
  }

  .teach-card__body { flex: 1; min-width: 0; }
  .teach-card__header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 0.25rem;
  }
  .teach-card__org {
    font-weight: 650;
    font-size: 1rem;
    color: #1a1a2e;
    line-height: 1.4;
  }
  .teach-card__meta {
    font-size: 0.8rem;
    color: #718096;
    flex-shrink: 0;
    text-align: right;
    white-space: nowrap;
  }
  .teach-card__role {
    font-size: 0.88rem;
    color: #2a7ae2;
    font-weight: 500;
    margin-bottom: 0.5rem;
  }
  .teach-card__desc {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .teach-card__desc li {
    font-size: 0.85rem;
    color: #4a5568;
    line-height: 1.6;
    padding-left: 1.1rem;
    position: relative;
    margin-bottom: 0.25rem;
  }
  .teach-card__desc li::before {
    content: '';
    position: absolute;
    left: 0; top: 0.6em;
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #2a7ae2;
    opacity: 0.45;
  }
  .teach-card__link {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.78rem;
    color: #2a7ae2;
    margin-top: 0.5rem;
    font-weight: 500;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .teach-content { font-size: 0.9rem; }
    .teach-content .philosophy { padding: 1.2rem 1.3rem; font-size: 0.9rem; }
    .teach-content .philosophy::before { font-size: 3.5rem; }
    .teach-card__img { width: 160px; height: 120px; }
    .teach-card { gap: 1rem; }
  }
  @media (max-width: 600px) {
    .teach-card { flex-direction: column; }
    .teach-card__img { width: 100%; height: 180px; }
    .teach-card__header { flex-direction: column; gap: 0.2rem; }
    .teach-card__meta { text-align: left; }
  }
  @media (max-width: 400px) {
    .teach-content .philosophy { padding: 1rem; margin-bottom: 1.5rem; }
    .teach-card__img { height: 140px; }
  }
</style>

<div class="teach-content">

<div class="philosophy">
My teaching philosophy is grounded in the belief that language acquisition is most effective when it is data-informed, authentic, and technologically empowered. Drawing on my research in Informal Digital Learning of English (IDLE) and AI-assisted self-directed learning, I aim to transition students from passive recipients of knowledge to active, autonomous learners who can navigate real-world linguistic challenges.
</div>

<h2>Teaching Experience</h2>

<!-- EDCI 612 -->
<a class="teach-card" href="https://www.purdue.edu/catalog/graduate/colleges-schools-programs/education/curriculum-instruction/edci.html" target="_blank">
  <div class="teach-card__img">
    <img src="/images/teaching/edci612-speakers.png" alt="EDCI 612 Guest Lecture speakers">
  </div>
  <div class="teach-card__body">
    <div class="teach-card__header">
      <span class="teach-card__org">Purdue University</span>
      <span class="teach-card__meta">Feb 2026 &middot; West Lafayette, IN</span>
    </div>
    <div class="teach-card__role">Guest Lecturer, EDCI 612: AI and Multilingual Learners</div>
    <ul class="teach-card__desc">
      <li>Co-presented with Dr. Victoria Lowell and Belle Li on GenAI research and language education, covering learning analytics, AI tutors, and instructional design implications for multilingual learners.</li>
    </ul>
    <span class="teach-card__link">View course details &rarr;</span>
  </div>
</a>

<!-- University of Silesia -->
<a class="teach-card" href="https://us.edu.pl/en/" target="_blank">
  <div class="teach-card__img teach-card__img--icon">
    🇵🇱
  </div>
  <div class="teach-card__body">
    <div class="teach-card__header">
      <span class="teach-card__org">University of Silesia</span>
      <span class="teach-card__meta">Oct 2023 &ndash; Jun 2024 &middot; Katowice, Poland</span>
    </div>
    <div class="teach-card__role">Lecturer, Institute of Linguistics</div>
    <ul class="teach-card__desc">
      <li>Developed and delivered targeted lessons on Spoken Chinese and Academic Writing. Designed weekly online and in-person oral Chinese tests and graded assignments with scaffolding feedback via email.</li>
      <li>Instructed 200+ Chinese learners from diverse international backgrounds, enhancing their academic communication and presentation skills.</li>
      <li>Reported monthly and semester reports on students' performance using SPSS and Prism.</li>
    </ul>
    <span class="teach-card__link">Visit university &rarr;</span>
  </div>
</a>

<!-- Northeastern University -->
<a class="teach-card" href="http://www.neu.edu.cn/" target="_blank">
  <div class="teach-card__img teach-card__img--icon">
    🇨🇳
  </div>
  <div class="teach-card__body">
    <div class="teach-card__header">
      <span class="teach-card__org">Northeastern University</span>
      <span class="teach-card__meta">Feb &ndash; Jul 2023 &middot; Shenyang, China</span>
    </div>
    <div class="teach-card__role">Teaching Assistant</div>
    <ul class="teach-card__desc">
      <li>Instructed 100+ undergraduates in oral interpreting techniques, focusing on pronunciation, coherence, and public speaking in real-world contexts.</li>
      <li>Collected and analyzed student performance data using SPSS to track progress and provide personalized, data-informed feedback.</li>
      <li>Rated weekly, monthly, and semester-long interpreting tests using Audacity for detailed speech analysis and scoring.</li>
    </ul>
    <span class="teach-card__link">Visit university &rarr;</span>
  </div>
</a>

<!-- TAL Education -->
<a class="teach-card" href="https://en.100tal.com/" target="_blank">
  <div class="teach-card__img teach-card__img--icon">
    📚
  </div>
  <div class="teach-card__body">
    <div class="teach-card__header">
      <span class="teach-card__org">TAL Education Group</span>
      <span class="teach-card__meta">Feb 2021 &ndash; Jan 2022 &middot; Chengdu, China</span>
    </div>
    <div class="teach-card__role">Lecturer, English Department</div>
    <ul class="teach-card__desc">
      <li>Taught spoken English and presentation strategies to 500+ elementary and high school students, focusing on fluency, pronunciation, and confidence-building.</li>
      <li>Conducted informal assessments of students' speaking abilities and provided personalized feedback to foster oral improvement.</li>
      <li>Organized English speech contests and coached students, leading to multiple regional and school-level awards, including the national FLTRP ETIC Cup.</li>
    </ul>
    <span class="teach-card__link">Visit TAL Education &rarr;</span>
  </div>
</a>

</div>
