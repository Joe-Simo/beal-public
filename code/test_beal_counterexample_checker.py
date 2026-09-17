"""
Beal Counterexample Checker Test Suite Entrypoint
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from test_section8_counterexample_checker import TestSection8BealChecker

__all__ = ["TestSection8BealChecker"]

if __name__ == "__main__":
    unittest.main(verbosity=2)
