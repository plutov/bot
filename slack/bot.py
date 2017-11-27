# Copyright (c) 2017 Alex Pliutau

from slackclient import SlackClient
import logging
import time
import sys

class SlackBot(object):
	def __init__(self, token, rasa_nlu):
		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

		self.sc = SlackClient(token)
		self.rasa_nlu = rasa_nlu

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
		# do not handle bot messages
		if "type" in data and not "bot_id" in data and data["type"] == "message":
			self.process_msg(data)

	def process_msg(self, data):
		logging.info("received message from {}: {}".format(data["user"], data["text"]))
		text_to_reply = self.rasa_nlu.find_reply(data["text"])
		if text_to_reply:
			self.send_im_msg(data["user"], text_to_reply)
			

	def send_im_msg(self, user, msg):
		self.sc.api_call(
			"chat.postMessage",
			channel=user,
			as_user="true",
			text=msg
		)
		logging.info("sent message to {}: {}".format(user, msg))