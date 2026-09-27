"""Regression tests for the embedded web UI."""

import asyncio

from eonapi.server import root


def test_web_ui_auto_renders_custom_graph_on_load():
    """The custom graph should initialize without a manual button click."""
    html = asyncio.run(root())

    assert "Average Half-hourly Energy Consumption" in html
    assert "Methodology for the average half-hourly chart" in html
    assert "Generate" not in html
    assert "watch: {" in html
    assert "customGraphType()" in html
    assert "customHour()" in html
    assert "this.renderCustomGraph();" in html
