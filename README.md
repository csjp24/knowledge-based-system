# ASD Social Cue Training Agent

This repository is a Knowledge-Based Systems assignment scaffold for an Agentic AI assistant that supports individuals with Autism Spectrum Disorder (ASD) in social cue training.

The knowledge base is based on the group interview with Dr. Atiyah. The system does not invent clinical rules. It maps the expert-derived rules into deterministic tool-routing logic, then produces a verbose trace for GDVRR auditing.

## Assignment Components

- Domain: Autism Spectrum Disorder social cue training
- Expert source: Dr. Atiyah interview
- Agent style: clear, direct, calm, structured, and predictable
- Main tools:
  - Sensory_Distress_Check
  - Step_Chunker
  - Social_Cue_Breakdown
  - Transition_Support
  - Hyperfixation_Redirect
  - Meltdown_Calm_Protocol
  - Output_Simplifier

## How To Run

Use Python 3.10+.

```bash
python agent.py
```

The script runs the sample scenarios and prints:

1. The user scenario
2. The agent's verbose trace
3. The final assistant response

## Files

- `knowledge_base.json`: Expert-derived rules, tools, and system constraints.
- `tools.py`: Procedural knowledge tools.
- `agent.py`: Tool-routing logic and trace generation.
- `sample_scenarios.json`: Test cases for the Generate phase.
- `traces/sample_trace_before_rewrite.md`: Example problematic trace for audit.
- `traces/sample_trace_after_rewrite.md`: Corrected trace after applying rewrite logic.

## Important Academic Note

The assignment prohibits using AI to generate the initial knowledge base. This scaffold assumes the listed rules were extracted from the human expert interview. Before submission, replace or refine any rule wording using your actual interview transcript or lecturer-approved elicitation notes.

