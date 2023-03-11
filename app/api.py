from flask import Flask
from solar import readData

app = Flask(__name__)

IP = "1.2.3.4"
PORT = 0000


@app.route("/")
def root():
    return "solar power plant status api up and running"

@app.route("/status")
def get_status():
    return readData(IP, PORT)