from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url).text) # Fetch meme data from the API
    meme_large = response['preview'][-2] # Get the second last image in the preview list
    subreddit = response['subreddit'] # Get the subreddit from which the meme was fetched
    return meme_large, subreddit

@app.route('/')
def index():
    meme_pic, subreddit = get_meme()
    return render_template('index.html', meme_pic=meme_pic, subreddit=subreddit) # Pass meme picture and subreddit to the template


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
# This code sets up a Flask application that fetches a meme from an API and displays it on the index page.