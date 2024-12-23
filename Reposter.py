from flask import Flask, request
import logging
import requests
import os

app = Flask(__name__)

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)
bot_token = '7201537354:AAFwLFM_AICUWSYnUg79jPgc4FWVJiLbEdk'
#Chat ID of the group where the bot will post(Profit Pulse Alerts)
chat_id = '-1002318178963'



def botSendMessage(message):
    # URL for the sendMessage API endpoint
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    # Send the message using a POST request

    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Message sent successfully:", response.json())
    except requests.exceptions.RequestException as e:
        logging.info(f"Error occurred:{e.response.text}")

# Bot token from Telegram
BOT_TOKEN = os.environ.get(bot_token)

@app.route("/webhook", methods=["POST"])
def webhook():

    try:
        # Parse the incoming request JSON
        update = request.get_json()
        logging.info(f"Received update: {update}")


        # Check if the update contains a message
        if update['channel_post']['sender_chat']['title'] == "Signal Hub":
            botSendMessage(update['channel_post']['text'])
            chat_title = update['channel_post']['sender_chat']['title']
            logging.info(f"New message from chat: {chat_title}")
            print("new message")  # Print "new message" to the console

        return "OK", 200
    except Exception as e:
        logging.error(f"Error handling update: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)