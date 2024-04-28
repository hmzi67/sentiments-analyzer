# YouTube Comments Sentiment Analyzer with Flask

This project is a YouTube comments sentiment analyzer built using Flask. It allows users to fetch comments from a YouTube video and analyze their sentiments using VADER (Valence Aware Dictionary and sEntiment Reasoner).

## Features

- Fetch YouTube comments by providing the video ID and your YouTube Data API Key.
- Perform sentiment analysis on the fetched comments.
- Display comments along with sentiment analysis results in a user-friendly format.

## Prerequisites

- Python installed on your system.
- Flask (`pip install Flask`)
- google-api-python-client (`pip install google-api-python-client`)
- vaderSentiment (`pip install vaderSentiment`)

## How to Use

1. Clone the repository.
2. Install the required dependencies.
3. Run the Flask app (`python app.py`).
4. Open your browser and navigate to `http://localhost:5000`.
5. Enter the YouTube video ID and your YouTube Data API Key.
6. Click the "Submit" button to fetch comments and view sentiment analysis results.

## File Structure

- `app.py`: Flask application file containing routes for fetching comments and performing sentiment analysis.
- `index.html`: HTML template for the homepage where users can input the video ID and API Key.
- `comments.html`: HTML template for displaying comments along with sentiment analysis results.

## Technologies Used

- Python
- Flask
- Google API Client Library
- VADER Sentiment Analysis

## Author

- [Hamza Waheed Abbasi](https://github.com/hmzi67)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
