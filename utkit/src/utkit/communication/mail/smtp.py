from __future__ import annotations

import smtplib
import ssl
from dataclasses import dataclass, field
from email.message import EmailMessage


@dataclass
class SMTPConfig:
    """SMTP connection configuration."""

    host: str
    port: int
    username: str
    password: str
    use_tls: bool = True


@dataclass
class MailMessage:
    """Email message parameters."""

    subject: str
    from_address: str
    to: list[str]
    cc: list[str] = field(default_factory=list)
    bcc: list[str] = field(default_factory=list)
    reply_to: str | None = None
    text: str | None = None
    html: str | None = None


def send_mail(config: SMTPConfig, message: MailMessage) -> None:
    """Send an email via SMTP.

    Args:
        config: SMTP server connection settings.
        message: Email content and addressing details.

    Raises:
        ValueError: If both text and html are None, or if port is unsupported.
    """
    if not message.text and not message.html:
        raise ValueError("Either 'text' or 'html' content must be provided")

    msg = EmailMessage()
    msg["Subject"] = message.subject
    msg["From"] = message.from_address
    msg["To"] = ", ".join(message.to)

    if message.cc:
        msg["Cc"] = ", ".join(message.cc)
    if message.reply_to:
        msg["Reply-To"] = message.reply_to

    # Set content based on what's provided
    if message.text and message.html:
        # Both text and html: set text first, then add html as alternative
        msg.set_content(message.text)
        msg.add_alternative(message.html, subtype="html")
    elif message.text:
        # Only text
        msg.set_content(message.text)
    else:
        # Only html
        msg.set_content(message.html, subtype="html")

    if config.port == 465:
        # Use SMTP_SSL for port 465
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config.host, config.port, context=context) as server:
            server.login(config.username, config.password)
            server.send_message(msg)
    elif config.port == 587:
        # Use SMTP with STARTTLS for port 587
        with smtplib.SMTP(config.host, config.port) as server:
            server.starttls()
            server.login(config.username, config.password)
            server.send_message(msg)
    else:
        raise ValueError(f"Unsupported SMTP port: {config.port}. Use 465 or 587.")
