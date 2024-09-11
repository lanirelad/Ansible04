import os
from flask import Flask, request
import socket
import datetime
import random

app = Flask(__name__)
counter = 0

# retrieve the host IP from the inventory file
hostIp = os.getenv('HOST_IP', 'Unknown IP')

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
    global counter
    counter += 1
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    
    return (f"<h1>Ansible 2.1 HW Submission!</h1>"
            f"<p><strong>Linode Host IP:</strong> {hostIp}</p>"
            f"<p><strong>Request Count:</strong> {counter}</p>"
            f"<p><strong>Time of Request:</strong> {current_time}</p>"
            f"<blockquote><i>{random_quote}</i></blockquote>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)