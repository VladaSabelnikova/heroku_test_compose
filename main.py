import os

from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, всем!"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    serve(app, port=port, host='0.0.0.0')
