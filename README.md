# sama-setup


## Setup

./sama-aws.py configure

Print temporary credentials
```
./sama-aws.py --credential-process --project-id 9888
```

## Configure AWS CLI / boto3

Add a sama profile in `~/.aws/config`
```
[profile sama]
credential_process = /<absolute-path>/sama-aws.py --project-id -i 9888
```

Test it
```
aws sts get-caller-identity --profile sama
```
