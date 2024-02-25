This repository contains a Python script for a Reddit bot designed to scan comments in a specified subreddit and reply to comments that match a predefined search string.


Installation
Clone this repository to your local machine.
Ensure you have Python installed.
Install the required Python dependencies by running:
Copy code
pip install praw
Set up the Reddit API credentials and bot configuration as described below.
Configuration
Navigate to the Reddit Developer Apps page and create a new app.

Obtain the following details:

REDDIT_CLIENT_ID: Client ID provided by Reddit for your app.
REDDIT_CLIENT_SECRET: Client secret provided by Reddit for your app.
REDDIT_USERNAME: Your Reddit username.
REDDIT_PASSWORD: Your Reddit password.
REDDIT_USER_AGENT: A unique identifier for your bot.
TARGET_SUBREDDIT: The subreddit where you want the bot to operate.
TARGET_STRING: The search string that the bot will look for in comments.
REPLY_MESSAGE: The message the bot will reply with to matching comments.
SLEEP_DURATION: Time interval between bot runs in seconds.
Set these values in the config.py file accordingly.

Usage
Run the bot script by executing the file.
The bot will log in to Reddit using the provided credentials and start scanning comments in the specified subreddit.
Whenever the bot finds a comment containing the target string, it will reply with the predefined message.
The bot will continue to run indefinitely, periodically scanning for new comments as per the specified sleep duration.
