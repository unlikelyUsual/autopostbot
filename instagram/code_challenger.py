import email
import imaplib
import re
from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice
import os

load_dotenv()

CHALLENGE_EMAIL = os.environ.get("CHALLENGE_EMAIL")
CHALLENGE_PASSWORD = os.environ.get("CHALLENGE_PASSWORD")

def get_code_from_email(username):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(CHALLENGE_EMAIL, CHALLENGE_PASSWORD)
    mail.select("inbox")
    result, data = mail.search(None, "(UNSEEN)")
    assert result == "OK", "Error1 during get_code_from_email: %s" % result
    ids = data.pop().split()
    for num in reversed(ids):
        mail.store(num, "+FLAGS", "\\Seen")  # mark as read
        result, data = mail.fetch(num, "(RFC822)")
        assert result == "OK", "Error2 during get_code_from_email: %s" % result
        msg = email.message_from_string(data[0][1].decode())
        payloads = msg.get_payload()
        if not isinstance(payloads, list):
            payloads = [msg]
        code = None
        for payload in payloads:
            body = payload.get_payload(decode=True).decode()
            if "<div" not in body:
                continue
            match = re.search(">([^>]*?({u})[^<]*?)<".format(u=username), body)
            if not match:
                continue
            print("Match from email:", match.group(1))
            match = re.search(r">(\d{6})<", body)
            if not match:
                print('Skip this email, "code" not found')
                continue
            code = match.group(1)
            if code:
                return code
    return False

def challenge_code_handler(username, choice):
    if choice == ChallengeChoice.EMAIL:
        return get_code_from_email(username)
    return False


if __name__ == "__main__":
    cl = Client()
    cl.challenge_code_handler = challenge_code_handler
    cl.login(os.environ.get("INSTA_USER_USERNAME"), os.environ.get("INSTA_USER_PASSWORD"))