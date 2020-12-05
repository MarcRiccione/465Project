from flask import Flask
import requests
#form bs4 import BeautifulSoup, SoupStrainer
import re
import time
app = Flask(__name__)


@app.route('/')
def start():

    return "Hello World!"

if __name__ == '__main__':
    app.run()

