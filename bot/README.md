## Bot

Deployment file for @Python, our valiant community bot and workhorse.

## Secrets
This deployment expects a number of secrets and environment variables to exist in a secret called `bot-env`.


| Environment           | Description                               |
|-----------------------|-------------------------------------------|
| BOT_API_TOKEN         | The token to access our API.              |
| BOT_TOKEN             | The bot token to run the bot on.          |
| REDDIT_CLIENT_ID      | The client ID to access the reddit API    |
| REDDIT_SECRET         | The client secret for the Reddit API      |
| REDIS_PASSWORD        | The password to access Redis              |
| SITE_URL              | The base URL for our website.             |
| METABASE_USERNAME     | Username for Metabase                     |
| METABASE_PASSWORD     | Password for Metabase                     |
| BOT_DEBUG             | Debug mode true/false                     |
