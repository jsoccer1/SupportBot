import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 🔐 Slack token from GitHub Secrets (use SLACK_BOT_TOKEN secret)
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = "C08PAJG9614"  # Replace with your channel ID

if not SLACK_BOT_TOKEN:
    print("❌ SLACK_BOT_TOKEN is not set!")
    exit(1)

client = WebClient(token=SLACK_BOT_TOKEN)

def send_message(text):
    try:
        response = client.chat_postMessage(channel=CHANNEL_ID, text=text)
        print("✅ Message sent! Timestamp:", response["ts"])
    except SlackApiError as e:
        print("❌ Slack API Error:")
        print(e.response.data)
        exit(1)

if __name__ == "__main__":
    message = "Please send any weekly updates or highlights from this week as a reply :party_cat:"
    send_message(message)
