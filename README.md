# Sama AWS Setup

## Requirements

  * Python 3
  * [AWS CLI](https://aws.amazon.com/cli/)
  * Your Sama API key
  * Your Sama Project Id

## Setup

Install Python 3.
Install [AWS CLI](https://aws.amazon.com/cli/)

This will create a `sama` AWS CLI profile.

```bash
./sama-aws.py configure
```

Look for `Assets S3 URL` in the command output, you will need it later.

Test it

```bash
./sama-aws.py print
```

Test AWS CLI sama profile

```bash
aws --profile sama sts get-caller-identity 
aws --profile sama s3 ls <Assets S3 URL as printed by the configure command>
```

## Configure Cyberduck

Install [Cyberduck](https://cyberduck.io/)

Run the following command in a shell. It will create or update the `sama-cyberduck` AWS profile.

```bash
./sama-aws.py update-credentials-file
```

- Add `S3 (Credentials from AWS Command Line Interface)` bookmark in Cyberduck
- Set profile name as `sama-cyberduck`
- Set path to `Assets S3 URL` as printed by the configure command but without the `s3://` prefix.

After an hour, the temporary credentials will expire in Cyberduck. You will need to rum the script aign and reconnect by going back to the Cyberduck landing page.
