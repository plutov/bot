# Copyright (c) 2017 Alex Pliutau

import random
import logging
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu.components import ComponentBuilder

class RasaNLP(object):
	COULD_NOT_PARSE_MSGS = [
		"Sorry, don't know it",
		"Next time I will know, but not now",
		"Sorry, can't get what do you mean",
		"Try something else"
	]
	GREET_MSGS = ["Hola!"]
	INTENT_GREET = "greet"
	INTENT_WHATIS = "whatis"
	ENTITY_QUERY = "query"

	def __init__(self, wolfram, config_file, data_file, model_dir):
		self.greeted = False

		self.wolfram = wolfram
		self.data_file = data_file
		self.model_dir = model_dir
		self.rasa_config = RasaNLUConfig(config_file)

		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

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
		logging.info(res)

		if not "intent" in res or res["intent"] is None:
			return random.choice(self.COULD_NOT_PARSE_MSGS)

		if res["intent"]["name"] == self.INTENT_GREET and self.greeted == False:
			self.greeted = True
			return random.choice(self.GREET_MSGS)

		if res["intent"]["name"] == self.INTENT_WHATIS and len(res["entities"]) > 0:
			for e in res["entities"]:
				if e["entity"] == self.ENTITY_QUERY:
					return self.get_short_answer(e["value"])

		return random.choice(self.COULD_NOT_PARSE_MSGS)

	def get_short_answer(self, query):
		try:
			return self.wolfram.get_short_answer(query)
		except:
			return self.wolfram.NOT_FOUND_MSG