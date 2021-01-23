# Redash

Redash is our database analysis tool for investigating PostgreSQL, Prometheus, Graphite and MongoDB.

## Environmment

There is little setup required for Redash, though there are some environment variables that should be created through a secret.

| Environment variable name    | Recommended                                                           | Description                                        |
| ---------------------------- | --------------------------------------------------------------------- | -------------------------------------------------- |
| `REDASH_COOKIE_SECRET`       | A random, long string                                                 | The secret that is used for signing user sessions  |
| `REDASH_DATABASE_URL`        | PostgreSQL connection string                                          | The primary database for Redash storage            |
| `REDASH_ENFORCE_HTTPS`       | True                                                                  | Whether Redash should perform HTTPS upgrades       |
| `REDASH_HOST`                | Hostname of running server (e.g. `https://redash.pythondiscord.com/`) | Location where Redash can be reached               |
| `REDASH_MAIL_DEFAULT_SENDER` | `redash@domain.com`                                                   | Sender value for outgoing mail                     |
| `REDASH_MAIL_PASSWORD`       | Password for mail account                                             | Password for Redash mail account for outgoing mail |
| `REDASH_MAIL_PORT`           | 587                                                                   | Port for SMTP                                      |
| `REDASH_MAIL_SERVER`         | SMTP server address                                                   | SMTP for outgoing mail                             |
| `REDASH_MAIL_USE_TLS`        | True                                                                  | Secure email using TLS                             |
| `REDASH_MAIL_USERNAME`       | Username for SMTP                                                     | Username for SMTP server used for outgoing mail    |
| `REDASH_REDIS_URL`           | Address for Redis                                                     | Used by Redash for job queues for workers          |

## Provisioning

Run `kubectl apply -f .` inside this folder after setting up the above environment variables in a secret named `redash-secrets`.

Redash sits at https://redash.pythondiscord.com/
