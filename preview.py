"""
Local preview tool — generates email HTML to a file so you can
open it in a browser and see exactly what will be sent.

Usage:
    python preview.py morning
    python preview.py midday
    python preview.py evening

No credentials needed. Opens the rendered HTML in your default browser.
"""

import sys
import os
import datetime
import webbrowser
import tempfile

sys.path.insert(0, os.path.dirname(__file__))

from content.messages import get_message
from templates.email_template import build_email


def preview(slot: str = "morning"):
    day_seed = datetime.datetime.now().timetuple().tm_yday
    message = get_message(slot=slot, day_seed=day_seed)

    html = build_email(
        slot=slot,
        title=message["title"],
        quote=message["quote"],
        source=message["source"],
        body=message["body"],
        challenge=message["challenge"],
        topic=message["topic"],
    )

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, encoding="utf-8"
    ) as f:
        f.write(html)
        path = f.name

    print(f"\n[Preview] Slot: {slot.upper()}")
    print(f"[Preview] Topic: {message['topic']}")
    print(f"[Preview] Title: {message['title']}")
    print(f"[Preview] Opening in browser: {path}\n")

    webbrowser.open(f"file://{path}")


if __name__ == "__main__":
    slot = sys.argv[1] if len(sys.argv) > 1 else "morning"
    if slot not in ("morning", "midday", "evening"):
        print("Usage: python preview.py [morning|midday|evening]")
        sys.exit(1)
    preview(slot)
