---
title: "Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education"
collection: publications
permalink: /publication/ur-tutor-not-solver
excerpt: 'A design case documenting PeteChat, an LLM-powered AI tutor at Purdue University that scaffolds learning without undermining academic integrity.'
date: 2026-03-03
venue: 'Under Review'
publication_type: "journal"
authors: 'Li, B., <strong>*Tan, L.</strong>, & Zakharov, W.'
badge: 'Under Review'
---

## PeteChat Interface

| Phase 1: Initial UI | Phase 2: Redesigned with SRL |
|:---:|:---:|
| ![PeteChat V1](/images/pubs/petechat-v1.png) | ![PeteChat V2](/images/pubs/petechat-v2.png) |
| *Identified critical UX issues* | *Added learning goals & scaffolding* |

## Overview

This design case documents the development and implementation of **PeteChat**, an LLM-powered learning assistant at Purdue University that serves as a "virtual teaching assistant" — designed to teach students *how to think*, not *what to answer*. The project follows a **design-based research (DBR)** approach with iterative refinement across multiple semesters.

## Research Questions

1. What design principles emerge for AI tutors that scaffold learning without undermining academic integrity?
2. How can **self-regulated learning (SRL) theory** be operationalized in AI-mediated dialogue?
3. What institutional constraints shape AI tutor design in practice?

## The PeteChat System

PeteChat is a course-aware AI assistant fine-tuned on curated Purdue course materials and aligned with instructional goals. Unlike generic AI tools, PeteChat incorporates:

- **Retrieval-Augmented Generation (RAG)** — grounding responses in verified course-specific content
- **Built-in guardrails** — prompting the model to refrain from giving away homework answers
- **Instructor-facing dashboard** — allowing faculty to monitor student questions and adjust teaching
- **Foldered chats by course topic** — mirroring syllabus structure for easy navigation

## Design-Based Research Phases

| Phase | Timeline | Focus |
|-------|----------|-------|
| **Phase 0** | Summer–Fall 2024 | Data collection, baseline tutor construction, fine-tuning Llama-3 on Purdue's Gilbreth cluster |
| **Phase 1** | Fall 2024–Spring 2025 | First large-scale deployment in ECE 20875 (undergraduate programming) |
| **Phase 2** | Spring–Summer 2025 | Direct Preference Optimization (DPO) to align with student preferences |
| **Phase 3** | Spring 2026 | Extension to additional large undergraduate Python courses |

## Key Design Principles

- **Scaffolding over answering**: The AI provides hints, asks guiding questions, and breaks down complex problems
- **Course-specific grounding**: Fine-tuned on institutional materials for accuracy and relevance
- **Privacy and integrity**: Institutional AI addresses student concerns about data privacy vs. public tools
- **Faculty oversight**: Instructor tools enable monitoring and curriculum adjustment based on student AI interactions

## Institutional Context

Supported by **Purdue's Innovation Hub Funding Program** ($84,787), in consultation with the Center for Instructional Excellence (CIE), Purdue Libraries, and RCAC (Rosen Center for Advanced Computing). The project reflects a "channel, don't ban" philosophy toward AI in higher education.

## Stakeholder Insights

- **Students** expressed frustration with generic AI answers and desired explanations over direct answers
- **Faculty** wanted visibility into student questions to preempt misconceptions and adjust teaching
- These inputs directly shaped PeteChat's design: course-scoped responses, explanation-focused dialogue, and instructor dashboards
