# Copyright (c) 2017 Alex Pliutau

import random
import logging
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu.components import ComponentBuilder

class RasaNLP(object):
	COULD_NOT_PARSE_MSGS = [
		"Sorry, I don't know it",
		"Next time I will know, but not now",
		"Sorry, can't get what do you mean",
		"Try something else"
	]
	GREET_MSGS = ["Hola!", "Privet!", "Xin chào!"]
	INTENT_GREET = "greet"
	INTENTS_QUESTION = ["whatis", "howto", "when", "do"]
	ENTITY_QUERY = "query"

	def __init__(self, data_provider, config_file, data_file, model_dir):
		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

		# store unparsed messages, so later we can train bot
		self.unparsed_messages = []

		self.data_provider = data_provider
		self.data_file = data_file
		self.model_dir = model_dir
		self.rasa_config = RasaNLUConfig(config_file)

	def train(self):
		training_data = load_data(self.data_file)
		trainer = Trainer(self.rasa_config)
		trainer.train(training_data)

		self.interpreter = Interpreter.load(trainer.persist(self.model_dir), self.rasa_config)

		logging.info("rasa trained successfully")

	def parse(self, msg):
		return self.interpreter.parse(msg)

	def find_reply(self, msg):
		res = self.parse(msg)
		logging.info("rasa parse res: {}".format(res))

		if not "intent" in res or res["intent"] is None:
			# later we can do something with unparsed messages, probably train bot
			self.unparsed_messages.append(msg)
			return random.choice(self.COULD_NOT_PARSE_MSGS)

		if res["intent"]["name"] == self.INTENT_GREET:
			return random.choice(self.GREET_MSGS)

		# same approach for all questions
		if res["intent"]["name"] in self.INTENTS_QUESTION and len(res["entities"]) > 0:
			for e in res["entities"]:
				if e["entity"] == self.ENTITY_QUERY:
					return self.get_short_answer(e["value"])

		self.unparsed_messages.append(msg)
		return random.choice(self.COULD_NOT_PARSE_MSGS)

	def get_short_answer(self, query):
		return self.data_provider.get_short_answer(query)

	# saves unparsed messages into a file
	def snapshot_unparsed_messages(self, filename):
		with open(filename, "a") as f:
			for msg in self.unparsed_messages:
				f.write("{}\n".format(msg))