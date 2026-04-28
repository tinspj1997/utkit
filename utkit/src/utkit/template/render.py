from __future__ import annotations

from typing import Dict

from jinja2 import Environment, FileSystemLoader, select_autoescape


# ------------------------
# Render HTML from file
# ------------------------

def render_html_template(
    template_name: str,
    context: Dict,
    template_dir: str = "templates",
) -> str:
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template(template_name)
    return template.render(**context)


# ------------------------
# Render HTML from string
# ------------------------

def render_html_string(template_str: str, context: Dict) -> str:
    env = Environment(autoescape=True)
    template = env.from_string(template_str)
    return template.render(**context)


__all__ = ["render_html_template", "render_html_string"]
