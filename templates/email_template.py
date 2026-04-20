"""
HTML email template builder.
Produces a clean, professional styled email with Stoic visual identity.
"""

SLOT_CONFIG = {
    "morning": {
        "label": "Morning Anchor",
        "time": "Start of day",
        "accent": "#534AB7",
        "accent_light": "#EEEDFE",
        "accent_text": "#3C3489",
        "icon_symbol": "&#9670;",  # diamond
        "sub": "Set your frame. Control the day.",
    },
    "midday": {
        "label": "Midday Reset",
        "time": "13:30",
        "accent": "#1D9E75",
        "accent_light": "#E1F5EE",
        "accent_text": "#085041",
        "icon_symbol": "&#9632;",  # square
        "sub": "Recalibrate. Are you building or being busy?",
    },
    "evening": {
        "label": "Evening Review",
        "time": "22:00",
        "accent": "#BA7517",
        "accent_light": "#FAEEDA",
        "accent_text": "#633806",
        "icon_symbol": "&#9679;",  # circle
        "sub": "Close the day with discipline and presence.",
    },
}


def build_email(
    slot: str,
    title: str,
    quote: str,
    source: str,
    body: str,
    challenge: str,
    topic: str,
) -> str:
    cfg = SLOT_CONFIG.get(slot, SLOT_CONFIG["morning"])

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cfg['label']}: {title}</title>
</head>
<body style="margin:0;padding:0;background-color:#F4F3F0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0" style="background-color:#F4F3F0;padding:32px 16px;">
<tr><td align="center">

  <!-- CARD -->
  <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#FFFFFF;border-radius:12px;overflow:hidden;border:1px solid #E5E3DC;">

    <!-- HEADER BAR -->
    <tr>
      <td style="background:{cfg['accent']};padding:24px 32px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td>
              <p style="margin:0;font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,0.7);">{cfg['label']} &nbsp;|&nbsp; {cfg['time']}</p>
              <h1 style="margin:8px 0 0;font-size:22px;font-weight:500;color:#FFFFFF;line-height:1.3;">{title}</h1>
              <p style="margin:6px 0 0;font-size:13px;color:rgba(255,255,255,0.65);">{cfg['sub']}</p>
            </td>
            <td align="right" valign="top">
              <div style="width:44px;height:44px;border-radius:50%;background:rgba(255,255,255,0.15);display:inline-flex;align-items:center;justify-content:center;text-align:center;line-height:44px;font-size:20px;color:rgba(255,255,255,0.8);">{cfg['icon_symbol']}</div>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- TOPIC BADGE -->
    <tr>
      <td style="padding:20px 32px 0;">
        <span style="display:inline-block;background:{cfg['accent_light']};color:{cfg['accent_text']};font-size:11px;font-weight:600;letter-spacing:1px;text-transform:uppercase;padding:4px 12px;border-radius:6px;">{topic}</span>
      </td>
    </tr>

    <!-- QUOTE BLOCK -->
    <tr>
      <td style="padding:20px 32px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td style="border-left:3px solid {cfg['accent']};padding-left:16px;">
              <p style="margin:0;font-size:16px;font-style:italic;color:#2C2C2A;line-height:1.65;">&#8220;{quote}&#8221;</p>
              <p style="margin:8px 0 0;font-size:12px;color:#888780;">&#8212; {source}</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- DIVIDER -->
    <tr><td style="padding:0 32px;"><hr style="border:none;border-top:1px solid #E5E3DC;margin:0;"></td></tr>

    <!-- BODY -->
    <tr>
      <td style="padding:24px 32px;">
        <p style="margin:0;font-size:15px;color:#444441;line-height:1.75;">{body}</p>
      </td>
    </tr>

    <!-- CHALLENGE BOX -->
    <tr>
      <td style="padding:0 32px 28px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td style="background:{cfg['accent_light']};border-radius:8px;padding:16px 20px;">
              <p style="margin:0 0 6px;font-size:11px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:{cfg['accent_text']};">Today's Challenge</p>
              <p style="margin:0;font-size:14px;color:#2C2C2A;line-height:1.6;">{challenge}</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- STOIC VISUAL ELEMENT — SVG inline -->
    <tr>
      <td style="padding:0 32px 28px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td align="center" style="background:#F4F3F0;border-radius:8px;padding:20px;">
              <!-- Stoic symbol: three concentric circles representing the Stoic hierarchy -->
              <svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
                <circle cx="60" cy="60" r="55" fill="none" stroke="{cfg['accent']}" stroke-width="1" opacity="0.2"/>
                <circle cx="60" cy="60" r="38" fill="none" stroke="{cfg['accent']}" stroke-width="1" opacity="0.4"/>
                <circle cx="60" cy="60" r="20" fill="{cfg['accent']}" opacity="0.15"/>
                <circle cx="60" cy="60" r="8" fill="{cfg['accent']}" opacity="0.9"/>
                <text x="60" y="100" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="{cfg['accent_text']}" letter-spacing="2">INNER CITADEL</text>
              </svg>
              <p style="margin:4px 0 0;font-size:11px;color:#888780;font-style:italic;">Control the inner. Release the outer.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- FOOTER -->
    <tr>
      <td style="background:#F4F3F0;border-top:1px solid #E5E3DC;padding:16px 32px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td>
              <p style="margin:0;font-size:11px;color:#888780;">Stoic Life OS &nbsp;&middot;&nbsp; Your daily discipline system</p>
              <p style="margin:4px 0 0;font-size:11px;color:#B4B2A9;">Building toward the top 1% &mdash; in career, character, and life.</p>
            </td>
            <td align="right">
              <p style="margin:0;font-size:11px;color:#B4B2A9;font-style:italic;">Marcus &middot; Seneca &middot; Epictetus</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>

  </table>
  <!-- END CARD -->

</td></tr>
</table>

</body>
</html>
"""
