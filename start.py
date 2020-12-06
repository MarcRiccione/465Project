from flask import Flask, render_template, session, request, jsonify, Response, flash, redirect, url_for
import requests
import re
import time
from main import *

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    #print(text)
    result = main(text)
    return render_template('result.html', result = result, text = text)


@app.route('/information')
def information():
    return render_template('information.html')

    
if __name__ == '__main__':
    app.run()

