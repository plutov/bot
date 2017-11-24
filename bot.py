# Copyright (c) 2017 Alex Pliutau

import os
import sys
from slack.bot import SlackBot
from nlp.rasa import RasaNLP

r = RasaNLP("rasa-config.json", "rasa-data.json", "./rasa-model")
b = SlackBot(os.environ.get("SLACK_TOKEN"))

try:
	r.train()
	b.start()
except KeyboardInterrupt:
	sys.exit(0)