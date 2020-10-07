"""Plotly Dash HTML layout override."""
from pathlib import Path
homedir = Path(__file__).parents[1]
basetemp = homedir/'templates'/ "project_dataviz_dash_calls.html"

with open(basetemp) as inf:
    html_layout = inf.read()



