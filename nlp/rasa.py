# Copyright (c) 2017 Alex Pliutau

from logging
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter

class RasaNLP(object):
	def __init__(self, config_file, data_file, model_dir):
		self.data_file = data_file
		self.model_dir = model_dir
		self.rasa_config = RasaNLUConfig(config_file)

		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

	def train(self):
		training_data = load_data(self.data_file)
		trainer = Trainer(self.rasa_config)
		trainer.train(training_data)

		self.interpreter = Interpreter.load(trainer.persist(self.model_dir), self.rasa_config)
