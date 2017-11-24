# Copyright (c) 2017 Alex Pliutau

from slackclient import SlackClient
import logging
import time
import sys

class Bot(object):
	def __init__(self, token):
		self.sc = SlackClient(token)

		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

	def connect(self):
		if self.sc.rtm_connect():
			logging.info("connected to slack rtm")
		else:
			logging.error("could not connect to slack rtm")
			sys.exit(1)

	def start(self):
		self.connect()
		while True:
			for reply in self.sc.rtm_read():
				self.input(reply)

			time.sleep(.1)

	def input(self, data):
		if "type" in data and data["type"] == "message":
			self.process_msg(data)

	def process_msg(self, data):
		logging.info("received message from {}: {}".format(data["user"], data["text"]))