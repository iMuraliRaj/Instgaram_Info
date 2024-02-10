from flask import Flask,render_template,request,abort
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
import instaloader
import pandas as pd

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def weather():
    username=request.args.get("username")

    # Creating an instance of the Instaloader class
    bot = instaloader.Instaloader()

    try:
        # Loading a profile from an Instagram handle
        profile = instaloader.Profile.from_username(bot.context, username)

        details=[]
        details.append(profile.biography)
        details.append(profile.followers)
        details.append(profile.followees)
        details.append(profile.mediacount)
    except:
        details = ["","","",""]

    return render_template('index.html',data=details)



if __name__ == '__main__':
    app.run(debug=True)
