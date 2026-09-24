---
title: "Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat"
collection: publications
permalink: /publication/2026-tutor-not-solver
excerpt: 'A design-based research case of PeteChat, a locally hosted, course-aligned AI tutor at Purdue University. A 284-message baseline analysis and four expert sessions inform eight design principles for assessment-aware AI tutors.'
date: 2026-04-27
venue: 'arXiv preprint (cs.HC)'
publication_type: "preprint"
paperurl: 'https://arxiv.org/abs/2606.09845'
authors: 'Li, B., <strong>*Tan, L.</strong>, Zakharov, W., Qiu, Q., & Acton, C.'
badge: 'Preprint'
citation: 'Li, B., *Tan, L., Zakharov, W., Qiu, Q., & Acton, C. B. (2026). Tutor, not solver: Designing a guardrailed AI assistant for learning in higher education: A design case of PeteChat. <i>arXiv</i>. https://arxiv.org/abs/2606.09845'
---

![Figure 1. From generic answer bots to a guardrailed, course-aligned tutor](/images/pubs/petechat-arxiv-positioning.jpg)
*Figure 1. Motivating problems, core design tensions, and the conceptual positioning of PeteChat as a guardrailed, course-aligned tutor.*

**At a glance:** 284 baseline messages · 31 conversations · 3 task contexts · κ = .82 · 4 expert sessions · 8 design decisions · 8 design principles

**Links:** [arXiv:2606.09845](https://arxiv.org/abs/2606.09845) · [PDF](https://arxiv.org/pdf/2606.09845) · Preprint, 16 pages, with appendices on interview protocol, second-prototype interface states, and baseline coding tables.

---

## Abstract

Generative AI tutors hold significant promise for higher education, yet designing systems that scaffold learning without undermining academic integrity remains an open design challenge. This paper presents PeteChat, a course-aligned AI tutor developed and deployed at Purdue University, documented through the lens of design-based research (DBR). Drawing on literature-informed design inputs, a pre-deployment baseline analysis of authentic student-system interactions, and formative expert evaluation with teaching assistants and UX/developer stakeholders, we report eight transferable design principles for assessment-aware AI tutors: from homework guardrails and debugging scaffolds to self-regulated learning support and instructor-facing customization tools. The system is built on a locally hosted Llama-3 model enhanced with retrieval-augmented generation (RAG) grounded in course-specific materials. Rather than reporting controlled experimental outcomes, this design case foregrounds the situated design reasoning, iterative refinement, and principled decision-making that shaped PeteChat across multiple development phases. The resulting principles and methodological approach offer actionable guidance for institutions seeking to deploy responsible, integrity-preserving AI tutors at scale.

**Index terms:** generative AI; educational chatbot; design-based research; self-regulated learning; academic integrity; retrieval-augmented generation; higher education

---

## Research Questions

1. What design principles emerge for AI tutors that scaffold learning without undermining academic integrity?
2. How can self-regulated learning (SRL) theory be operationalized in AI-mediated dialogue?
3. What institutional constraints shape AI tutor design in practice?

---

## Design-Based Research Across Four Phases

![Figure 2. The DBR cycle guiding PeteChat](/images/pubs/petechat-arxiv-dbr.png)
*Figure 2. Needs analysis, design, evaluation, and development form an outer loop of information flow, while an inner classroom data loop feeds authentic usage evidence back to every phase.*

The project is reported as a design case rather than an outcome study. Each semester of pilot use constituted one design cycle. Chronologically, the work unfolded in four project phases; the paper marks the DPO alignment and cross-course deployment phases as anticipatory (see Limitations).

| Phase | Period | Focus |
|:--|:--|:--|
| 1 | Summer to Fall 2024 | Course-specific data collection, baseline tutor, fine-tuning of open-source LLMs (beginning with Llama-3) on Purdue’s Gilbreth cluster |
| 2 | Fall 2024 to Spring 2025 | First deployment to undergraduates in ECE 20875 through Gradio/Hugging Face |
| 3 | Spring to Summer 2025 | Direct Preference Optimization to align response style and scaffolding with student preferences |
| 4 | Spring 2026 | Extension to additional large undergraduate Python programming courses |

---

## Evidence Base Before the Redesign

Before the guardrails and SRL scaffolds were built, the team analyzed all interactions logged during a pre-guardrail deployment in ECE 20875 (Fall 2025): 284 messages from 31 conversations across exam preparation, homework debugging, and an open-ended mini-project. Messages were coded with a dual-family scheme (10 student SRL codes grounded in Zimmerman’s three-phase model; 9 system-alignment codes). A second coder independently coded 60 messages (21.1% of the corpus), yielding Cohen’s κ = .82.

Three design pressures emerged:

- **Boundary and answer control.** Direct answer seeking appeared in 7.0% of student messages, and boundary testing reached 13.4% overall and 22.0% in the homework context. The baseline system sometimes complied with direct-solution requests.
- **Grounding and freshness.** Stale or incorrect course information appeared, and 29.6% of system output was generic or non-instructional.
- **SRL visibility.** Hint utilization was not observed, and self-evaluation appeared in only two messages (1.4%). SRL scaffolds therefore became a design necessity rather than a theoretical aspiration.

These pressures were then triangulated with four formative expert sessions (two ECE 20875 teaching assistants, one software developer, one UX designer; 45 to 60 minutes each; IRB approved). Teaching assistants reported that heavy reliance on generic AI tools such as ChatGPT was inflating homework scores (often above 95%) while exam performance dropped, that unjustified regrade requests were a major time sink, and that students "are not reading anymore."

---

## System Architecture

![Figure 4. Overview of the PeteChat architecture](/images/pubs/petechat-arxiv-architecture.png)
*Figure 4. A mixture-of-experts-inspired router dispatches each query to exam generation, MCP tools, multimodal support, or RAG question answering. The RAG pipeline includes query rewriting, multimodal retrieval, shared-vector embedding, and generation under tutor guardrails.*

PeteChat runs on a locally hosted Llama-3 model, fine-tuned with parameter-efficient methods (LoRA/QLoRA) on syllabi, lecture notes, prior exams and solutions, and discussion-board Q&A shared with faculty permission. Course data are not exported for third-party fine-tuning. A continuously updated knowledge base supplies current announcements and clarifications, and the model is prompted to cite retrieved course sources and to express uncertainty rather than fabricate.

---

## Eight Design Principles

The principles emerged from the synthesis of the expert-session findings; each is tied to specific design decisions in the paper, several of which also draw on the baseline analysis. Principle wording follows Section XI of the paper.

| Principle | What PeteChat does |
|:--|:--|
| 1. Tutor, not solver | Default to hints and scaffolding and avoid direct answers; teach how to think through debugging explanations and step-by-step reasoning |
| 2. Align to the course | Ground responses in instructor-provided materials, show provenance, add freshness disclaimers for logistics |
| 3. Respect academic integrity | Guardrails and integrity reminders on homework; encourage students to read and follow instructions |
| 4. Reduce TA overhead | Instruction summaries, rubric-based regrade explanations before escalation, and consistent answers to repeat questions |
| 5. Design for clarity and momentum | Default-open sidebar with "Try asking..." prompts per assignment; concise, readable, visual answers |
| 6. Flexible control for staff | Instructor upload slots, per-course tone settings, alignment metrics without code |
| 7. Trust through transparency | Show sources, note uncertainty, offer share/confirm actions for verification with peers or TAs |
| 8. Time-aware support | Study planners and mock quizzes scoped to available time and upcoming exams |

---

## Limitations

The evidence base is formative rather than outcome validating: one course at one R1 university, one semester of baseline data, and four expert evaluators who overlap with the design team, which the authors note raises the potential for self-report bias; transferability remains to be tested. The SRL-aligned features are theoretically motivated but not yet validated against learning outcomes. Hallucination risk persists even with RAG grounding, and claims about the later phases (DPO alignment, cross-course deployment) are anticipatory pending dedicated reporting.

---

## Related Work on PeteChat

An invited Springer book chapter (in press), [From Answer Bot to Course Tutor](/publication/answer-bot-to-tutor), presents the practice-oriented design case for the same system. A related presentation, "A Design Case of PeteChat: Designing AI Tutors That Teach Students How to Think, Not What to Answer," is scheduled for the AECT International Convention, Chicago, October 2026.
