# Copyright (c) 2017 Alex Pliutau

import wolframalpha
import wikipedia
import logging

class DataProvider(object):
	NOT_FOUND_MSG = "Sorry, I don't know this yet"

	def __init__(self, app_id):
		logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

		self.wolfram_client = wolframalpha.Client(app_id)
		logging.info("connected to wolfram")

	def get_short_answer(self, query):
		logging.info("searching in wolfram: {}".format(query))

		try:
			wolfram_res = self.wolfram_client.query(query)
			logging.info("wolfram res: {}".format(wolfram_res))

			return next(wolfram_res.results).text
		except:
			# use wikipedia as failover
			wikiepedia_res = wikipedia.summary(query, sentences=1)
			logging.info("wikipedia res: {}".format(wikiepedia_res))
			if wikiepedia_res:
				return wikiepedia_res

			return self.NOT_FOUND_MSG
