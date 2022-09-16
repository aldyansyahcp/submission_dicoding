from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bes
from requests import get

app = Flask(__name__)

@app.route("/")
def maink():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
