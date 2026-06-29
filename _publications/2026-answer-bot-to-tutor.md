---
title: "From Answer Bot to Course Tutor: A Practical Design Case of a Guardrailed AI Assistant in Higher Education"
collection: publications
permalink: /publication/answer-bot-to-tutor
excerpt: 'A design case of PeteChat, a course-aligned, guardrailed AI tutor built to keep students reasoning within the course rather than handing them finished work.'
date: 2026-06-11
venue: 'Invited book chapter, Springer (in press)'
publication_type: "book chapter"
authors: 'Li, B., <strong>*Tan, L.</strong>, Zakharov, W., Qiu, Q., & Acton, C.'
badge: 'In Press'
---

![From Answer Bot to Course Tutor: PeteChat design story](/images/pubs/answer-bot-to-tutor.png)

*Invited book chapter, Springer (in press). Preprint available on arXiv: [arXiv:2606.09845](https://arxiv.org/abs/2606.09845).*

---

## Abstract

As public generative AI tools provide students with timely help, they may also produce information ungrounded in the course, complete assessed work on their behalf, and operate entirely outside instructors' oversight. In order to address this challenge, this chapter presents **PeteChat**, a course-aligned and guardrailed AI tutor developed at Purdue University for a high-enrollment undergraduate programming course, built to keep students reasoning within the course rather than to hand them finished work.

We examine how the design responded to three recurring instructional situations:

- supporting homework **without completing it**,
- providing reliable course logistics and clarification, and
- reducing repetitive teaching-assistant workload **without transferring academic judgment to the system**.

The case documents the design responses, tensions, and early failures involved in making assistance assessment-aware, grounded in visible course sources, and subject to human authority. Practically, it contributes to the design reasoning behind these choices, which other institutions can adapt to their own courses, assessment structures, and resources. Importantly, PeteChat is offered as a design precedent for a course-aligned AI tutor rather than a validated, universally applicable solution.

**Keywords:** Generative AI; course-aligned AI tutor; academic integrity; retrieval-augmented generation; design case; higher education; self-regulated learning

---

## The PeteChat Interface

![PeteChat interface with goal-setting and self-regulated learning scaffolds](/images/pubs/petechat-v2.png)

*The redesigned interface adds explicit learning goals, self-reflection prompts, and pedagogical scaffolds that steer students toward reasoning rather than answers.*

---

## How PeteChat Works

PeteChat is **not ChatGPT in a Purdue wrapper**. It is a purpose-built system with three layers:

**1. Course-Specific Knowledge (RAG Pipeline)**
The AI retrieves answers from verified course materials first — not from general internet knowledge. When a student asks about Python data structures in ECE 20875, PeteChat responds with content aligned to what their professor actually taught.

**2. Guardrails That Protect Learning**
When a student pastes a homework problem, PeteChat does not solve it. Instead, it asks: *"What have you tried so far?"* and *"Which part is confusing?"* — guiding them through the problem-solving process.

**3. Instructor Oversight**
Faculty can see what students are asking — not individual conversations, but patterns. If many students ask about recursion in the same week, the professor knows to revisit it in class.

---

## The "Scaffolding over Shortcuts" Principle in Action

| Student asks... | A public AI would say... | PeteChat says... |
|:---------------|:---------------------|:-----------------|
| "Write a for loop that sums a list" | `sum = 0; for x in lst: sum += x` | "What do you know about for loops? Let's start with the structure." |
| "What's the answer to Q3?" | [provides full solution] | "I can help you work through Q3. What's the first step you'd take?" |
| "Fix my code" | [rewrites the code] | "I see an issue on line 5. What do you think `range()` returns here?" |

---

## Why It Matters

Universities face a choice: ban AI tools (and lose) or integrate them thoughtfully. PeteChat demonstrates that **AI can enhance learning without replacing it** — but only when the design explicitly prioritizes pedagogy over convenience.
