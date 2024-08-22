# Twitter API v2 Tweepy Integration

This repository demonstrates how to post a tweet using the Tweepy library with Twitter API v2. The script authenticates using OAuth 2.0 Bearer Token and posts a simple tweet.

## Prerequisites

- Python 3.6+
- Tweepy library
- Twitter Developer Account

## Setup

### 1. Enable Developer Account

Follow the instructions to enable your developer account:
[Enable Developer Account](https://developer.x.com/en/docs/authentication/oauth-1-0a/api-key-and-secret)

### 2. Login to Developer Account

Login to your developer account to get your API credentials:
[Developer Dashboard](https://developer.x.com/en/portal/dashboard)

### 3. Install Tweepy

Install the Tweepy library using pip:

```sh
pip install tweepy
```

### Usage
1. Replace Credentials
```sh
API_KEY = 'API_KEY'
API_KEY_SECRET = 'API_KEY_SECRET'
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
BEARER_TOKEN = 'BEARER_TOKEN'
```

2. Run the Script
run the script:
```sh
python main.py
```

### License
This project is licensed under the MIT License.
