# sama-setup


## Quick start

Print temporary credentials
```
python3 sama-aws.py --credential-process --project-id 9888
```

## Add a sama profile in ~/.aws/config

```
[profile sama]
credential_process = python3 /<absolute-path>/sama-aws.py --project-id -i 9888
```

Test it
```
aws sts get-caller-identity --profile sama
```
