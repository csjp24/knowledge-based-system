# ASD Social Cue Training Agent

This repository contains a Knowledge-Based Systems (KBS) assignment project for designing an Agentic AI assistant that supports individuals with Autism Spectrum Disorder (ASD) in social cue training.

The project follows the GDVRR Protocol: Generate, Deconstruct, Verify, Rewrite, Reflect. It focuses on mapping human expert knowledge into a deterministic AI support system.

## Assignment Overview

This project was developed for the Knowledge-Based Systems course.

The objective is to:

- Extract knowledge from a real human expert.
- Transform declarative and procedural knowledge into an Agentic AI architecture.
- Audit AI reasoning using the GDVRR protocol.
- Reduce cognitive offloading by forcing human verification of AI logic.

The selected domain is:

> Autism Spectrum Disorder (ASD) Social Cue Training

## Human Expert Knowledge Source

The knowledge base was derived from a structured interview with:

- Dr. Atiyah

The extracted knowledge includes:

- Social communication guidance
- Sensory distress handling
- Meltdown response support
- Hyperfixation management
- Task chunking strategies
- Transition assistance

The system does not invent clinical rules independently. All rules are mapped from expert-derived guidance into deterministic tool-routing logic.

## System Characteristics

The AI assistant is designed to communicate in a:

- Calm
- Structured
- Direct
- Predictable
- Non-judgmental

manner suitable for ASD support interactions.

## Main Procedural Tools

The system contains the following expert-derived tools:

- `Sensory_Distress_Check`
- `Step_Chunker`
- `Social_Cue_Breakdown`
- `Transition_Support`
- `Hyperfixation_Redirect`
- `Meltdown_Calm_Protocol`
- `Output_Simplifier`

## Technologies Used

- Python 3.10+
- JSON knowledge base
- Rule-based tool routing
- Deterministic decision logic

## Project Structure

```text
asd_social_cue_agent/
|
├── knowledge_base.json
├── tools.py
├── agent.py
├── sample_scenarios.json
|
├── traces/
|   ├── sample_trace_before_rewrite.md
|   └── sample_trace_after_rewrite.md
|
└── README.md
```

## How To Run

### 1. Clone Repository

```bash
git clone https://github.com/csjp24/knowledge-based-system.git
```

### 2. Open Project Folder

```bash
cd knowledge-based-system
```

If the files are inside an `asd_social_cue_agent` subfolder, open that folder first:

```bash
cd asd_social_cue_agent
```

### 3. Run the Agent

```bash
python agent.py
```

## Expected Output

The system executes sample ASD support scenarios and displays:

1. User scenario input
2. Verbose reasoning trace
3. Tool-routing decisions
4. Final assistant response

The verbose trace supports GDVRR auditing and verification.

## Sample Scenario Mapping

Each member can audit one scenario for the individual Table 1 component:

| Member | Scenario | Focus |
|---|---|---|
| Donny | S1 | Sensory priority conflict |
| Corina | S2 | Hyperfixation and refusal to move on |
| Safiah | S4 | Meltdown support sequence |
| Hifzi | S5 | Long instructions and communication style |
| Dayang | S3 | Task transition and step chunking |

## GDVRR Protocol Support

This repository supports all GDVRR phases:

| Phase | Implementation |
|---|---|
| Generate | Scenario execution from `sample_scenarios.json` |
| Deconstruct | Verbose execution trace from `agent.py` |
| Verify | KBS anomaly analysis in the trace files |
| Rewrite | Prompt, rule, or tool correction |
| Reflect | Human oversight discussion in individual Table 1 |

## Trace Files

The `traces` folder contains:

- `sample_trace_before_rewrite.md`: problematic traces for all five members.
- `sample_trace_after_rewrite.md`: corrected traces after applying the GDVRR rewrite.

These files help each member explain what the AI did wrong, which expert rule was violated, and how the rewrite fixed the issue.

## Academic Integrity Note

The assignment prohibits using generative AI to create the initial expert knowledge base.

The declarative rules, procedural tools, and system constraints included in this project are assumed to originate from the human expert interview and lecturer-approved elicitation process.

Before submission, all placeholders and rule wording should be verified using the actual interview transcript or supporting evidence.

## Disclaimer

This project is developed strictly for educational and academic purposes only.

It is not intended to replace professional diagnosis, therapy, or medical advice.

