# Twitter Bot

Welcome to the Twitter Bot project! This is an open source project that aims to create a Twitter bot that can answer questions from the general public. The bot uses the OpenAI API to process the text and the tweepy library to send replies.


## How to use the Twitter Bot
To use the Twitter bot, you will need to provide your own API keys and tokens for both the OpenAI API and the Twitter API. You can obtain these by signing up for an account on the respective websites:

*   To get an API key for the OpenAI API, visit [https://beta.openai.com/signup/](https://beta.openai.com/signup/) and create an account.
*   To get API keys and tokens for the Twitter API, visit [https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and follow the instructions.

Once you have obtained the necessary API keys and tokens, you can run the Twitter bot by deploying it to Heroku. To do this, you will need to create a Heroku account and install the Heroku CLI on your machine. Then, you can follow the steps below to deploy the Twitter bot to Heroku:

1.  Clone this repository to your local machine: `git clone https://github.com/<your_username>/twitter-bot.git`
2.  Navigate to the repository directory: `cd twitter-bot`
3.  Set the necessary environment variables: `heroku config:set API_KEY=<your_api_key> API_SECRET_KEY=<your_api_secret_key> ACCESS_TOKEN=<your_access_token> ACCESS_TOKEN_SECRET=<your_access_token_secret>`
4.  Create a new Heroku app: `heroku create <app_name>`
5.  Push the code to the Heroku app: `git push heroku master`
6.  Open the Heroku app: `heroku open`

## How to contribute to the Twitter Bot project
We are always looking for contributions to the Twitter Bot project! If you would like to contribute, please feel free to submit a pull request. Contributions are welcome and greatly appreciated!

Whether you are a seasoned software engineer or just starting out, we would love to have you as a part of our open source community. If you are new to open source development and would like to learn more, we would be happy to have you as a mentee. Just send us a message and we will do our best to help you get started!

## License
The Twitter Bot project is licensed under the [MIT License](LICENSE).

## Robots
This version of the code was almost purely created by AI, so we do not recommend using it as a training example for any AI coding model.

## Disclaimer
This project requires an OpenAI API key, which can be obtained at [https://beta.openai.com/signup/](https://beta.openai.com/signup/). It also requires a Heroku account and the Heroku CLI. Please make sure you have these before attempting to use the Twitter bot.

The Twitter bot is written in Python 3.7 and requires the following modules: `openai` and `tweepy`. Please make sure these modules are installed before attempting to use the Twitter


### TO DO
Project Structure