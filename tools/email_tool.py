"""Email tool via SMTP — works with Gmail, Outlook, or any SMTP server.

Setup in .env:
    EMAIL_SENDER=your@gmail.com
    EMAIL_PASSWORD=your_app_password   # Gmail: 16-char App Password
    EMAIL_SMTP_HOST=smtp.gmail.com     # default
    EMAIL_SMTP_PORT=587                # default

Gmail App Password: myaccount.google.com -> Security -> 2FA -> App passwords
"""

from __future__ import annotations

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


def send_email(to: str, subject: str, body: str) -> str:
    """Send an email. Input format: 'to@example.com | Subject | Body text'"""
    sender   = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    host     = os.getenv("EMAIL_SMTP_HOST", "smtp.gmail.com")
    port     = int(os.getenv("EMAIL_SMTP_PORT", "587"))

    if not sender or not password:
        return "EMAIL_SENDER or EMAIL_PASSWORD not set in .env"

    msg = MIMEMultipart()
    msg["From"]    = sender
    msg["To"]      = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, to, msg.as_string())
        return f"Email sent to {to} with subject '{subject}'"
    except Exception as e:
        return f"Failed to send email: {e}"


def parse_and_send(raw_input: str) -> str:
    """Parse 'to | subject | body' format and send email."""
    parts = [p.strip() for p in raw_input.split("|", 2)]
    if len(parts) < 3:
        return "Invalid format. Use: recipient@email.com | Subject | Body"
    return send_email(parts[0], parts[1], parts[2])
