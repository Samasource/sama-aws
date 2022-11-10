# sama-setup


## Setup

Create a file in `~/.sama.json

```
{
  "apiKey": "<Your Sama API Key>",
}
```

```
# Not yet done
./sama-aws.py configure
```


Print temporary credentials
```
./sama-aws.py print --project-id 9888
```

## Configure AWS CLI / boto3

Add a sama profile in `~/.aws/config`
```
[profile sama]
credential_process = /<absolute-path>/sama-aws.py print --project-id 9888
```

Test AWS CLI sama profile
```
aws sts get-caller-identity --profile sama
aws s3 ls s3://sama-client-assets/<client_id>/
```

## Configure for cyberduck

Run in a shell and let it run. It will refresh the credentials every 45 minutes.

```
./sama-aws.py update-credentials-file --project-id 9888
```

Configure cyberduck using S3 (Credentials from AWS Command Line Interface)
Set profile name as `sama-cyberduck`.
Set path to sama-client-assets/<client_id>
