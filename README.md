### Overview

Bot using RASA NLU to answer different questions.

### Run it with Docker

Get Slack API Toen first: https://wizeline.slack.com/services/B861V31E3

```
docker build -t bot . && docker run -e SLACK_TOKEN=<token> bot
```

### Run with Python 3

```
SLACK_TOKEN=<token> python3 bot.py
```

### RASA

Create initial intentions - https://rasahq.github.io/rasa-nlu-trainer/