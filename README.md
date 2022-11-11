# Sama AWS Setup

## Requirements

  * Python 3
  * [AWS CLI](https://aws.amazon.com/cli/)
  * Your Sama API key
  * Your Sama Project Id

## Setup

```bash
./sama-aws.py configure
```

Test it

```bash
./sama-aws.py print
```

## Configure AWS CLI / boto3 for sama

Install [AWS CLI](https://aws.amazon.com/cli/)

If it's the first time you use AWS CLI, run the following command with some dummy values so it create the config files.

```
aws configure
```

Look for `Assets S3 URL` in the command output, you will need it later.

Add a sama profile in `~/.aws/config`

```ini
[profile sama]
credential_process = /<absolute-path>/sama-aws.py print
```

Test AWS CLI sama profile

```bash
aws --profile sama sts get-caller-identity 
aws --profile sama s3 ls <Assets S3 URL as printed by the configure command>
```

## Configure Cyberduck

Install [Cyberduck](https://cyberduck.io/)

Run in a shell and let it run. It will refresh the credentials every 45 minutes.

```bash
./sama-aws.py update-credentials-file
```

- Add `S3 (Credentials from AWS Command Line Interface)` bookmark in Cyberduck
- Set profile name as `sama-cyberduck`
- Set path to `Assets S3 URL` as printed by the configure command but without the `s3://` prefix.

After an hour, the temporary credentials will expire in Cyberduck and you will need to reconnect by going back to the landing page.
