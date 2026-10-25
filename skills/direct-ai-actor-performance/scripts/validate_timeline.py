#!/usr/bin/env python3
"""Validate shot timing and estimate whether dialogue fits each beat."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def speech_seconds(text: str) -> float:
    chinese = len(re.findall(r"[\u4e00-\u9fff]", text))
    english_words = len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text))
    punctuation = len(re.findall(r"[\uff0c\u3002\uff01\uff1f\uff1b,.!?;\u2026]", text))
    return chinese / 4.5 + english_words / 2.4 + punctuation * 0.12


def validate(data: dict) -> dict:
    total = float(data.get("total_duration", 0))
    beats = data.get("beats") or data.get("shots") or []
    issues: list[dict] = []
    normalized = []
    previous_end = 0.0
    for index, beat in enumerate(beats, 1):
        start = float(beat.get("start", 0))
        end = float(beat.get("end", 0))
        duration = end - start
        label = beat.get("label") or f"beat-{index}"
        if duration <= 0:
            issues.append({"level": "error", "beat": label, "message": "End time must be later than start time"})
        if start < previous_end - 1e-6:
            issues.append({"level": "error", "beat": label, "message": f"Overlaps the previous beat by {previous_end - start:.2f}s"})
        elif start > previous_end + 0.15:
            issues.append({"level": "warning", "beat": label, "message": f"Unaccounted gap of {start - previous_end:.2f}s before this beat"})
        if start < 0 or (total and end > total + 1e-6):
            issues.append({"level": "error", "beat": label, "message": "Beat runs outside the total duration"})
        dialogue = str(beat.get("dialogue", ""))
        estimate = round(speech_seconds(dialogue), 2) if dialogue else 0.0
        available = max(0.0, duration - float(beat.get("reserved_action_seconds", 0)))
        if dialogue and estimate > available:
            issues.append({
                "level": "warning",
                "beat": label,
                "message": f"Dialogue estimated at {estimate:.2f}s exceeds the {available:.2f}s available; shorten the line or lengthen the beat",
            })
        normalized.append({"label": label, "start": start, "end": end, "duration": round(duration, 2), "speech_estimate": estimate})
        previous_end = max(previous_end, end)
    if total and previous_end < total - 0.15:
        issues.append({"level": "warning", "beat": "timeline", "message": f"{total - previous_end:.2f}s at the end is unaccounted for"})
    return {
        "valid": not any(i["level"] == "error" for i in issues),
        "total_duration": total,
        "beats": normalized,
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSON file containing total_duration and beats/shots")
    args = parser.parse_args()
    result = validate(json.loads(args.input.read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
