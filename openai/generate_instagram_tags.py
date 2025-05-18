import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_instagram_tags(title, subreddit):
    prompt = f"""You are an Instagram expert. Generate a list of 10 relevant and trending hashtags for the following Reddit post that will be uploaded to Instagram.

Reddit Title: "{title}"
Subreddit: {subreddit}

Only return the hashtags as a space-separated list. Do not include explanations."""

    response = openai.ChatCompletion.create(
        model="gpt-4o mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    hashtags = response.choices[0].message['content'].strip()
    return hashtags


generate_instagram_tags("","")
