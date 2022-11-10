# sama-setup

## Setup

You will need your Sama API key and project id.

```bash
./sama-aws.py configure
```

Print temporary credentials

```bash
./sama-aws.py print --project-id 9888
```

## Configure AWS CLI / boto3 for sama

Add a sama profile in `~/.aws/config`

```ini
[profile sama]
credential_process = /<absolute-path>/sama-aws.py print --project-id 9888
```

Test AWS CLI sama profile

```bash
aws sts get-caller-identity --profile sama
aws s3 ls s3://sama-client-assets/<client_id>/
```

## Configure for cyberduck

Run in a shell and let it run. It will refresh the credentials every 45 minutes.

```bash
./sama-aws.py update-credentials-file --project-id 9888
```

- Add `S3 (Credentials from AWS Command Line Interface)` bookmark in Cyberduck
- Set profile name as `sama-cyberduck`
- Set path to sama-client-assets/<client_id>
