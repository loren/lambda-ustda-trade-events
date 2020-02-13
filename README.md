[![CircleCI](https://circleci.com/gh/GovWizely/lambda-ustda-trade-events/tree/master.svg?style=svg)](https://circleci.com/gh/GovWizely/lambda-ustda-trade-events/tree/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/309c971db2f097b4c032/maintainability)](https://codeclimate.com/github/GovWizely/lambda-ustda-trade-events/maintainability)

# USTDA Trade Events Lambda

This project provides an AWS Lambda that creates a single JSON document from the RSS feed 
at [https://www.ustda.gov/events/feed](https://www.ustda.gov/events/feed) and the XML feed at
[https://www.ustda.gov/api/events/xml](https://www.ustda.gov/api/events/xml).
It uploads that JSON file to a S3 bucket.

## Prerequisites

- This project is tested against Python 3.7+ in [CircleCI](https://app.circleci.com/github/GovWizely/lambda-ustda-trade-events/pipelines).

## Getting Started

	git clone git@github.com:GovWizely/lambda-ustda-trade-events.git
	cd lambda-ustda-trade-events
	mkvirtualenv -p /usr/local/bin/python3.8 -r requirements-test.txt ustda-trade-events

If you are using PyCharm, make sure you enable code compatibility inspections for Python 3.7/3.8.

### Tests

```bash
python -m pytest
```

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of `~/.aws/credentials`. To use another profile, you can do something like `export AWS_DEFAULT_PROFILE=govwizely`.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control.

## Invocation

	lambda invoke -v
 
## Deploy
    
To deploy:

	lambda deploy --requirements requirements.txt
