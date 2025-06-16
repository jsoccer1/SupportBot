import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
import pytz

# 🔐 Use Slack bot token from environment variable
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = "C07NHCHDAC8"  # Replace with your actual channel ID

client = WebClient(token=SLACK_BOT_TOKEN)

# 🧠 Helper to send message
def send_message(text):
    try:
        response = client.chat_postMessage(channel=CHANNEL_ID, text=text)
        print("✅ Message sent! Timestamp:", response["ts"])
    except SlackApiError as e:
        print("❌ Error sending message:", e.response["error"])

# 🎭 Emoji Map
emoji_map = {
    "John": "🐶",
    "Ryan": "🦈",
    "Taylor": "🐯",
    "Colin": "👻",
    "Josh": "🎩",
    "Team Effort": "🤝"
}

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
    today = datetime.now(eastern).strftime("%A")

    if today == "Monday":
        monday_schedule()
    elif today == "Tuesday":
        tuesday_schedule()
    elif today == "Wednesday":
        wednesday_schedule()
    elif today == "Thursday":
        thursday_schedule()
    elif today == "Friday":
        friday_schedule()
    else:
        print("❌ No schedule to send today.")

if __name__ == "__main__":
    main()
