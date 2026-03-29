---
layout: single
title: "Research & Publications"
permalink: /publications/
author_profile: true
---

<style>
  .pub-page { font-size: 0.95rem; line-height: 1.75; }
  .pub-page h2 {
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: #2a7ae2;
    margin-top: 2.2rem; margin-bottom: 1rem;
    padding-bottom: 0.4rem; border-bottom: 2px solid #eef4ff;
  }
  .pub-page .research-stmt {
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
  .pub-page .research-stmt:hover {
    box-shadow: 0 4px 24px rgba(99,102,241,.1);
    border-color: rgba(139,92,246,.2);
  }
  .pub-page .research-stmt::before {
    content: "\201C";
    position: absolute;
    top: -0.1rem; left: 0.8rem;
    font-size: 3.5rem;
    font-family: Georgia, serif;
    color: rgba(139,92,246,.12);
    line-height: 1;
  }
  .pub-page .research-stmt::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899, #f59e0b);
    opacity: 0;
    transition: opacity .4s;
  }
  .pub-page .research-stmt:hover::after {
    opacity: 1;
  }
  .pub-page .stats {
    font-size: 0.85rem; color: #718096; margin-bottom: 1.5rem;
  }

  /* ===== Publication card with thumbnail (Young-Ho Kim style) ===== */
  .pub-card {
    display: flex;
    gap: 1.2rem;
    padding: 1.1rem;
    margin-bottom: 0.8rem;
    border: 1px solid #e8edf5;
    border-radius: 12px;
    background: #fff;
    transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
    text-decoration: none;
    color: inherit;
    align-items: flex-start;
  }
  .pub-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    border-color: #2a7ae2;
    color: inherit;
  }

  /* Thumbnail */
  .pub-card__thumb {
    flex-shrink: 0;
    width: 120px;
    height: 85px;
    border-radius: 8px;
    overflow: hidden;
    background: #f0f4f8;
  }
  .pub-card__thumb img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s;
  }
  .pub-card:hover .pub-card__thumb img { transform: scale(1.05); }

  /* Placeholder thumbnail with emoji */
  .pub-card__thumb--icon {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    background: linear-gradient(135deg, #eef4ff, #f8fafc);
    color: #94a3b8;
  }

  .pub-card__body { flex: 1; min-width: 0; }
  .pub-card__top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 0.6rem;
    margin-bottom: 0.2rem;
  }
  .pub-card__title {
    font-weight: 600;
    font-size: 0.92rem;
    color: #1a1a2e;
    line-height: 1.4;
    flex: 1;
  }

  /* Badges */
  .pub-card__badges { display: flex; gap: 0.3rem; flex-wrap: wrap; flex-shrink: 0; }
  .pub-badge {
    font-size: 0.65rem;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    white-space: nowrap;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }
  .pub-badge--q1 { background: #dcfce7; color: #16a34a; }
  .pub-badge--q2 { background: #dbeafe; color: #2563eb; }
  .pub-badge--ur { background: #fef3c7; color: #d97706; }
  .pub-badge--upcoming { background: #ede9fe; color: #7c3aed; }
  .pub-badge--pdf { background: #fee2e2; color: #dc2626; }
  .pub-badge--doi { background: #dbeafe; color: #2563eb; }
  .pub-badge--web { background: #d1fae5; color: #059669; }

  .pub-card__authors {
    font-size: 0.8rem;
    color: #718096;
    margin-bottom: 0.15rem;
  }
  .pub-card__venue {
    font-size: 0.8rem;
    color: #4a5568;
    font-style: italic;
    margin-bottom: 0.2rem;
  }
  .pub-card__excerpt {
    font-size: 0.78rem;
    color: #94a3b8;
    line-height: 1.45;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .pub-page { font-size: 0.9rem; }
    .pub-page .research-stmt { padding: 1.2rem 1.3rem; font-size: 0.9rem; }
    .pub-page .research-stmt::before { font-size: 3.5rem; }
    .pub-card { padding: 0.9rem; }
    .pub-card__top { flex-wrap: wrap; }
    .pub-card__badges { flex-wrap: wrap; }
  }
  @media (max-width: 600px) {
    .pub-card { flex-direction: column; }
    .pub-card__thumb { width: 100%; height: 140px; }
    .pub-card__top { flex-direction: column; gap: 0.4rem; }
    .pub-card__badges { justify-content: flex-start; }
  }
  @media (max-width: 400px) {
    .pub-page .research-stmt { padding: 1rem; margin-bottom: 1.5rem; }
    .pub-card { padding: 0.7rem; gap: 0.8rem; }
    .pub-card__title { font-size: 0.85rem; }
    .pub-card__authors, .pub-card__venue { font-size: 0.75rem; }
  }
</style>

<div class="pub-page">

<div class="research-stmt">
I study how emerging technologies transform education beyond the classroom. My work centers on AI-assisted self-directed learning and IDLE, aiming to design authentic learning pathways that bridge the gap between theoretical knowledge and real-world application.
</div>

<p class="stats">
  <a href="{{ site.author.googlescholar }}">Google Scholar</a> &middot; Citation: 48 &middot; h-index: 2
</p>

<h2>Peer-Reviewed Journal Articles</h2>

<a class="pub-card" href="/publication/2026-doubao-genai-efl">
  <div class="pub-card__thumb">
    <img src="/images/pubs/doubao-model.jpg" alt="AI-Human Collaborative Model">
  </div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Doubao as a GenAI Scaffold in Senior High School EFL Writing</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--q2">Q2</span>
        <span class="pub-badge pub-badge--pdf">PDF</span>
      </div>
    </div>
    <div class="pub-card__authors">Wang, S. & <strong>*Tan, L.</strong> (2026)</div>
    <div class="pub-card__venue">Psicologia Educativa, 14, 19–33</div>
    <div class="pub-card__excerpt">Mixed-methods case study with 90 EFL students using Doubao for AI-assisted writing feedback.</div>
  </div>
</a>

<a class="pub-card" href="/publication/2025-two-years-innovation">
  <div class="pub-card__thumb">
    <img src="/images/pubs/two-years-growth.jpg" alt="Publication growth chart">
  </div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Two Years of Innovation: A Systematic Review of Empirical GenAI Research in Language Learning</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--q1">Q1</span>
        <span class="pub-badge pub-badge--pdf">PDF</span>
        <span class="pub-badge pub-badge--doi">DOI</span>
      </div>
    </div>
    <div class="pub-card__authors">Li, B., <strong>*Tan, L.Y.</strong>, Wang, C., & Lowell, V. (2025)</div>
    <div class="pub-card__venue">Computers and Education: AI, 9, 100445 &middot; IF &asymp; 10.5</div>
    <div class="pub-card__excerpt">PRISMA systematic review of 144 articles on GenAI in language learning (2023–2024).</div>
  </div>
</a>

<a class="pub-card" href="/publication/2025-pointing-to-context">
  <div class="pub-card__thumb">
    <img src="/images/pubs/mjss-cover.jpg" alt="Human vs Machine Interpreting">
  </div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Pointing to Context from a Relevance Theory Perspective: Human vs. Machine Interpreting</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--pdf">PDF</span>
        <span class="pub-badge pub-badge--doi">DOI</span>
      </div>
    </div>
    <div class="pub-card__authors"><strong>*Tan, L.Y.</strong> & Gao, L. (2025)</div>
    <div class="pub-card__venue">Mediterranean Journal of Social Sciences, 16(3), 1</div>
    <div class="pub-card__excerpt">Quasi-experimental study comparing context-awareness via Coh-Metrix across 108 linguistic indices.</div>
  </div>
</a>

<a class="pub-card" href="/publication/2023-clil-translation">
  <div class="pub-card__thumb"><img src="/images/pubs/clil-cover.png" alt="CLIL paper"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Study on MTI Talent Cultivation Mode from the Perspective of CLIL</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--doi">DOI</span>
      </div>
    </div>
    <div class="pub-card__authors">Gao, L. & <strong>*Tan, Y.</strong> (2023)</div>
    <div class="pub-card__venue">Education Advances, 13(12), 10029–10034</div>
    <div class="pub-card__excerpt">CLIL-inspired reforms for Master of Translation and Interpreting programs.</div>
  </div>
</a>

<h2>Under Review</h2>

<a class="pub-card" href="/publication/ur-tutor-not-solver">
  <div class="pub-card__thumb"><img src="/images/pubs/petechat-v2.png" alt="PeteChat interface"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Scaffolding over Shortcuts: Building a Safety-Aware LLM Tutoring System for University Contexts</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--ur">Under Review</span>
      </div>
    </div>
    <div class="pub-card__authors">Li, B., <strong>*Tan, L.</strong>, & Zakharov, W.</div>
    <div class="pub-card__excerpt">Design case of PeteChat: an LLM-powered AI tutor with RAG pipeline and guardrails at Purdue.</div>
  </div>
</a>

<a class="pub-card" href="/publication/ur-tpack-xinjiang">
  <div class="pub-card__thumb"><img src="/images/pubs/tpack-model.png" alt="TPACK Framework"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">How Ethnic and Cultural Context Shapes Technology Integration Knowledge Among Trainee Teachers in Western China</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--ur">Under Review</span>
      </div>
    </div>
    <div class="pub-card__authors">Liu, H. & <strong>*Tan, L.</strong></div>
    <div class="pub-card__venue">The Asia-Pacific Education Researcher</div>
  </div>
</a>

<a class="pub-card" href="/publication/ur-authorship-agency-ai">
  <div class="pub-card__thumb"><img src="/images/pubs/authorship-ai-loop.png" alt="AI Authenticity Loop diagram"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Whose Words Are These? University Faculty Perspectives on Originality and AI-Mediated Composition</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--ur">Under Review</span>
      </div>
    </div>
    <div class="pub-card__authors">Li, B. & <strong>*Tan, L.</strong></div>
    <div class="pub-card__venue">Education Science</div>
  </div>
</a>

<h2>Conference Presentations</h2>

<a class="pub-card" href="/publication/2026-aera-meta-analysis">
  <div class="pub-card__thumb"><img src="/images/pubs/meta-analysis-cover.png" alt="Meta-analysis cover slide"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">A Meta-analysis on the Achievement of Technology on Students from Low-income Families</span>
      <div class="pub-card__badges">
        <span class="pub-badge pub-badge--upcoming">Upcoming</span>
      </div>
    </div>
    <div class="pub-card__authors"><strong>*Tan, L.</strong>, Lowell, V. & Li, B. (2026, Apr)</div>
    <div class="pub-card__venue">AERA International Convention, Los Angeles, CA</div>
  </div>
</a>

<a class="pub-card" href="/publication/2026-clawdbot-unboxed">
  <div class="pub-card__thumb"><img src="/images/pubs/clawdbot-poster.jpg" alt="Clawdbot Unboxed poster"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Clawdbot Unboxed: What It Does, Why It's Hot, and Where It Breaks</span>
    </div>
    <div class="pub-card__authors"><strong>Tan, L.</strong> (2026, Feb)</div>
    <div class="pub-card__venue">AI Lunch and Learn Series, Purdue College of Education</div>
  </div>
</a>

<a class="pub-card" href="/publication/2025-purdue-ai-gai">
  <div class="pub-card__thumb">
    <img src="/images/service/ai-p12.png" alt="Purdue AI Conference presentation">
  </div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Assessing the Effects of Extramural GAI-mediated IDLE on Pragmatic Competence</span>
    </div>
    <div class="pub-card__authors"><strong>Tan, L.</strong>, Lowell, V. & Li, B. (2025, Nov)</div>
    <div class="pub-card__venue">Purdue AI in P-12 Conference, West Lafayette, IN</div>
  </div>
</a>

<a class="pub-card" href="/publication/2025-aect-authenticity">
  <div class="pub-card__thumb"><img src="/images/pubs/aect-authenticity.png" alt="AI vs. Authenticity"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Artificial Authenticity and Academic Integrity in an Age of Generative AI</span>
    </div>
    <div class="pub-card__authors">Li, B., Wang, J., & <strong>Tan, L.</strong> (2025, Oct)</div>
    <div class="pub-card__venue">AECT International Convention, Las Vegas, NV</div>
  </div>
</a>

<a class="pub-card" href="/publication/2024-call-context">
  <div class="pub-card__thumb"><img src="/images/pubs/call-tokyo.png" alt="CALL Conference Tokyo"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Pointing to Context (CALL Conference, Tokyo)</span>
    </div>
    <div class="pub-card__authors"><strong>Tan, L.</strong> (2024, Sep)</div>
    <div class="pub-card__venue">XXIInd International CALL Conference, Tokyo, Japan</div>
  </div>
</a>

<a class="pub-card" href="/publication/2024-sociocultural-ai">
  <div class="pub-card__thumb"><img src="/images/pubs/sociocultural-zpd.png" alt="ZPD diagram"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">Exploring the Extracurricular Development of AI-Assisted English Learners</span>
    </div>
    <div class="pub-card__authors"><strong>Tan, L.</strong> & Zhang, Y. (2024, May)</div>
    <div class="pub-card__venue">3rd International Conference on Sociocultural Theory, Guangdong, China</div>
  </div>
</a>

<a class="pub-card" href="/publication/2024-intercultural-pragmatics">
  <div class="pub-card__thumb"><img src="/images/pubs/intercultural-pisa.png" alt="Intercultural Pragmatics Conference group photo"></div>
  <div class="pub-card__body">
    <div class="pub-card__top">
      <span class="pub-card__title">10th International Conference on Intercultural Pragmatics and Communication</span>
    </div>
    <div class="pub-card__authors"><strong>Tan, L.</strong> (2024, May–Jun)</div>
    <div class="pub-card__venue">Pisa, Italy</div>
  </div>
</a>

</div>
