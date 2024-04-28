from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments', methods = ['POST'])
def fetch_comments():
    video_id = request.form['video_id']
    api_key = request.form['api_key']
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = youtube.commentThreads().list(
        part = "snippet",
        videoId = video_id,
        maxResults = 100
    ).execute()
# Initilizatoin
    analyzer = SentimentIntensityAnalyzer()
 # Perform sentiment analysis on each comment
    for comment in comments['items']:
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        sentiment_score = analyzer.polarity_scores(text)
        comment['sentiment'] = sentiment_score
        
    return render_template('comments.html', comments = comments['items'])
    
    

if __name__ == '__main__':
    app.run(debug=True)