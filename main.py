import os
from flask import Flask, request, render_template
import socket
import datetime
import random

app = Flask(__name__)


# retrieve the host IP from the inventory file
host_ip = None
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
    host_ip = os.getenv('HOST_IP', 'Unknown IP')
    return render_template("main.html", hostIp=host_ip,counter=counter,currentTime=currentTime,randomQuote=randomQuote)

#
# @app.route('/webhook', method=['POST'])
# def webhookRequest():
#     print(f"Webhook request is being processed", flush=True)
#     return 'Webhook received', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)