# Patsy

The deployment for the [Patsy API](https://git.pydis.com/patsy), hosted at https://patsy.pythondiscord.com.

This API is given help channel messages by the bot and stores them in postgres for after-the-fact processing.
The hope with this project is that we can inspect what topics get asked about often in help channels, along with which ones go un-answered the most.

## Secret

It requires a `patsy-env` secret with the values defined [here](https://git.pydis.com/patsy#env-file).
