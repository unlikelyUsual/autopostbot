from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="hyperbolic",
    api_key=os.environ.get("HUGGING_FACE_API_KEY"),
)

def generate_instagram_tags(subreddit, posttitle):

    prompt = f"""You are an Instagram expert. Generate a list of 10 relevant and trending hashtags for the following Reddit post that will be uploaded to Instagram.

Subreddit: {subreddit}
post title: {posttitle}

Only return the hashtags as a space-separated list. Do not include explanations."""

    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )


    hashtags = completion.choices[0].message.content.strip()
    return hashtags
