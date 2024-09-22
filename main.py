import os
from flask import Flask, request, render_template
import socket
import datetime
import random
import json

app = Flask(__name__)


# retrieve the host IP from the inventory file
host_ip =  os.getenv('HOST_IP', 'Unknown IP')
# initialize the counter var
counter = 0
# just to make it a little interesting
quotes = [
    "Believe you can and you're halfway there.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do something today that your future self will thank you for.",
    "It always seems impossible until it's done.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don’t watch the clock; do what it does. Keep going.",
    "You are never too old to set another goal or to dream a new dream.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "The best way to predict the future is to create it.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us."
]

@app.route('/')
def mainPage():
    global counter, host_ip 
    counter += 1
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    randomQuote = random.choice(quotes)
    return render_template("main.html", hostIp=host_ip, counter=counter, currentTime=currentTime, randomQuote=randomQuote)


# @app.route('/webhook', methods=['POST'])
# def webhookRequest():
#     print(f"Webhook request is being processed", flush=True)
#     return 'Webhook received', 200

@app.route('/webhook', methods=['POST'])
def webhookRequest():
    webhook_data = request.get_json()

    if webhook_data:
        with open('webhook_data.json', 'a') as f:
            json.dump(webhook_data, f, indent=4)
        print("Webhook data received and saved.", flush=True)
        return 'Webhook received and saved', 200

    return 'No data', 400


# route to show webhook payload file
@app.route('/payload')
def show_payload():
    with open('/opt/flaskApp/webhook_data.json', 'r') as f:
        payload_data = f.read()
     # Wrap the log data in a <pre> tag to preserve formatting
    return f"<pre>{payload_data}</pre>"


# route to show log file
@app.route('/log')
def show_log():
    with open('/opt/flaskApp/app.log', 'r') as f:
        log_data = f.read()
     # Wrap the log data in a <pre> tag to preserve formatting
    return f"<pre>{log_data}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)