import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
import pytz

# 🔐 Use Slack bot token from environment variable
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = "C08PAJG9614"  # Replace with your actual channel ID

# ✅ Debug: Check if token is set
if not SLACK_BOT_TOKEN:
    print("❌ SLACK_BOT_TOKEN is not set!")
else:
    print("✅ SLACK_BOT_TOKEN loaded.")

client = WebClient(token=SLACK_BOT_TOKEN)

# 🧠 Helper to send message
def send_message(text):
    try:
        response = client.chat_postMessage(channel=CHANNEL_ID, text=text)
        print("✅ Message sent! Timestamp:", response["ts"])
    except SlackApiError as e:
        print("❌ Slack API Error:")
        print(e.response.data)

# 🎭 Emoji Map
emoji_map = {
    "John": "🐶",
    "Ryan": "🦈",
    "Taylor": "🐯",
    "Colin": "👻",
    "Josh": "🎩",
    "Team Effort": "🤝"
}

# 🎉 Holiday Dates
holiday_map = {
    "01-01": "New Year's Day",
    "01-20": "Martin Luther King Day",
    "02-17": "Presidents' Day",
    "04-18": "Good Friday",
    "05-26": "Memorial Day",
    "06-19": "Juneteenth",
    "07-04": "Independence Day",
    "09-01": "Labor Day",
    "11-27": "Thanksgiving Day",
    "11-28": "Friday after Thanksgiving",
    "12-25": "Christmas Day",
}

# 🎄 Christmas Break (range check)
def is_christmas_break(date):
    return date >= datetime(date.year, 12, 22) and date <= datetime(date.year, 12, 26)

# 🛑 Send holiday message
def holiday_message(name):
    message = f"📅 *{name.upper()} — HOLIDAY!* 🎉"
    print(f"📨 Sending holiday message: {message}")
    send_message(message)

# 🗓 Daily schedules
def monday_schedule():
    message = (
        "📅 *Monday:*\n\n"
        f"*Odds & Ends:* {emoji_map['John']} John\n"
        f"*Front Liine 9-1:* {emoji_map['Ryan']} Ryan\n"
        f"*Front Liine 1-5:* {emoji_map['Taylor']} Taylor\n"
        f"*After Hours:* {emoji_map['Colin']} Colin"
    )
    send_message(message)

def tuesday_schedule():
    message = (
        "📅 *Tuesday:*\n\n"
        f"*Odds & Ends:* {emoji_map['Taylor']} Taylor\n"
        f"*Front Liine 9-1:* {emoji_map['Colin']} Colin\n"
        f"*Front Liine 1-5:* {emoji_map['John']} John\n"
        f"*After Hours:* {emoji_map['Ryan']} Ryan"
    )
    send_message(message)

def wednesday_schedule():
    message = (
        "📅 *Wednesday:*\n\n"
        f"*Odds & Ends:* {emoji_map['Colin']} Colin\n"
        f"*Front Liine 9-1:* {emoji_map['Taylor']} Taylor\n"
        f"*Front Liine 1-5:* {emoji_map['Ryan']} Ryan\n"
        f"*After Hours:* {emoji_map['John']} John"
    )
    send_message(message)

def thursday_schedule():
    message = (
        "📅 *Thursday:*\n\n"
        f"*Odds & Ends:* {emoji_map['Ryan']} Ryan\n"
        f"*Front Liine 9-1:* {emoji_map['John']} John\n"
        f"*Front Liine 1-5:* {emoji_map['Colin']} Colin\n"
        f"*After Hours:* {emoji_map['Taylor']} Taylor"
    )
    send_message(message)

def friday_schedule():
    message = (
        "📅 *Friday:*\n\n"
        f"*Odds & Ends:* {emoji_map['Team Effort']} Team Effort\n"
        f"*9-11:* {emoji_map['Taylor']} Taylor\n"
        f"*11-1:* {emoji_map['Colin']} Colin\n"
        f"*1-3:* {emoji_map['John']} John\n"
        f"*3-5:* {emoji_map['Ryan']} Ryan"
    )
    send_message(message)

# 📆 Run the schedule for today
def main():
    eastern = pytz.timezone("US/Eastern")
    today = datetime.now(eastern)
    today_str = today.strftime("%m-%d")
    weekday = today.strftime("%A")

    print(f"📆 Running schedule for {weekday} ({today_str})")

    if today_str in holiday_map:
        print(f"🎉 Today is a fixed-date holiday: {holiday_map[today_str]}")
        holiday_message(holiday_map[today_str])
        return

    if is_christmas_break(today):
        print("🎄 Today falls within Christmas Break.")
        holiday_message("Christmas Break")
        return

    print(f"🧾 Proceeding to send daily schedule for {weekday}")

    if weekday == "Monday":
        monday_schedule()
    elif weekday == "Tuesday":
        tuesday_schedule()
    elif weekday == "Wednesday":
        wednesday_schedule()
    elif weekday == "Thursday":
        thursday_schedule()
    elif weekday == "Friday":
        friday_schedule()
    else:
        print("❌ No schedule to send today (Weekend).")

if __name__ == "__main__":
    main()
