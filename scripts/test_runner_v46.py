# -*- coding: utf-8 -*-
"""
scripts/test_runner_v46.py - SOTA Structured Validation Engine (v46.1)
Master orchestrator for Gênio LLM certification.
"""

import json
import time
import psutil
import subprocess
import os
import sys
from datetime import datetime
from pathlib import Path

# INDICATORS (Zero Emoji Policy)
INFO = "[INFO]"
OK = "[OK]"
ERR = "[ERR]"
SCAN = "[SCAN]"
STEP = "[STEP]"

TEST_MODULES = {
    "COUNCIL": "tests/validation/test_council_core.py",
    "CONFIG": "tests/validation/test_config_dna.py",
    "SAT": "tests/validation/test_active_agents.py",
    "MISSION": "tests/validation/test_specialist_soldiers.py",
    "LAB": "tests/validation/test_sensors_boosters.py"
}

class ValidationOrchestrator:
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "version": "v46.1",
            "system": "Genio LLM SOTA",
            "categories": {}
        }
        self.report_dir = Path(".panda/benchmarks")
        self.report_dir.mkdir(parents=True, exist_ok=True)

    def add_results(self, category, data):
        if category not in self.results["categories"]:
            self.results["categories"][category] = []
        
        if isinstance(data, list):
            self.results["categories"][category].extend(data)
        else:
            self.results["categories"][category].append(data)

    def generate_json_report(self):
        filename = f"validation_full_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_path = self.report_dir / filename
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        return report_path

    def generate_markdown_report(self):
        report_path = self.report_dir / "validation_v46_report.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# Genio LLM Validation Report - {self.results['timestamp']}\n\n")
            f.write(f"**Version:** {self.results['version']} | **Status:** PROOF OF QUALITY\n\n")
            
            for cat, tests in self.results["categories"].items():
                f.write(f"## [{cat}] {cat}\n\n")
                f.write("| Component | Status | Score | Duration | RAM Delta | Feedback |\n")
                f.write("|-----------|--------|-------|----------|-----------|----------|\n")
                for t in tests:
                    status_icon = "PASS" if t.get("status") == "PASS" else "FAIL"
                    score = t.get("score", "N/A")
                    duration = f"{t.get('duration_sec', 0):.2f}s"
                    ram = f"{t.get('ram_delta_mb', 0):.1f} MB"
                    feedback = t.get("feedback", "")
                    f.write(f"| {t['component']} | {status_icon} | {score} | {duration} | {ram} | {feedback} |\n")
                f.write("\n")
        return report_path

def run_test_module(name, path):
    print(f"{STEP} Executing {name} ({path})...")
    try:
        # Propagate current working directory to PYTHONPATH
        env = os.environ.copy()
        env["PYTHONPATH"] = os.getcwd() + os.pathsep + env.get("PYTHONPATH", "")
        
        # We use current python executable
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=120,
            env=env
        )
        
        # Parse output looking for RESULT_JSON:
        output = result.stdout
        for line in output.splitlines():
            if line.startswith("RESULT_JSON:"):
                json_str = line.replace("RESULT_JSON:", "").strip()
                return json.loads(json_str)
        
        return {"component": name, "status": "FAIL", "feedback": f"No JSON data found in output. Error: {result.stderr}"}
    except Exception as e:
        return {"component": name, "status": "FAIL", "feedback": f"Execution error: {str(e)}"}

def main():
    print(f"\n=== GENIO LLM STRUCTURED VALIDATION ENGINE v46.1 ===")
    print(f"{INFO} Initializing Orchestrator...")
    
    orch = ValidationOrchestrator()
    
    for cat, path in TEST_MODULES.items():
        if os.path.exists(path):
            res = run_test_module(cat, path)
            orch.add_results(cat, res)
        else:
            print(f"{INFO} Skipping {cat} (not found)")
    
    json_p = orch.generate_json_report()
    md_p = orch.generate_markdown_report()
    
    print(f"\n{OK} Validation Cycle Complete!")
    print(f"{INFO} MD Report: {md_p}")
    print(f"{INFO} JSON Report: {json_p}")
    
    total = 0
    passed = 0
    for cat in orch.results["categories"].values():
        for t in cat:
            total += 1
            if t.get("status") == "PASS":
                passed += 1
    
    print(f"{INFO} Results: {passed}/{total} components passed.")

if __name__ == "__main__":
    main()
