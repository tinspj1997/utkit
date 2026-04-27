from __future__ import annotations

import smtplib
from dataclasses import dataclass, field
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    html: str
    cc: list[str] = field(default_factory=list)
    bcc: list[str] = field(default_factory=list)
    reply_to: str | None = None


def send_mail(config: SMTPConfig, message: MailMessage) -> None:
    """Send an HTML email via SMTP.

    Args:
        config: SMTP server connection settings.
        message: Email content and addressing details.
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = message.subject
    msg["From"] = message.from_address
    msg["To"] = ", ".join(message.to)

    if message.cc:
        msg["Cc"] = ", ".join(message.cc)
    if message.reply_to:
        msg["Reply-To"] = message.reply_to

    msg.attach(MIMEText(message.html, "html"))

    all_recipients = message.to + message.cc + message.bcc

    if config.use_tls:
        with smtplib.SMTP(config.host, config.port) as server:
            server.ehlo()
            server.starttls()
            server.login(config.username, config.password)
            server.sendmail(message.from_address, all_recipients, msg.as_string())
    else:
        with smtplib.SMTP_SSL(config.host, config.port) as server:
            server.login(config.username, config.password)
            server.sendmail(message.from_address, all_recipients, msg.as_string())
