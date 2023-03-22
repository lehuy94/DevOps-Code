from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Day la bai test thu!!'