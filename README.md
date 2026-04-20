# Stoic Life OS — Daily Email Notifier

A scheduled email notification system delivering daily Stoic discipline and life-performance reminders across three daily touchpoints.

Built as a portfolio project combining Python automation, HTML email templating, content rotation logic, and GitHub Actions CI/CD scheduling — with zero cost and zero external dependencies.

---

## What it does

Sends three daily emails to a configured recipient:

| Slot | Time (SAST) | Purpose |
|------|-------------|---------|
| Morning Anchor | 05:00 | Set the day's frame, prime discipline |
| Midday Reset | 13:30 | Recalibrate focus and integrity |
| Evening Review | 22:00 | Audit the day, close with presence |

Each email draws from a rotating library of messages across **7 life domains**:

- Career & Data performance
- Integrity & ethical discipline
- Family & relationships
- Finances & provider mindset
- Body & physical energy
- Mental discipline & focus
- Stoic philosophy (Marcus Aurelius, Seneca, Epictetus)

The rotation is seeded by the day of the year — consistent within a day but different every day, ensuring no two consecutive days deliver the same topic or message.

---

## Tech stack

| Component | Tool | Cost |
|-----------|------|------|
| Language | Python 3.11 | Free |
| Email delivery | Gmail SMTP (standard library) | Free |
| Scheduling | GitHub Actions cron | Free |
| Hosting | GitHub | Free |
| Dependencies | None (stdlib only) | Free |

---

## Project structure

```
stoic-notifier/
├── notifier.py              # Entry point — orchestrates sending
├── content/
│   └── messages.py          # All message content + rotation logic
├── templates/
│   └── email_template.py    # HTML email builder
├── .github/
│   └── workflows/
│       └── notify.yml       # GitHub Actions scheduler
├── requirements.txt
└── README.md
```

---

## Setup guide

### 1. Fork or clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/stoic-notifier.git
cd stoic-notifier
```

### 2. Enable Gmail App Password

Gmail requires an App Password for SMTP when 2-factor authentication is enabled (recommended).

1. Go to your Google Account → Security
2. Under "How you sign in to Google", select **2-Step Verification**
3. Scroll to the bottom → **App Passwords**
4. Generate a password for "Mail" on "Other device" — name it "Stoic Notifier"
5. Copy the 16-character password

### 3. Add GitHub Secrets

In your GitHub repository:

1. Go to **Settings → Secrets and variables → Actions**
2. Add three secrets:

| Secret name | Value |
|-------------|-------|
| `GMAIL_USER` | Your Gmail address (e.g. `you@gmail.com`) |
| `GMAIL_APP_PASSWORD` | The 16-character app password from step 2 |
| `RECIPIENT_EMAIL` | The email address to send notifications to |

### 4. Enable GitHub Actions

Go to the **Actions** tab in your repository and enable workflows if prompted.

### 5. Test manually

Go to **Actions → Stoic Daily Notifier → Run workflow**.

Select a slot (`morning`, `midday`, or `evening`) and click **Run workflow**. Check your inbox within 30 seconds.

---

## Customising content

All message content lives in `content/messages.py`.

To add a new message, find the relevant slot (`morning`, `midday`, or `evening`) and topic, then append a new dictionary to the list:

```python
{
    "title": "Your message title",
    "quote": "A Stoic quote relevant to this message",
    "source": "Author, Work",
    "topic": "The domain label",
    "body": "The main message body — 3 to 5 sentences of direct, practical wisdom.",
    "challenge": "A single, specific action the reader can take today.",
},
```

To add a new topic, add a new key to the slot dictionary and populate it with at least one message.

---

## Rotation logic

The rotation uses the **day of the year** (1–365) as a seed:

```python
topic_index = day_seed % len(topics)          # cycles through topics daily
msg_index = (day_seed // len(topics)) % len(topic_msgs)  # cycles through messages within topic
```

This means:
- The topic changes every day
- The message within the topic changes on a longer cycle
- The same seed always returns the same message (deterministic, no database needed)

---

## Portfolio notes

This project demonstrates:

- **Python automation** — SMTP email sending, environment variable management, modular structure
- **Content logic** — deterministic rotation without a database, slot-based routing
- **HTML email templating** — inline CSS, responsive layout, visual identity system
- **CI/CD with GitHub Actions** — cron scheduling, secrets management, manual dispatch triggers
- **Clean code structure** — separation of concerns (content / template / orchestration)
- **Zero-cost infrastructure** — production system with no paid services

---

## Inspired by

- Marcus Aurelius, *Meditations* (Gregory Hays translation)
- Seneca, *Letters from a Stoic*
- Epictetus, *The Enchiridion*

---

*Built as part of a personal discipline and data career development system.*
