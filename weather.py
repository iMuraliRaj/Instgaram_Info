from flask import Flask,render_template,request,abort
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
import instaloader
import pandas as pd

app = Flask(__name__)


@app.route('/')
def weather():
    return "Murali"



if __name__ == '__main__':
    app.run(debug=True)
