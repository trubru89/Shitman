import os
from flask import Flask
from shitman import shitman


app = Flask(__name__)


@app.route("/")
def shitman_the_game():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
