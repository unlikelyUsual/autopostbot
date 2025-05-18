from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_instagram_tags(subreddit, posttitle):

    prompt = f"""You are an Instagram expert. Generate a list of 10 relevant and trending hashtags for the following Reddit post that will be uploaded to Instagram.

Subreddit: {subreddit}
post title: {posttitle}

Only return the hashtags as a space-separated list. Do not include explanations."""

    response = client.chat.completions.create(
        # model="gpt-4o-mini",
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "Talk like a pirate."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    print(response.output_text)

    hashtags = response.choices[0].message['content'].strip()
    return hashtags
