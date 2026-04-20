"""
Stoic Life OS — Daily Email Notifier
Portfolio Project | Data & Business Career Edition
Author: Dean C
"""

import smtplib
import os
import json
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from content.messages import get_message
from templates.email_template import build_email


def send_email(subject: str, html_body: str):
    sender = os.environ["GMAIL_USER"]
    recipient = os.environ["RECIPIENT_EMAIL"]
    password = os.environ["GMAIL_APP_PASSWORD"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Stoic Life OS <{sender}>"
    msg["To"] = recipient

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

    print(f"[OK] Email sent: {subject}")


def main():
    slot = os.environ.get("SLOT", "morning")  # morning | midday | evening

    # Day-of-year as rotation seed — changes daily, consistent across runs
    day_of_year = datetime.datetime.now().timetuple().tm_yday

    message = get_message(slot=slot, day_seed=day_of_year)

    html = build_email(
        slot=slot,
        title=message["title"],
        quote=message["quote"],
        source=message["source"],
        body=message["body"],
        challenge=message["challenge"],
        topic=message["topic"],
    )

    subject_map = {
        "morning": f"[Morning Anchor] {message['title']}",
        "midday": f"[Midday Reset] {message['title']}",
        "evening": f"[Evening Review] {message['title']}",
    }

    send_email(subject=subject_map[slot], html_body=html)


if __name__ == "__main__":
    main()
