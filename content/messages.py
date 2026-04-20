"""
Message library — 7 topics, 3 slots, daily rotation.
Topics: career, integrity, family, finances, body, mental, philosophy
Each topic rotates through multiple entries so content stays fresh.
"""

TOPICS = ["career", "integrity", "family", "finances", "body", "mental", "philosophy"]

MESSAGES = {

    # ─────────────────────────────────────────────
    # MORNING SLOT
    # ─────────────────────────────────────────────
    "morning": {

        "career": [
            {
                "title": "Deliver insight, not output",
                "quote": "Confine yourself to the present.",
                "source": "Marcus Aurelius, Meditations",
                "topic": "Career & Data",
                "body": "Every analyst produces numbers. The top 1% translate numbers into decisions. Before you open a single dashboard today, ask: what decision does my work need to support? Work backwards from that. Insight is the product. Data is just the material.",
                "challenge": "Identify one piece of work this week that you will reframe — not as a report, but as a recommendation.",
            },
            {
                "title": "Build visibility deliberately",
                "quote": "No man is crushed by Fortune unless he first trusts her.",
                "source": "Seneca, Letters from a Stoic",
                "topic": "Career & Data",
                "body": "Excellence in isolation is a career dead end. Today, think about one senior stakeholder who does not yet know the quality of your work. What can you put in front of them — proactively, professionally, with no agenda except value? The person who is seen doing excellent work gets promoted. The person who only does it gets passed over.",
                "challenge": "Send one value-adding communication to a stakeholder above your direct manager this week.",
            },
            {
                "title": "Stay six months ahead",
                "quote": "If you wish to improve, be content to appear foolish.",
                "source": "Epictetus, Enchiridion",
                "topic": "Career & Data",
                "body": "The data professional who is learning what everyone else learned six months ago is already behind. AI tools, advanced analytics, machine learning fundamentals — these are not optional extras for the ambitious. Block three hours this week for skills beyond your current role. Protect that block like a client meeting.",
                "challenge": "Name one technical skill you will dedicate time to this week. Schedule it now.",
            },
        ],

        "integrity": [
            {
                "title": "Draw your lines before the moment",
                "quote": "First say to yourself what you would be; and then do what you have to do.",
                "source": "Epictetus, Discourses",
                "topic": "Integrity",
                "body": "Ethical decisions made in the moment are the most dangerous. The pressure, the politics, the incentive — they all cloud judgment. The top performers draw their non-negotiables in advance, when the mind is clear. Today: identify one area of your work or personal life where the line needs to be drawn before you are tested.",
                "challenge": "Write one non-negotiable you will not cross — professionally or personally — regardless of pressure.",
            },
            {
                "title": "Your private life is not private",
                "quote": "Retire into yourself as much as possible.",
                "source": "Seneca, Letters from a Stoic",
                "topic": "Integrity",
                "body": "Every high-achiever who fell, fell because of something they thought was contained. Affairs, financial shortcuts, substance habits — nothing stays contained forever. The standard is not 'will anyone find out.' The standard is: would you be comfortable if every action you took today was visible to the people you most respect? Live at that standard.",
                "challenge": "Run the visibility test on one area of your personal life today. Be honest.",
            },
        ],

        "family": [
            {
                "title": "Presence is the rarest resource",
                "quote": "Begin the morning by saying to thyself, I shall meet with meddling, ungrateful, violent men today — but I have seen the beauty of good.",
                "source": "Marcus Aurelius, Meditations",
                "topic": "Family & Love",
                "body": "Marcus Aurelius ran an empire and still wrote about the duty of care owed to those closest to him. Your family does not need your money or your title. They need your full attention — not the version of you that arrives home still mentally in the office. Being truly present with the people you love is not a break from discipline. It is an expression of it.",
                "challenge": "Designate one hour today with no phone, no work thoughts — fully present with someone you love.",
            },
            {
                "title": "Your children are watching your character",
                "quote": "Waste no more time arguing about what a good man should be. Be one.",
                "source": "Marcus Aurelius, Meditations",
                "topic": "Family & Love",
                "body": "Every value you want to instil in your children is being absorbed right now — not from your words, but from your behaviour under pressure. How you handle disappointment, how you treat people with less power, how you respond when things go wrong. The most powerful parenting you will ever do is simply being the person you want them to become.",
                "challenge": "Identify one character trait you want to model for your child. Demonstrate it deliberately today.",
            },
        ],

        "finances": [
            {
                "title": "Never spend what you have not earned",
                "quote": "It is not the man who has too little who is poor, but the man who craves more.",
                "source": "Seneca, Letters from a Stoic",
                "topic": "Finances",
                "body": "Provider pressure creates the most dangerous financial decisions. The fear of not being enough pushes people into get-rich-quick thinking, lifestyle debt, and investments they do not understand. The Stoic rule: separate needs from appearances. Most of what feels urgent financially is ego. Your actual obligations are far smaller than your fear makes them feel.",
                "challenge": "List your three largest expenses this month. Identify which serves your goals and which serves your image.",
            },
            {
                "title": "Build the asset column first",
                "quote": "Prefer knowledge to wealth, for the one is transitory, the other perpetual.",
                "source": "Socrates",
                "topic": "Finances",
                "body": "As a data professional, your primary asset is your skill set and your earning capacity — not your car or your lifestyle. Every rand invested in growing your professional capabilities compounds faster than almost any financial product. Invest in yourself first, consistently, before you invest in anything else.",
                "challenge": "Calculate what 10% of this month's income invested in your own development would buy you — a course, a book, a certification.",
            },
        ],

        "body": [
            {
                "title": "Exercise before email",
                "quote": "Endure, and preserve yourself for better things.",
                "source": "Virgil",
                "topic": "Body & Energy",
                "body": "Your cognitive edge — the thing that separates you in a data career — runs entirely on your physical state. Sleep quality, exercise, nutrition: these are not lifestyle choices, they are performance inputs. The first hour of your day sets the neurological tone for everything that follows. Protect it from screens, from email, from other people's urgency.",
                "challenge": "Move your body before you open your phone this morning. Even 20 minutes changes your entire cognitive day.",
            },
        ],

        "mental": [
            {
                "title": "Control the first hour",
                "quote": "You have power over your mind, not outside events. Realise this and you will find strength.",
                "source": "Marcus Aurelius, Meditations",
                "topic": "Mental Discipline",
                "body": "The first 60 minutes of your day are the highest-leverage window you have. Most people surrender them immediately — phone notifications, news, other people's problems. The top performers guard this window. Read, plan, move, think. Enter the world on your own terms. Everything else is noise until you have set your frame.",
                "challenge": "No social media, no news, no email for the first 45 minutes this morning. Your mind first.",
            },
            {
                "title": "One priority, executed completely",
                "quote": "If one does not know to which port one is sailing, no wind is favourable.",
                "source": "Seneca, Letters from a Stoic",
                "topic": "Mental Discipline",
                "body": "Busyness is not progress. The data professional who works 10 hours on six half-finished things produces less than the one who works four hours on the single most important thing. Every morning: name the one thing that, if completed today, would move your career or life forward most significantly. Do that thing first, before the day hijacks you.",
                "challenge": "Write your single most important task for today. Do it before 10am. Nothing else counts until it is done.",
            },
        ],

        "philosophy": [
            {
                "title": "The dichotomy of control",
                "quote": "Make the best use of what is in your power, and take the rest as it happens.",
                "source": "Epictetus, Enchiridion",
                "topic": "Stoic Philosophy",
                "body": "Epictetus built the entire Stoic system on one distinction: what is yours and what is not. Your judgments, your effort, your character — yours. Other people's opinions, market conditions, your manager's mood, outcomes — not yours. This is not passivity. It is the most efficient possible allocation of your energy. Stop spending it where it cannot work.",
                "challenge": "Write two lists: what you control today, and what you do not. Only act on list one.",
            },
            {
                "title": "Premeditatio malorum — defang the day",
                "quote": "Nothing happens to the wise man against his expectation.",
                "source": "Seneca, Letters from a Stoic",
                "topic": "Stoic Philosophy",
                "body": "The Stoics practiced mentally rehearsing the worst realistic outcome of their day — not to become pessimistic, but to remove the element of shock. When you have already faced something mentally, it loses its power to destabilise you in reality. Spend three minutes every morning asking: what is the hardest thing that could happen today? Rehearse your composed response. Then release it.",
                "challenge": "Name the most difficult scenario you might face today. Decide now how the disciplined version of you will respond.",
            },
        ],
    },

    # ─────────────────────────────────────────────
    # MIDDAY SLOT (13:30)
    # ─────────────────────────────────────────────
    "midday": {

        "career": [
            {
                "title": "The meeting audit",
                "quote": "Speak only when you are certain your words are better than silence.",
                "source": "Attributed to Pythagoras",
                "topic": "Career & Data",
                "body": "Midday check: how have you shown up in conversations today? The top professional speaks less and lands harder. One sharp, well-prepared point beats five reactive ones. If you have a meeting this afternoon, ask yourself: what is the single thing I want them to remember about my contribution? Enter with that, and only that.",
                "challenge": "In your next meeting or conversation, make one deliberate, prepared point — then listen.",
            },
        ],

        "integrity": [
            {
                "title": "The midday integrity scan",
                "quote": "It is not enough to do good; one must do it the right way.",
                "source": "John Morley",
                "topic": "Integrity",
                "body": "Pause. In the last four hours: did you say anything you would not want recorded? Did you make any commitment you are not certain you can keep? Did you cut any corner — however small — that compromises your standard? Small ethical drifts compound invisibly. This is the moment to catch them before they become character.",
                "challenge": "Name one thing from this morning you would do differently. Correct it this afternoon.",
            },
        ],

        "family": [
            {
                "title": "Send one message that matters",
                "quote": "The best thing to spend on your children is your time.",
                "source": "Louise Hart",
                "topic": "Family & Love",
                "body": "You are deep in the workday. Take 90 seconds right now — not tonight, not later. Send a message to someone you love. Not a functional message. A human one. The person who is building a career and still makes their family feel seen is rare. Be that person daily, not occasionally.",
                "challenge": "Send one genuine, non-functional message to a family member or partner right now.",
            },
        ],

        "finances": [
            {
                "title": "No reactive financial decisions",
                "quote": "He who is brave is free.",
                "source": "Seneca",
                "topic": "Finances",
                "body": "Midday is when financial temptation and impulsive decisions peak — lunch purchases that erode budgets, investment impulses triggered by a conversation, lifestyle spending justified by stress. The rule: no financial decision made in an emotionally activated state. Pause 72 hours on anything that is not a necessity. The decision will either survive or dissolve — both are useful information.",
                "challenge": "Is there any financial decision or temptation active right now? Write it down. Return to it in 72 hours.",
            },
        ],

        "body": [
            {
                "title": "Recalibrate your energy",
                "quote": "Take care of your body. It's the only place you have to live.",
                "source": "Jim Rohn",
                "topic": "Body & Energy",
                "body": "Midday energy collapse is a choice, not an inevitability. What did you eat this morning — fuel or comfort? Are you hydrated? Have you moved since you sat down? Your afternoon performance — in data work, in meetings, in thinking — is entirely determined by what you do with your body in the next 20 minutes. A 10-minute walk now returns two hours of cognitive quality.",
                "challenge": "Step away from your screen for 10 minutes. Walk, breathe, reset. Do it now.",
            },
        ],

        "mental": [
            {
                "title": "Are you building or being busy?",
                "quote": "It is not that we have a short time to live, but that we waste much of it.",
                "source": "Seneca, On the Shortness of Life",
                "topic": "Mental Discipline",
                "body": "Midday honest check: look at your last four hours. Were you doing the work that moves your career forward — or were you managing email, attending meetings that could have been messages, and reacting to other people's priorities? Busyness is the enemy of building. The ambitious person protects their deep work hours ruthlessly.",
                "challenge": "Name the single highest-leverage thing you have not done yet today. Protect the next 90 minutes for it.",
            },
        ],

        "philosophy": [
            {
                "title": "The view from above",
                "quote": "You could leave life right now. Let that determine what you do and say and think.",
                "source": "Marcus Aurelius, Meditations",
                "topic": "Stoic Philosophy",
                "body": "Marcus practised what he called the 'view from above' — mentally zooming out from the immediate problem to see it in its true proportion. The difficult colleague, the delayed project, the awkward email — seen from the perspective of a year from now, how significant is this? Most midday stress is manufactured urgency. Step back. Respond from the elevated view.",
                "challenge": "Name the thing causing you most stress right now. Ask: will this matter in one year? Then respond accordingly.",
            },
        ],
    },

    # ─────────────────────────────────────────────
    # EVENING SLOT (22:00)
    # ─────────────────────────────────────────────
    "evening": {

        "career": [
            {
                "title": "Document today's win",
                "quote": "When you arise in the morning, think of what a precious privilege it is to be alive.",
                "source": "Marcus Aurelius, Meditations",
                "topic": "Career & Data",
                "body": "The person who tracks their wins gets promoted. The person who does not gets forgotten. Before you sleep: write one specific thing you did today that demonstrates your value as a data professional. Not a task completed — a contribution made. Build this record weekly. It becomes your promotion case, your interview story, your confidence in difficult moments.",
                "challenge": "Write one sentence: the most valuable contribution I made today was...",
            },
        ],

        "integrity": [
            {
                "title": "The nightly Seneca audit",
                "quote": "I examine my entire day and go back over what I've done and said.",
                "source": "Seneca, On Anger",
                "topic": "Integrity",
                "body": "Seneca ended every day with three questions: What bad habit have I resisted today? How have I improved? What remains to be worked on? This is not self-punishment — it is quality control. The person who audits themselves nightly is the person who improves weekly. Five minutes of honest reflection compounds into years of character.",
                "challenge": "Answer Seneca's three questions honestly before you sleep tonight.",
            },
        ],

        "family": [
            {
                "title": "Did the people who matter feel it?",
                "quote": "In family life, love is the oil that eases friction, the cement that binds closer together.",
                "source": "Friedrich Nietzsche",
                "topic": "Family & Love",
                "body": "This is the hardest question a high achiever can sit with: did the people closest to you feel loved, seen, and valued today — or were they recipients of your leftover energy? Success that costs you your family is not success. It is a trade you make gradually, invisibly, until one day the cost becomes visible. Tonight: close the day with the people who matter most.",
                "challenge": "Before you sleep, tell one person you love them — not functionally, genuinely.",
            },
            {
                "title": "Leave work at the door",
                "quote": "A man who dares to waste one hour of time has not discovered the value of life.",
                "source": "Charles Darwin",
                "topic": "Family & Love",
                "body": "The most disciplined professional skill you can develop is compartmentalisation. When you are home, be home. Fully. Your family does not need 20% of you while 80% is still in the office. Presence is not about time — it is about quality of attention. The hour you give fully is worth more than four hours given partially.",
                "challenge": "No work email, no Slack, no 'just one more thing' after 9pm tonight. Protect the hour before sleep for the people and the rest that matter.",
            },
        ],

        "finances": [
            {
                "title": "The evening financial check",
                "quote": "Wealth consists not in having great possessions, but in having few wants.",
                "source": "Epictetus",
                "topic": "Finances",
                "body": "End the day with a clear financial picture, not a vague anxiety about money. What did you spend today — and was it intentional? Are you moving toward your financial goals or drifting? The person who manages money daily makes better decisions monthly. Five minutes of financial clarity at night removes the low-grade stress that bleeds into everything else.",
                "challenge": "Name one financial decision this week that moved you toward your goals. Name one that did not.",
            },
        ],

        "body": [
            {
                "title": "Protect the recovery",
                "quote": "Early to bed and early to rise makes a man healthy, wealthy and wise.",
                "source": "Benjamin Franklin",
                "topic": "Body & Energy",
                "body": "Your sleep is your performance infrastructure. Every elite performer — every serious athlete, every high-functioning executive — treats sleep as a non-negotiable. No screen one hour before bed. No heavy food. No work email after 9pm. Tomorrow's focus, patience, decision quality, and emotional regulation are all determined by what you do in the next hour. Protect it.",
                "challenge": "Put your phone face-down in one hour. Read, reflect, or rest. Tomorrow's version of you is built tonight.",
            },
        ],

        "mental": [
            {
                "title": "The three-question debrief",
                "quote": "I will keep constant watch over myself and — most usefully — will put each day up for review.",
                "source": "Seneca, Letters from a Stoic",
                "topic": "Mental Discipline",
                "body": "Tonight's three questions, answered with honesty not harshness: Where did I act with full discipline today? Where did ego, fear, or distraction get the better of me? What would the most disciplined version of me do differently tomorrow? This is not self-criticism — it is the nightly calibration that makes the long game possible.",
                "challenge": "Write three sentences — one for each question. Be honest. Then release it and rest.",
            },
        ],

        "philosophy": [
            {
                "title": "Memento mori — the gift of urgency",
                "quote": "Let us prepare our minds as if we had come to the very end of life.",
                "source": "Seneca, Letters from a Stoic",
                "topic": "Stoic Philosophy",
                "body": "The Stoics contemplated death not with morbidity but with clarity. If today had been your last day — not in a panicked sense, but in a clear-eyed one — did you spend it on what matters? Did you move your career forward? Did you love the people who deserve it? Did you live with the integrity you claim to hold? The contemplation of finitude is the antidote to drifting.",
                "challenge": "Name one thing you have been postponing that matters. Commit to beginning it tomorrow.",
            },
        ],
    },
}


def get_message(slot: str, day_seed: int) -> dict:
    """
    Returns a message for the given slot and day seed.
    Topics rotate by day. Within each topic, messages rotate independently.
    This ensures maximum variety — different topic AND different message daily.
    """
    slot_messages = MESSAGES.get(slot, MESSAGES["morning"])
    topics = list(slot_messages.keys())

    # Pick topic for today
    topic_index = day_seed % len(topics)
    topic = topics[topic_index]

    # Pick message within topic
    topic_msgs = slot_messages[topic]
    msg_index = (day_seed // len(topics)) % len(topic_msgs)

    return topic_msgs[msg_index]
