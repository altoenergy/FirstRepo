

"""
finance.py 
"""
import requests



class Quote(object):

	def __init__(self, symbol):
		stats = "l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7"
		url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=%s" % (symbol, stats)
		try:
			response = requests.get(url)
		except Exception, e:
			raise e
		if response.status_code is not 200:
			raise Exception("Web response not OK")

		values = response.text.split(',')
		self.values = {}

		self.values['price'] = values[0]
		self.values['change'] = values[1]
		self.values['volume'] = values[2]
		self.values['avg_daily_volume'] = values[3]
		self.values['stock_exchange'] = values[4]
		self.values['market_cap'] = values[5]
		self.values['book_value'] = values[6]
		self.values['ebitda'] = values[7]
		self.values['dividend_per_share'] = values[8]
		self.values['dividend_yield'] = values[9]
		self.values['earnings_per_share'] = values[10]
		self.values['year_high'] = values[11]
		self.values['year_low'] = values[12]
		self.values['50day_moving_avg'] = values[13]
		self.values['200day_moving_avg'] = values[14]
		self.values['price_earnings_ratio'] = values[15]
		self.values['price_earnings_growth_ratio'] = values[16]
		self.values['price_sales_ratio'] = values[17]
		self.values['price_book_ratio'] = values[18]
		self.values['short_ratio'] = values[19]

	def __getitem__(self, key):
		try:
			return self.values[key]
		except KeyError, k:
			raise k

	def __repr__(self):
		return '<Quote ' + self.values.__repr__() + '>'

_sectors = { 'Basic Materials': 1, "Conglomerates": 2, "Consumer Goods": 3,
	'Financial': 4, 'Healthcare': 5, 'Industrial Goods': 6,
	'Services': 7, 'Technology': 8, 'Utilities': 9 }

class Sector(object):
	def __init__(self):
		stat_sorted_by = "coname"
		sort_direction = "u"
		url = "http://biz.yahoo.com/p/csv/s_%s%s.csv" % (stat_sorted_by, sort_direction)
		try:
			response = requests.get(url)
		except Exception, e:
			raise e
		if response.status_code is not 200:
			raise Exception("Web response not OK")

		self.string = response.text

	def __repr__(self):
		return '<Sector ' + self.string + '>'

class Industry(object):
	def __init__(self, sector):
		sector_num = _sectors[sector]
		stat_sorted_by = "coname"
		sort_direction = "u"
		url = "http://biz.yahoo.com/p/csv/%s%s%s.csv" % (sector_num, stat_sorted_by, sort_direction)
		try:
			response = requests.get(url)
		except Exception, e:
			raise e
		if response.status_code is not 200:
			raise Exception("Web response not OK")

		self.string = response.text

	def __repr__(self):
		return '<Industry ' + self.string + '>'





