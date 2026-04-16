"""
CornScan AI · utils/report.py
Generates a plain-text PDF-style diagnosis report.
"""

import datetime


def generate_report(results: list) -> bytes:
    lines = []
    ts = datetime.datetime.now().strftime("%d %B %Y, %H:%M")
    lines += [
        "╔" + "═" * 60 + "╗",
        "║   CORNSCAN AI — APEX FIELD DIAGNOSIS REPORT v7.0          ║",
        "║   Deep Learning · CNN Plant Pathology · TensorFlow         ║",
        f"║   Generated: {ts:<44}║",
        "╚" + "═" * 60 + "╝", "",
    ]
    for i, r in enumerate(results, 1):
        info = r["info"]
        lines += [
            f"  SCAN #{i}  ·  {r['fname']}",
            f"  {'─' * 58}",
            f"  Diagnosis      : {info['short']}",
            f"  Pathogen       : {info['pathogen']}",
            f"  Confidence     : {r['conf'] * 100:.1f}%",
            f"  Severity       : {info['severity']}",
            f"  Risk Score     : {info['risk_score']}/100",
            f"  Yield Impact   : {info['yield_impact']}",
            f"  Spread Rate    : {info['spread_rate']}",
            f"  Timestamp      : {r['ts']}", "",
            "  ┌─ PROBABILITY BREAKDOWN ──────────────────────────────┐",
        ]
        for cls, p in r["all_probs"].items():
            bar = "█" * int(p * 30) + "░" * (30 - int(p * 30))
            lines.append(f"  │  {cls:<18} {bar} {p * 100:5.1f}%  │")
        lines.append("  └──────────────────────────────────────────────────────┘")
        lines += [
            "", "  DESCRIPTION", f"  {info['desc']}",
            "", "  3-DAY TREATMENT PLAN",
        ]
        for step in info["plan_3day"]:
            lines.append(f"  · {step}")
        lines += ["", "  7-DAY TREATMENT PLAN"]
        for step in info["plan_7day"]:
            lines.append(f"  · {step}")
        lines += ["", "  PREVENTION STRATEGY"]
        for step in info["prevention"]:
            lines.append(f"  · {step}")
        lines += [
            "", "  FARMER INTELLIGENCE", f"  {info['farmer_advice']}",
            "", "  EXPERT NOTE", f"  {info['expert_note']}",
            "", "  WEATHER TRIGGER", f"  {info['weather_trigger']}",
            "", "─" * 62, "",
        ]
    lines.append("  CornScan AI v7.0 APEX · No data leaves your device · For research use")
    return "\n".join(lines).encode("utf-8")
