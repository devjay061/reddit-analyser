import requests
from textblob import TextBlob
import matplotlib.pyplot as plt

def display_posts(posts):
    for post in posts:
        print(f"\nTitle: {post['title']}")
        print(f"Score: {post['score']}")
        print(f"Comments: {post['num_comments']}")
        print(f"Sentiment: {post['sentiment']} (Polarity: {post['polarity']:.2f})")
        print("-" * 40)

def visualise(posts):
    #pie chart to show the distribution of sentiments
    sentiments = [post['sentiment'] for post in posts]
    labels = ['Positive', 'Negative', 'Neutral']
    counts = [sentiments.count(label) for label in labels]
    plt.pie(counts,labels=labels, autopct='%1.1f%%')
    plt.title('Sentiment Distribution')
    plt.show()
    

    #bar chart - top posts by score 
    titles=[post['title'][:30]+'...' for post in posts]
    scores=[post['score'] for post in posts]
    plt.figure() #new figure for the bar chart so it doesn't overlap with the pie chart
    plt.barh(titles, scores, color='skyblue')
    plt.xlabel('Score')
    plt.title('Posts by Score')
    plt.tight_layout() #adjust layout to prevent overlap of labels
    plt.show()

def analyse_sentiment(posts):
    for post in posts:
        blob=TextBlob(post['title'])
        polarity=blob.sentiment.polarity
        if polarity > 0:
            sentiment='Positive'
        elif polarity < 0:
            sentiment='Negative'
        else:
            sentiment='Neutral'

        post['sentiment']=sentiment
        post['polarity']=polarity
    return posts


def fetch_posts(headers):
    subreddit = input("Enter the subreddit you want to fetch posts from: ")
    category = input("Enter the category (hot, new, top): ")
    if category not in ["hot", "new", "top"]:
        print("Invalid category. Defaulting to hot.")
        category = "hot"
    limit = int(input("Enter the number of posts to fetch: "))
    url = f"https://www.reddit.com/r/{subreddit}/{category}.json?limit={limit}" #default format of a url to fetch posts from reddit
    response = requests.get(url, headers=headers)
    data=response.json()
    posts=[]

    for post in data["data"]["children"]:
        p=post["data"]
        posts.append({
            "title": p["title"],
            "score": p["score"],
            "url": p["url"],
            'num_comments': p['num_comments']
        })

    return posts

def main():
    while True:
        print("Welcome to the Reddit Sentiment Analyser!")
        print("1. Fetch and analyse posts")
        print("2. Visualise results")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            global posts
            posts=fetch_posts(headers)
            posts=analyse_sentiment(posts)
            display_posts(posts)

        elif choice == '2':
            if not posts:
                print("No posts to visualise. Please fetch and analyse posts first.")   
            else:
                visualise(posts)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
           
    

#main
headers = {"User-Agent": "data-analytics-project/0.1"}
posts = []
main()
