#!/usr/bin/env python3
"""Diff and source-health checks for CI."""
import os, re, sys
CONTROL = re.compile(r"[^\x09\x0a\x0d\x20-\x7e]")
problems = 0
for root, dirs, files in os.walk("src"):
    dirs[:] = [d for d in dirs if d not in ("__pycache__",)]
    for f in files:
        if not f.endswith(".py"):
            continue
        path = os.path.join(root, f)
        content = open(path, encoding="utf-8").read()
        if "eval(" in content:
            print(f"ERROR: eval() in {path}")
            problems += 1
        if CONTROL.search(content):
            print(f"ERROR: control/unicode in {path}")
            problems += 1
sys.exit(problems)
