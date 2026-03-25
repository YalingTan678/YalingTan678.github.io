---
title: "Scaffolding over Shortcuts: Building a Safety-Aware LLM Tutoring System for University Contexts"
collection: publications
permalink: /publication/ur-tutor-not-solver
excerpt: 'A design case documenting PeteChat, an LLM-powered AI tutor at Purdue University that scaffolds learning without undermining academic integrity.'
date: 2026-03-03
venue: 'Under Review'
publication_type: "journal"
authors: 'Li, B., <strong>*Tan, L.</strong>, & Zakharov, W.'
badge: 'Under Review'
---

## What This Paper Is About

Most AI chatbots give students **answers**. PeteChat is designed to give them **guidance**. This design case documents how we built an LLM-powered AI tutor at Purdue University that teaches students *how to think*, not *what to answer* — and what we learned along the way.

---

## PeteChat Interface Evolution

| Phase 1: Initial UI | Phase 2: Redesigned with SRL |
|:---:|:---:|
| ![PeteChat V1](/images/pubs/petechat-v1.png) | ![PeteChat V2](/images/pubs/petechat-v2.png) |
| *Identified critical UX issues* | *Added learning goals & scaffolding* |

---

## How PeteChat Works

PeteChat is **not ChatGPT in a Purdue wrapper**. It's a purpose-built system with three layers:

**1. Course-Specific Knowledge (RAG Pipeline)**
The AI retrieves answers from verified course materials first — not from general internet knowledge. This means when a student asks about Python data structures in ECE 20875, PeteChat responds with content aligned to what their professor actually taught.

**2. Guardrails That Protect Learning**
When a student pastes a homework problem, PeteChat doesn't solve it. Instead, it asks: *"What have you tried so far?"* and *"Which part is confusing?"* — guiding them through the problem-solving process.

**3. Instructor Dashboard**
Faculty can see what students are asking — not individual conversations, but patterns. If 40 students ask about recursion in the same week, the professor knows to revisit it in class.

---

## Design-Based Research: Four Phases

| Phase | What Happened | What We Learned |
|:------|:-------------|:----------------|
| **Phase 0** (Summer '24) | Built baseline tutor, fine-tuned Llama-3 on Purdue's cluster | Generic LLMs need heavy customization for education |
| **Phase 1** (Fall '24) | Deployed to 200+ students in ECE 20875 | Students wanted explanations, not answers — validating our approach |
| **Phase 2** (Spring '25) | Applied Direct Preference Optimization | Student feedback dramatically improved response quality |
| **Phase 3** (Spring '26) | Expanded to multiple Python courses | Moving from pilot to campus-wide integration |

---

## The "Scaffolding over Shortcuts" Principle in Action

| Student asks... | ChatGPT would say... | PeteChat says... |
|:---------------|:---------------------|:-----------------|
| "Write a for loop that sums a list" | `sum = 0; for x in lst: sum += x` | "What do you know about for loops? Let's start with the structure." |
| "What's the answer to Q3?" | [provides full solution] | "I can help you work through Q3. What's the first step you'd take?" |
| "Fix my code" | [rewrites the code] | "I see an issue on line 5. What do you think `range()` returns here?" |

---

## What Made This Work

- **$84,787 funding** from Purdue's Innovation Hub
- Collaboration with CIE, Purdue Libraries, and RCAC
- A "channel, don't ban" philosophy — students will use AI regardless; better to shape how
- Students told us they actually *preferred* guided help over direct answers — it reduced anxiety about "not really learning"

---

## Why It Matters

Universities face a choice: ban AI tools (and lose) or integrate them thoughtfully. PeteChat demonstrates that **AI can enhance learning without replacing it** — but only when the design explicitly prioritizes pedagogy over convenience.
