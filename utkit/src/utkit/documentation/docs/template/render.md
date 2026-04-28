---
icon: lucide/layout-template
---

# Template Rendering

The `utkit.template.render` module provides HTML rendering utilities powered by [Jinja2](https://jinja.palletsprojects.com/). It supports rendering from template files on disk and from raw template strings.

## Installation

`jinja2` is part of the optional `standard` extras. Install `utkit` with the `standard` extra:

```bash
pip install "utkit[standard]"
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[standard]"
```

---

## Quick start

**From a file:**

```python
from utkit.template.render import render_html_template

html = render_html_template(
    template_name="welcome.html",
    context={"name": "Alice", "app": "utkit"},
    template_dir="templates",
)
```

**From a string:**

```python
from utkit.template.render import render_html_string

html = render_html_string(
    template_str="<h1>Hello, {{ name }}!</h1>",
    context={"name": "Alice"},
)
```

---

## `render_html_template`

Renders an HTML template file using Jinja2's `FileSystemLoader`. HTML and XML autoescaping is enabled automatically.

```python
def render_html_template(
    template_name: str,
    context: Dict,
    template_dir: str = "templates",
) -> str
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `template_name` | `str` | — | File name of the template relative to `template_dir` (e.g. `"email.html"`) |
| `context` | `Dict` | — | Dictionary of variables passed into the template |
| `template_dir` | `str` | `"templates"` | Path to the directory containing template files |

**Returns:** `str` — the fully rendered HTML string.

```python
# templates/invoice.html
# <p>Invoice #{{ number }} for {{ customer }}</p>

html = render_html_template(
    "invoice.html",
    {"number": 1042, "customer": "Acme Corp"},
    template_dir="templates",
)
```

---

## `render_html_string`

Renders HTML directly from a Jinja2 template string. Autoescaping is always enabled.

```python
def render_html_string(template_str: str, context: Dict) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `template_str` | `str` | A Jinja2 template string |
| `context` | `Dict` | Dictionary of variables passed into the template |

**Returns:** `str` — the fully rendered HTML string.

```python
html = render_html_string(
    "<p>Welcome, <strong>{{ name }}</strong>!</p>",
    {"name": "Alice"},
)
# <p>Welcome, <strong>Alice</strong>!</p>
```

---

## Usage with mail

`render_html_template` pairs naturally with `utkit.communication.mail.smtp` to send dynamic HTML emails:

```python
from utkit.template.render import render_html_template
from utkit.communication.mail.smtp import SMTPConfig, MailMessage, send_mail

config = SMTPConfig(
    host="smtp.gmail.com",
    port=587,
    username="you@gmail.com",
    password="your-app-password",
)

html = render_html_template(
    "welcome_email.html",
    {"name": "Alice", "app_url": "https://example.com"},
)

message = MailMessage(
    subject="Welcome to utkit",
    from_address="you@gmail.com",
    to=["alice@example.com"],
    html=html,
)

send_mail(config, message)
```
