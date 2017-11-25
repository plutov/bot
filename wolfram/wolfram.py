# Copyright (c) 2017 Alex Pliutau

import wolframalpha
import logging

class Wolfram(object):
	NOT_FOUND_MSG = "Sorry, I don't know this yet"

	def __init__(self, app_id):
		self.client = wolframalpha.Client(app_id)

		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
		logging.info("connected to wolfram")

	def get_short_answer(self, query):
		logging.info("searching in wolfram: {}".format(query))

		try:
			res = self.client.query(query)
			logging.info(res)

			return next(res.results).text
		except:
			return self.NOT_FOUND_MSG
