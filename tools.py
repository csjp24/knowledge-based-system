from __future__ import annotations

from dataclasses import dataclass
import re
from typing import List


@dataclass
class ToolResult:
    tool_name: str
    output: str
    rules_used: List[str]


def sensory_distress_check(context: str) -> ToolResult:
    output = (
        "The setting may be too much right now. Move to a quieter place if possible. "
        "Lower noise and bright light. Do not start social coaching yet."
    )
    return ToolResult("Sensory_Distress_Check", output, ["R4", "R11"])


def step_chunker(task: str) -> ToolResult:
    output = (
        "Break the task into one small part. Give only the first part now. "
        "Wait until it is finished before giving the next part."
    )
    return ToolResult("Step_Chunker", output, ["R1", "R2", "R3"])


def social_cue_breakdown(scenario: str) -> ToolResult:
    output = (
        "Explain the social cue in simple parts: what happened, what the other person may feel, "
        "and one better response to try next time."
    )
    return ToolResult("Social_Cue_Breakdown", output, ["R1", "R7", "R10"])


def transition_support(current_topic: str, next_topic: str) -> ToolResult:
    output = (
        f"First acknowledge the current topic: 'Yes, I heard you about {current_topic}.' "
        f"Then give one clear next step: 'Now we will talk about {next_topic}.'"
    )
    return ToolResult("Transition_Support", output, ["R1", "R2", "R8"])


def hyperfixation_redirect(topic: str, next_topic: str, stuck: bool = False) -> ToolResult:
    if stuck:
        output = (
            "Acknowledge the topic once. Do not force the change. "
            "Stop the session and try again another day."
        )
        return ToolResult("Hyperfixation_Redirect", output, ["R5", "R8", "R9"])

    output = (
        f"Say: 'Yes, your point about {topic} is correct.' "
        f"Then say: 'Now let's talk about {next_topic}.'"
    )
    return ToolResult("Hyperfixation_Redirect", output, ["R1", "R8"])


def meltdown_calm_protocol(safety_risk: bool = False) -> ToolResult:
    if safety_risk:
        output = (
            "Stay calm. Reduce stimulation. Get caregiver support immediately because there may be harm risk. "
            "Do not give a long explanation now."
        )
        return ToolResult("Meltdown_Calm_Protocol", output, ["R4", "R5", "R6", "R11"])

    output = (
        "Stay calm. Do not yell or force. Give space for safe self-regulation. "
        "Explain only after the person is calm."
    )
    return ToolResult("Meltdown_Calm_Protocol", output, ["R5", "R6", "R7", "R11"])


def output_simplifier(text: str) -> ToolResult:
    compact_text = re.sub(r"\s+", " ", text).strip()
    sentences = re.findall(r"[^.!?]+[.!?]['\"]?|[^.!?]+$", compact_text)
    short = " ".join(sentence.strip() for sentence in sentences[:4] if sentence.strip())
    return ToolResult("Output_Simplifier", short, ["R1"])
