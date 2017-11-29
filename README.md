### Overview

Bot using RASA NLU to answer different questions. Using Wolfram Alpha to get answers. Using Wikipedia as failover.

![bot.png](https://raw.githubusercontent.com/plutov/bot/master/bot.png)

[Article in my blog](http://pliutau.com/create-bot-with-nlu-in-python/) describing how it works.

### Run it with Docker

 - [Get Slack API Token](https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens)
 - [Get Wolfram App ID](https://developer.wolframalpha.com/portal/myapps/)
 - Wikipedia API doesn't require API key.

```
docker build -t bot . && docker run -e SLACK_TOKEN=<token> -e WOLFRAM_APP_ID=<app_id> bot
```

### Run with Python 3

Install dependencies from Dockerfile and run:

```
SLACK_TOKEN=<token> WOLFRAM_APP_ID=<app_id> python3 bot.py
```

### RASA

Create initial intentions - https://rasahq.github.io/rasa-nlu-trainer/. During the Bot start we run training process based on `rasa-data.json` intentions. Later we work with messages we can parse, also Bot stores all unparsed messages so we can check them later.