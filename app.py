from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Xin cam on thay va cac ban da xem!!'