# Copyright (c) 2017 Alex Pliutau

import os
import sys
from slack.bot import SlackBot
from nlp.rasa import RasaNLP
from wolfram.wolfram import Wolfram

try:
	w = Wolfram(os.environ.get("WOLFRAM_APP_ID"))

	r = RasaNLP(w, "rasa-config.json", "rasa-data.json", "./rasa-model")
	r.train()

	b = SlackBot(os.environ.get("SLACK_TOKEN"), r)
	b.start()
except KeyboardInterrupt:
	sys.exit(0)