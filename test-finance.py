

"""
Test harness for the finance.py module

"""

import finance


def initial():
	test_condition = True
	if(not test_condition): raise Exception('Initial Error')

def create_quote():
	google = finance.Quote("goog")
	fb = finance.Quote("FB")
	#print google
	#print fb

def twenty_values():
	google = finance.Quote("goog")

	price = google["price"]
	change = google["change"]
	volume = google["volume"]
	avg_daily_volume = google["avg_daily_volume"]
	stock_exchange = google["stock_exchange"]
	market_cap = google["market_cap"]
	book_value = google["book_value"]
	ebitda = google["ebitda"]
	dividend_per_share = google["dividend_per_share"]
	dividend_yield = google["dividend_yield"]
	earnings_per_share = google["earnings_per_share"]
	year_high = google["year_high"]
	year_low = google["year_low"]
	fifty_day_moving_avg = google["50day_moving_avg"]
	twohundred_day_moving_avg = google["200day_moving_avg"]
	price_earnings_ratio = google["price_earnings_ratio"]
	price_earnings_growth_ratio = google["price_earnings_ratio"]
	price_sales_ratio = google["price_sales_ratio"]
	price_book_ratio = google["price_book_ratio"]
	short_ratio = google["short_ratio"]

def create_sector():
	sectors = finance.Sector()
	print sectors

def create_industry():
	tech_industry = finance.Industry("Technology")
	print tech_industry



def main():
	initial()
	create_quote()
	twenty_values()
	create_sector()

	create_industry()

	print "All systems are GO"

if __name__ == '__main__':
	main()