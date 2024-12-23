from flask import Flask, request
import logging
import os

app = Flask(__name__)

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

# Bot token from Telegram
BOT_TOKEN = os.environ.get("7201537354:AAFwLFM_AICUWSYnUg79jPgc4FWVJiLbEdk")

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Parse the incoming request JSON
        update = request.get_json()
        logging.info(f"Received update: {update}")

        # Check if the update contains a message
        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            logging.info(f"New message from chat: {chat_id}")
            print("new message")  # Print "new message" to the console

        return "OK", 200
    except Exception as e:
        logging.error(f"Error handling update: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)