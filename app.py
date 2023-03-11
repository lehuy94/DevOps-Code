from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Cam on thay va cac ban da xem!!'