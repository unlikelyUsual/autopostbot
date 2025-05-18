import praw
import os
from dotenv import load_dotenv
from reddit.download import download_video

load_dotenv()

def get_reddit_videos(sub_reddits, num_top_posts=3):
    reddit = praw.Reddit(
        client_id=os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        user_agent=os.environ.get("REDDIT_USER_AGENT"),
    )

    video_posts = []

    for subreddit_name in sub_reddits:
        try:
            subreddit = reddit.subreddit(subreddit_name)
            top_posts = subreddit.top(limit=num_top_posts,time_filter='day')
            for post in top_posts:
                if post.is_video and not post.over_18:
                    video_posts.append({
                        "title": post.title,
                        "url": post.url,
                        "subreddit": subreddit_name,
                        "score": post.score,
                    })
        except Exception as e:
            print(f"Error fetching from subreddit {subreddit_name}: {e}")

    # Sort the video posts by score (highest score first)
    sorted_video_posts = sorted(video_posts, key=lambda x: x["score"], reverse=True)
    return sorted_video_posts

def get_and_download_videos():
    print("🔍 Fetching videos from Reddit...")
    to_fetch_from = ["Damnthatsinteresting", "funny", "aww", "animalsdoingstuff" ,"nextfuckinglevel", "oddlysatisfying", "Unexpected", "MadeMeSmile", "ContagiousLaughter"]
    # to_fetch_from = ["Damnthatsinteresting"]
    num_top_posts_to_fetch = int(os.environ.get("REDDIT_MAX_POSTS"))

    # Get top based on score
    top_video_posts = get_reddit_videos(to_fetch_from, num_top_posts_to_fetch)

    if top_video_posts:
        for i,post in enumerate(top_video_posts):
            video_url = post['url']
            print(video_url)
            sanitized_title = "".join(c if c.isalnum() else "_" for c in post['title'][:50])
        return download_video(video_url, sanitized_title)
    else:
        print("No video posts found in the specified sub reddits")
        return None