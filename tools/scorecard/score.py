#!/usr/bin/env python3
"""
AI Freelancer Client Qualification Scorecard
Run this after any lead inquiry to score whether the lead is worth pursuing.
"""

def ask_score(prompt, max_score=5):
    while True:
        try:
            val = int(input(f"  {prompt} (1-5): "))
            if 1 <= val <= max_score:
                return val
            print(f"    → Enter a number 1-{max_score}")
        except (ValueError, EOFError):
            print(f"    → Defaulting to 3 (neutral)")
            return 3

def main():
    print("=" * 55)
    print("  CLIENT QUALIFICATION SCORECARD")
    print("  Score any lead in 2 minutes. Spend time only on winners.")
    print("=" * 55)
    print()

    print("[1/5] PROBLEM CLARITY")
    print("  Do they have a specific, describable problem you can solve?")
    print("  1 = Vague / 'help with stuff'")
    print("  3 = Somewhat clear")
    print("  5 = Specific, well-defined problem")
    p1 = ask_score("Score")

    print()
    print("[2/5] BUDGET")
    print("  Have they mentioned a budget or will they answer if asked?")
    print("  1 = No budget mentioned / 'depends' / very low")
    print("  3 = Has a range ($X - $Y)")
    print("  5 = Explicit budget stated and reasonable for your rates")
    p2 = ask_score("Score")

    print()
    print("[3/5] TIMELINE")
    print("  Is there a real deadline or urgency?")
    print("  1 = No timeline / 'when you can' / 'sometime'")
    print("  3 = This month or quarter")
    print("  5 = This week or specific urgent deadline")
    p3 = ask_score("Score")

    print()
    print("[4/5] DECISION MAKER")
    print("  Can they approve and sign, or do they need to report upward?")
    print("  1 = Needs multiple approvals / 'I need to check with my boss'")
    print("  3 = Can decide but will loop in one other person")
    print("  5 = Single decision-maker, can sign today")
    p4 = ask_score("Score")

    print()
    print("[5/5] WARMTH")
    print("  How did they find you and how researched is this?")
    print("  1 = Cold outreach / mass email / no prior contact")
    print("  3 = Visited your site / cold LinkedIn / mutual group")
    print("  5 = Referral, warm intro, or deeply researched their situation")
    p5 = ask_score("Score")

    total = p1 + p2 + p3 + p4 + p5
    print()
    print("=" * 55)
    print(f"  TOTAL SCORE: {total}/25")
    print("=" * 55)

    if total >= 18:
        tier = "TOP PRIORITY"
        action = "Reply within 2 hours. Send tailored pitch + propose next step."
    elif total >= 12:
        tier = "SCHEDULE A CALL"
        action = "Reply within 24 hours. Propose a 15-min discovery call."
    else:
        tier = "NURTURE ONLY"
        action = "Add to email nurture sequence. Don't chase aggressively."

    print(f"  Decision: {tier}")
    print(f"  Action:   {action}")
    print()

    print("Factor breakdown:")
    print(f"  Problem Clarity : {p1}/5  {'★' * p1}{'☆' * (5-p1)}")
    print(f"  Budget          : {p2}/5  {'★' * p2}{'☆' * (5-p2)}")
    print(f"  Timeline        : {p3}/5  {'★' * p3}{'☆' * (5-p3)}")
    print(f"  Decision Maker  : {p4}/5  {'★' * p4}{'☆' * (5-p4)}")
    print(f"  Warmth          : {p5}/5  {'★' * p5}{'☆' * (5-p5)}")
    print()
    print("=" * 55)

    if total >= 18:
        print("  ★ SCORE 18-25: TOP PRIORITY — respond within 2 hours")
        print("    These leads are worth your full attention right now.")
    elif total >= 12:
        print("  → SCORE 12-17: SCHEDULE A CALL")
        print("    Worth a conversation but qualify further before scoping.")
    else:
        print("  ○ SCORE BELOW 12: NURTURE ONLY")
        print("    Keep in your pipeline but don't deprioritize other work.")

    print()
    print("  Questions to ask on your discovery call:")
    print("  1. 'Walk me through what you're trying to accomplish?'")
    print("  2. 'What's the timeline looking like?'")
    print("  3. 'What range are you comfortable investing to get this done?'")

    print()
    print("Part of the AI Freelancer Swift Start Toolkit")
    print("miloantaeus.gumroad.com/l/xofwuq")

if __name__ == "__main__":
    main()
