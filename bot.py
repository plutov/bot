# Copyright (c) 2017 Alex Pliutau

import os
import sys
import traceback
from slack.bot import SlackBot
from nlp.rasa import RasaNLP
from dataprovider.dataprovider import DataProvider

try:
	dp = DataProvider(os.environ.get("WOLFRAM_APP_ID"))

	r = RasaNLP(dp, "rasa-config.json", "rasa-data.json", "./rasa-model")
	r.train()

	b = SlackBot(os.environ.get("SLACK_TOKEN"), r)
	b.start()
except KeyboardInterrupt:
	r.snapshot_unparsed_messages("rasa-unparsed.txt")
	sys.exit(0)
except:
	r.snapshot_unparsed_messages("rasa-unparsed.txt")
	traceback.print_exc()