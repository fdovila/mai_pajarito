import os
from src.twitter_bot import TwitterBot

api_key = os.environ["API_KEY"]
api_secret_key = os.environ["API_SECRET_KEY"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

bot = TwitterBot(api_key, api_secret_key, access_token, access_token_secret)

def app():
    bot.run()