# Reddit Sentiment Analyser

A Python CLI tool that analyses sentiment of Reddit posts from any subreddit.

## Features
- Fetch posts from any subreddit (hot/new/top)
- Sentiment analysis on post titles (Positive/Negative/Neutral)
- Pie chart showing sentiment distribution
- Bar chart ranking posts by score

## Libraries Used
- `requests` — fetch data from Reddit's public API
- `textblob` — sentiment analysis
- `matplotlib` — data visualisation

## How to Run
1. Install dependencies:
   pip install requests textblob matplotlib
2. Run the script:
   python analyser.py

## Example Output
Subreddit: python | Category: top | Posts: 10
