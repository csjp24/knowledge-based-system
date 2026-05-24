# ASD Social Cue Training Agent

This repository contains a Knowledge-Based Systems (KBS) assignment project for designing an Agentic AI assistant that supports individuals with Autism Spectrum Disorder (ASD) in social cue training.

The project follows the GDVRR Protocol (Generate, Deconstruct, Verify, Rewrite, Reflect) and focuses on mapping human expert knowledge into a deterministic AI support system.


# Assignment Overview

This project was developed for the Knowledge-Based Systems course.

The objective is to:

- Extract knowledge from a real human expert
- Transform declarative and procedural knowledge into an Agentic AI architecture
- Audit AI reasoning using the GDVRR protocol
- Reduce cognitive offloading by forcing human verification of AI logic

The selected domain is:

> Autism Spectrum Disorder (ASD) Social Cue Training


# Human Expert Knowledge Source

The knowledge base was derived from a structured interview with:

- Dr. Atiyah

The extracted knowledge includes:

- social communication guidance
- sensory distress handling
- meltdown response support
- hyperfixation management
- task chunking strategies
- transition assistance

The system does not invent clinical rules independently. All rules are mapped from expert-derived guidance into deterministic tool-routing logic.


# System Characteristics

The AI assistant is designed to communicate in a:

- calm
- structured
- direct
- predictable
- non-judgmental

manner suitable for ASD support interactions.


# Main Procedural Tools

The system contains the following expert-derived tools:

- `Sensory_Distress_Check`
- `Step_Chunker`
- `Social_Cue_Breakdown`
- `Transition_Support`
- `Hyperfixation_Redirect`
- `Meltdown_Calm_Protocol`
- `Output_Simplifier`


# Technologies Used

- Python 3.10+
- JSON Knowledge Base
- Rule-Based Tool Routing
- Deterministic Decision Logic


# Project Structure

```text
asd_social_cue_agent/
│
├── knowledge_base.json
├── tools.py
├── agent.py
├── sample_scenarios.json
│
├── traces/
│   ├── sample_trace_before_rewrite.md
│   └── sample_trace_after_rewrite.md
│
└── README.md
```


# How To Run

## 1. Clone Repository

```bash
git clone https://github.com/csjp24/knowledge-based-system.git
```

## 2. Open Project Folder

```bash
cd knowledge-based-system
```

## 3. Run the Agent

```bash
python agent.py
```


# Expected Output

The system executes sample ASD support scenarios and displays:

1. User scenario input
2. Verbose reasoning trace
3. Tool-routing decisions
4. Final assistant response

The verbose trace supports GDVRR auditing and verification.


# GDVRR Protocol Support

This repository supports all GDVRR phases:

| Phase | Implementation |
|---|---|
| Generate | Scenario execution |
| Deconstruct | Verbose execution trace |
| Verify | KBS anomaly analysis |
| Rewrite | Prompt/tool correction |
| Reflect | Human oversight discussion |


# Academic Integrity Note

The assignment prohibits using generative AI to create the initial expert knowledge base.

The declarative rules, procedural tools, and system constraints included in this project are assumed to originate from the human expert interview and lecturer-approved elicitation process.

Before submission, all placeholders and rule wording should be verified using the actual interview transcript or supporting evidence.


# Disclaimer

This project is developed strictly for educational and academic purposes only.

It is not intended to replace professional diagnosis, therapy, or medical advice.
