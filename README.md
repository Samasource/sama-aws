# How to upload your assets to Sama

## Gather your Sama info

If you already know your Sama API key and project ID, you can skip this section.

### API Key

How to get your API key?

1.   Go to the [clients](https://app.sama.com/clients) tab
2.   Look for your client
3.   Click on show API key

### Project ID

How to get your project ID?

1.   Go to the [projects](https://app.sama.com/projects) page
2.   Use the filters and search for the client you are working with (i.e.,**BDD**)
3.   Click on view
4.   Choose the **BDD** project
5.   Take the ID from the URL (i.e., app.sama.com/projects/*12345*)

## Sama CLI

You can use the Sama CLI to upload assets and directly create tasks if it fit your needs.
[Sama CLI documentation](https://docs.sama.com/reference/cli-overview)

## AWS CLI

Using the AWS CLI will give you the best performance to upload a lot of assets.

### Install Python 3

#### Windows

Python3 is available on the [Microsoft store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5?hl=en-us&gl=us)

#### MacOs

Python3 is available on macOS via [Homebrew](https://brew.sh/):

```sh
brew install python3
```

On macOS, make sure to run `Install Certificates.command` after the installation.

### Install AWS CLI

[AWS CLI](https://aws.amazon.com/cli/)

### Configure sama-aws tool

Download the [sama-aws.py](https://github.com/Samasource/sama-aws/releases/latest/download/sama-aws.py)

Start a terminal. The configure command create a `sama` AWS CLI profile and AWS CLI will fetch temporary credentials from https://app.sama.com using your API key. It will auto-renew the credentials every hour.

```bash
python3 sama-aws.py configure
```

Look for `Assets S3 URL` in the command output, you will need it later.

Test AWS CLI sama profile. 

```bash
aws --profile sama sts get-caller-identity 
aws --profile sama s3 ls <Assets S3 URL as printed by the configure command>
```

### Uploads assets

This command upload the batch-1 folder to your S3 dedicated prefix.

```bash
aws --profile sama s3 sync ./batch-1 <Assets S3 URL>/batch-1
```

## Configure Cyberduck

Install [Cyberduck](https://cyberduck.io/)

Run the following command in a shell. It will create or update the `sama-cyberduck` AWS profile.

```bash
python3 sama-aws.py update-credentials-file
```

- Add `S3 (Credentials from AWS Command Line Interface)` bookmark in Cyberduck
- Set profile name as `sama-cyberduck`
- Set path to `Assets S3 URL` as printed by the configure command but without the `s3://` prefix.

After an hour, the temporary credentials will expire in Cyberduck. You will need to run the script again and reconnect by going back to the Cyberduck landing page.
