## Sir-Robin
Deployment file for @Sir-Robin, the not-quite-so-bot as Sir Lancebot, is our humble events bot.
He is tasked with dealing with all the things that the event team can throw at it!

## Secrets
This deployment expects a number of secrets/environment variables to exist in a secret called `sir-robin-env`.

The secrets are:
```
BOT_TOKEN - The Discord bot token for Sir Robin to connect to Discord with
SITE_URL - The base URL for our website.
SITE_API_TOKEN - The token to access the site API.
BOT_DEBUG - Whether debug is enabled (true/false).
```

Sir Robin also requires the below secret to redis, which is pulled from the `redis-credentials` secret.
```
REDIS_PASSWORD - The password to redis
```
