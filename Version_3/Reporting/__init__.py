"""
Reporting Module

Generates:
- Summary tables
- Figures (DCC, IRF proxies)
- Markdown reports
- LaTeX reports
"""

from .runner import run_reporting
from .collector import collect_all_results

__all__ = [
    "run_reporting",
    "collect_all_results",
]
