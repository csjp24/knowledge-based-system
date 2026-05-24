from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

from tools import (
    ToolResult,
    hyperfixation_redirect,
    meltdown_calm_protocol,
    output_simplifier,
    sensory_distress_check,
    social_cue_breakdown,
    step_chunker,
    transition_support,
)


ROOT = Path(__file__).parent


@dataclass
class TraceStep:
    thought: str
    action: str
    observation: str
    rules_used: List[str]


class ASDSocialCueAgent:
    def __init__(self) -> None:
        self.kb = json.loads((ROOT / "knowledge_base.json").read_text(encoding="utf-8"))

    def respond(self, scenario: str) -> dict:
        text = scenario.lower()
        trace: List[TraceStep] = []
        tool_outputs: List[str] = []

        def call(thought: str, result: ToolResult) -> None:
            trace.append(
                TraceStep(
                    thought=thought,
                    action=result.tool_name,
                    observation=result.output,
                    rules_used=result.rules_used,
                )
            )
            tool_outputs.append(result.output)

        sensory_keywords = ["crowded", "bright", "noise", "noisy", "ears", "high-pitched", "cafeteria"]
        meltdown_keywords = ["screams", "cries", "tantrum", "meltdown", "drops to the floor"]
        harm_keywords = ["hurting", "hit", "hits", "self-harm", "harm"]
        fixation_keywords = ["keeps talking", "repeats", "again and again", "fixated", "same"]
        transition_keywords = ["move to", "next activity", "continue", "questions 4", "transition"]

        has_sensory = any(word in text for word in sensory_keywords)
        has_meltdown = any(word in text for word in meltdown_keywords)
        has_harm = any(word in text for word in harm_keywords) and "not hurting" not in text
        has_fixation = any(word in text for word in fixation_keywords)
        has_transition = any(word in text for word in transition_keywords)
        has_social_misunderstanding = any(
            word in text
            for word in ["classmate", "rude", "hello", "looks away", "flat tone", "social"]
        )
        stop_session = False

        if has_meltdown:
            call(
                "The user is emotionally distressed. Expert rules say calming and safety come before explanation.",
                meltdown_calm_protocol(safety_risk=has_harm),
            )

        if has_sensory:
            call(
                "The setting contains sensory triggers. Sensory regulation has priority over social cue training.",
                sensory_distress_check(scenario),
            )

        if has_fixation:
            stuck = "again and again" in text or "repeats" in text
            call(
                "The user may be in a repetitive loop. Use acknowledgement and gentle redirection; stop if stuck.",
                hyperfixation_redirect("the current topic", "the next activity", stuck=stuck),
            )
            stop_session = stuck

        if has_transition and not has_meltdown and not stop_session:
            current_topic = "questions 1 to 3" if "questions" in text else "the current topic"
            next_topic = "questions 4 to 6" if "questions" in text else "the next activity"
            call(
                "The scenario asks for a task or topic change. Use a structured transition.",
                transition_support(current_topic, next_topic),
            )

        if has_social_misunderstanding and not has_meltdown and not has_sensory and not stop_session:
            call(
                "Social misunderstanding can be explained after checking that the person is regulated.",
                social_cue_breakdown(scenario),
            )

        if "questions" in text and not stop_session:
            call(
                "The task contains multiple parts, so it should be chunked.",
                step_chunker("question set"),
            )

        combined = " ".join(tool_outputs)
        simplified = output_simplifier(combined)
        trace.append(
            TraceStep(
                thought="The final answer must be short and direct.",
                action=simplified.tool_name,
                observation=simplified.output,
                rules_used=simplified.rules_used,
            )
        )

        return {
            "final_response": simplified.output,
            "trace": [asdict(step) for step in trace],
        }


def run_demo() -> None:
    scenarios = json.loads((ROOT / "sample_scenarios.json").read_text(encoding="utf-8"))
    agent = ASDSocialCueAgent()

    for scenario in scenarios:
        result = agent.respond(scenario["scenario"])
        print("=" * 72)
        print(f"{scenario['id']}: {scenario['title']}")
        print(scenario["scenario"])
        print("\nTRACE")
        for index, step in enumerate(result["trace"], 1):
            print(f"{index}. Thought: {step['thought']}")
            print(f"   Action: {step['action']}")
            print(f"   Observation: {step['observation']}")
            print(f"   Rules: {', '.join(step['rules_used'])}")
        print("\nFINAL RESPONSE")
        print(result["final_response"])


if __name__ == "__main__":
    run_demo()
