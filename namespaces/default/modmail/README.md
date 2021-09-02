# Modmail

This folder contains the manifests for our Modmail service.

## Secrets

The services require one shared secret called `modmail` containing the following:

| Key                   | Value                            | Description                                   |
| --------------------- | -------------------------------- | --------------------------------------------- |
| `DISABLE_AUTOUPDATES` | `yes`                            | Auto-updates breaks in production             |
| `GUILD_ID`            | Snowflake of Discord guild       | Guild to respond to commands in               |
| `LOG_URL`             | URL of the web portal            | Used for generating links on the bot          |
| `MONGO_URI`           | MongoDB connection URI           | Used for storing data                         |
| `OWNERS`              | Comma separated list of user IDs | Used for granting high permissions on the bot |
| `TOKEN`               | Discord Token                    | Used to connect to Discord                    |
