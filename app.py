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


















# from googleapiclient.discovery import build

# # API key obtained from Google Cloud Console
# API_KEY = "AIzaSyD5Ir0JthOBP7eQXpcUDIWJLCra7z4Au6Q"

# # Create a service object for the YouTube Data API
# youtube = build('youtube', 'v3', developerKey=API_KEY)

# # Specify the parameters for the comment request
# video_id = "wejaREXePtg"
# max_results = 50  # Maximum number of comments to fetch

# # Call the commentThreads().list() method to fetch comments
# comments = youtube.commentThreads().list(
#     part = "snippet",
#     videoId = video_id,
#     maxResults = max_results
# ).execute()

# # Iterate through the comments and print them
# for comment in comments['items']:
#     snippet = comment['snippet']['topLevelComment']['snippet']
#     author = snippet['authorDisplayName']
#     text = snippet['textDisplay']
#     print(f"{author}: {text}")

# # print(comments)