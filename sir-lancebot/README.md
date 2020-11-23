## Sir Lancebot
```
Oh brave Sir Lancebot! 

Whereat he turned and stood with folded arms and numerous antennae,
"Why frown upon a friend? Few live that have too many."
A weary-waiting optical array, now calibrated to a sad wrath. 
Hereafter, thus t'was with him that we hath forged our path.
```

## Secrets
This deployment expects a number of secrets and environment variables to exist in a secret called `sir-lancebot-env`.


| Environment           | Description                               |
|-----------------------|-------------------------------------------|
| BOT_SENTRY_DSN        | The DSN for the Sentry project.           |
| BOT_TOKEN             | The bot token to run the bot on.          |
| BOT_DEBUG             | Should the bot start in DEBUG mode?       |
| REDIS_PASSWORD        | The password for the Redis service.       |
| REDIS_HOST            | The hostname for the Redis service.       |
| REDIS_PORT            | The port that the Redis service runs on.  |
| AOC_JOIN_CODE         | Public leaderboard join code for AoC.     |
| AOC_JOIN_STAFF_CODE   | Staff leaderboard join code for AoC.      |
| AOC_SESSION_COOKIE    | Advent of Code session cookie.            |
| GITHUB_TOKEN          | GitHub access token, for Hacktoberstats.  |
| TMDB_TOKEN            | Token for TMBD. Used for scarymovie.py.   |
| TMDB_API_KEY          | API key for TMBD.                         |
| IGDB_API_KEY          | API key for IGDB - used to find games.    |
| OMDB_API_KEY          | API key for OMDB - used with snake cog.   |
| WOLFRAM_API_KEY       | API key for Wolfram Alpha.                |
| GIPHY_TOKEN           | API key for Giphy.                        |
| YOUTUBE_API_KEY       | API key for YouTube.                      |
| NASA_API_KEY          | API key for NASA.                         |

