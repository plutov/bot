# Copyright (c) 2017 Alex Pliutau

import os
import sys
from bot.bot import Bot

b = Bot(os.environ.get('SLACK_TOKEN'))
try:
	b.start()
except KeyboardInterrupt:
	sys.exit(0)