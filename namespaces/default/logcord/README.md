# Logcord
A web viewer for Discord message logs, hosted at https://logcord.pythondiscord.com.

## Secrets
This deployment needs one secret named `logcord-secret-env`, with the following values:

| Environment | Description          |
|-------------|----------------------|
| MONGO_HOST  | MongoDB database URI |
