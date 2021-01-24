# Blackbox
These manifests provision a CronJob for blackbox, our database backup tool.

You can find the repository for blackbox at [lemonsaurus/blackbox](https://github.com/lemonsaurus/blackbox).

## Secrets
The secrets required for blackbox are pulled from various sources:

| Variable                       | Environment       | Description            |
|--------------------------------|-------------------|------------------------|
| **POSTGRES_USER**              | postgres-env      | Postgres username      |
| **POSTGRES_PASSWORD**          | postgres-env      | Postgres password      |
| **REDIS_PASSWORD**             | redis-credentials | Redis password         |
| **MONGO_INITDB_ROOT_USERNAME** | mongo-credentials | MongoDB username       |
| **MONGO_INITDB_ROOT_PASSWORD** | mongo-credentials | MongoDB password       |
| **AWS_ACCESS_KEY_ID**          | s3-credentials    | Access key for S3      |
| **AWS_SECRET_ACCESS_KEY**      | s3-credentials    | Secret key for S3      |
| **DEVOPS_WEBHOOK**             | discord-webhooks  | Webhook for #dev-ops   |
