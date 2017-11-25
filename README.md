### Overview

Bot using RASA NLU to answer different questions. Using Wolfram Alpha to get answers.

### Run it with Docker

Get Slack API Token first: https://wizeline.slack.com/services/B861V31E3

Get Wolfram App ID: https://developer.wolframalpha.com/portal/myapps/

```
docker build -t bot . && docker run -e SLACK_TOKEN=<token> -e WOLFRAM_APP_ID=<app_id> bot
```

### Run with Python 3

```
SLACK_TOKEN=<token> WOLFRAM_APP_ID=<app_id> python3 bot.py
```

### RASA

Create initial intentions - https://rasahq.github.io/rasa-nlu-trainer/