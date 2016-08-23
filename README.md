# USTDA Trade Events Lambda

This project provides an AWS Lambda that creates a single JSON document from the RSS feed 
at [https://www.ustda.gov/events/feed](https://www.ustda.gov/events/feed) and the XML feed at
[https://www.ustda.gov/api/events/xml](https://www.ustda.gov/api/events/xml).
It uploads that JSON file to a S3 bucket.

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python
* Pip
* Virtualenv
* Virtualenvwrapper
* AWS credentials

## Getting Started

	git clone git@github.com:GovWizely/lambda-ustda-trade-events.git
	cd lambda-ustda-trade-events
	mkvirtualenv -r requirements.txt lambda-ustda-trade-events

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of ~/.aws/credentials.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control

## Invocation

	lambda invoke -v
 
## Deploy

	lambda deploy
