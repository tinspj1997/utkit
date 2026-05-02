---
icon: lucide/mail
---

# Mail

The `utkit.communication.mail.smtp` module provides a simple interface for sending emails (plain text or HTML) over SMTP.

## Installation

No extra dependencies are required — the module uses Python's built-in `smtplib` and `email` libraries.

## Quick start

```python
from utkit.communication.mail.smtp import SMTPConfig, MailMessage, send_mail

config = SMTPConfig(
    host="smtp.gmail.com",
    port=587,
    username="you@gmail.com",
    password="your-app-password",
)

message = MailMessage(
    subject="Hello from utkit",
    from_address="you@gmail.com",
    to=["recipient@example.com"],
    html="<h1>Hello!</h1><p>This email was sent using <strong>utkit</strong>.</p>",
)

send_mail(config, message)
```

---

## `SMTPConfig`

Holds the SMTP server connection settings.

```python
@dataclass
class SMTPConfig:
    host: str
    port: int
    username: str
    password: str
    use_tls: bool = True
```

| Field | Type | Required | Description |
|---|---|---|---|
| `host` | `str` | Yes | SMTP server hostname (e.g. `smtp.gmail.com`) |
| `port` | `int` | Yes | SMTP port — use `587` for STARTTLS, `465` for SSL |
| `username` | `str` | Yes | SMTP login username |
| `password` | `str` | Yes | SMTP login password or app password |
| `use_tls` | `bool` | No | `True` uses STARTTLS (default), `False` uses SMTP_SSL (note: `port` determines the method) |

---

## `MailMessage`

Defines the email content and addressing.

```python
@dataclass
class MailMessage:
    subject: str
    from_address: str
    to: list[str]
    cc: list[str] = field(default_factory=list)
    bcc: list[str] = field(default_factory=list)
    reply_to: str | None = None
    text: str | None = None
    html: str | None = None
```

| Field | Type | Required | Description |
|---|---|---|---|
| `subject` | `str` | Yes | Email subject line |
| `from_address` | `str` | Yes | Sender email address |
| `to` | `list[str]` | Yes | List of recipient email addresses |
| `cc` | `list[str]` | No | CC recipients (default: empty) |
| `bcc` | `list[str]` | No | BCC recipients (default: empty) |
| `reply_to` | `str \| None` | No | Reply-To address (default: `None`) |
| `text` | `str \| None` | No | Plain text body (default: `None`) |
| `html` | `str \| None` | No | HTML body (default: `None`) |

**Note:** At least one of `text` or `html` must be provided, otherwise a `ValueError` is raised.

---

## `send_mail`

Sends the email using the provided configuration and message.

```python
def send_mail(config: SMTPConfig, message: MailMessage) -> None
```

| Parameter | Type | Description |
|---|---|---|
| `config` | `SMTPConfig` | SMTP server connection settings |
| `message` | `MailMessage` | Email content and addressing details |

**Raises:**
- `ValueError` — If both `text` and `html` are `None`, or if `port` is not 465 or 587
- `smtplib.SMTPException` — On delivery failure

---

## Examples

### Plain text email

```python
message = MailMessage(
    subject="Hello",
    from_address="sender@example.com",
    to=["recipient@example.com"],
    text="This is a plain text email.\nMultiple lines supported.",
)
```

### With CC and BCC

```python
message = MailMessage(
    subject="Team update",
    from_address="sender@example.com",
    to=["alice@example.com"],
    cc=["bob@example.com"],
    bcc=["audit@example.com"],
    html="<p>Please find the update below.</p>",
)
```

### Multipart (text + HTML fallback)

```python
message = MailMessage(
    subject="Welcome",
    from_address="sender@example.com",
    to=["user@example.com"],
    text="Welcome! View this email in HTML for best experience.",
    html="<h1>Welcome!</h1><p>This is the HTML version.</p>",
)
```

### With Reply-To

```python
message = MailMessage(
    subject="No-reply notification",
    from_address="noreply@example.com",
    to=["user@example.com"],
    html="<p>Your order has been shipped.</p>",
    reply_to="support@example.com",
)
```

### Using SSL (port 465)

```python
config = SMTPConfig(
    host="smtp.example.com",
    port=465,
    username="sender@example.com",
    password="secret",
)
```

Port 465 automatically uses SMTP_SSL. Port 587 uses STARTTLS.

---


