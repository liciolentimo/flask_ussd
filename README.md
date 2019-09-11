# Flask USSD Application 
Simple ussd application built with Flask, Africa's Talking, Heroku and Docker

## Prerequisites
- Python 3
- Docker CLI
- Heroku CLI
- Africa's Talking Sandbox Account

## Installation instructions
- `pip install -r requirements.txt`
- `docker build -t flaskafricastalking .`
- `heroku create`
- `heroku container:push web --app <YOUR_APP_NAME>`
- `heroku container:release web --app <YOUR_APP_NAME>`

## Set up USSD on Africa's Talking
- Create a USSD Channel
- On your callback, get the URL from your Heroku app and add it as your callback URL.
- Launch the simulator

## Resources
Refer to this blog [post](https://anthonylimo.hashnode.dev/build-and-deploy-a-ussd-application-with-africas-talking-docker-and-heroku-python-part-1-ck09qewl9000sc2s1n12d2zqa) for further references.