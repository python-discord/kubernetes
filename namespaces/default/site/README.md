# Python Discord Site
This folder contains the manifests for Python Discord site.

## Secrets

The deployment expects the following secrets to be available in `site-env`:

| Environment           | Description                                                |
|-----------------------|------------------------------------------------------------|
| DATABASE_URL          | The URL for the Postgresql database.                       |
| METRICITY_DB_URL      | The URL for the Metricity database.                        |
| SECRET_KEY            | Secret key for Django.                                     |
| SENTRY_DSN            | The Sentry Data Source Name.                               |
| GITHUB_APP_KEY        | A PEM key for a GitHub Application.                        |
| GITHUB_APP_ID         | The ID of a GitHub Application (related to the above key). |
