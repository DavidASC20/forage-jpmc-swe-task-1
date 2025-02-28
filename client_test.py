import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # for each quote, assert that the tuple returned from the function is what it is supposed to be
    for quote in quotes:
      ticker = quote['stock']
      bid_price = quote['top_bid']['price'] 
      ask_price = quote['top_ask']['price']
      self.assertEqual(getDataPoint(quote), (ticker, bid_price, ask_price, (bid_price + ask_price) / 2 ))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # for each quote, assert that the tuple returned from the function is what it is supposed to be
    for quote in quotes:
      ticker = quote['stock']
      bid_price = quote['top_bid']['price'] 
      ask_price = quote['top_ask']['price']
      self.assertEqual(getDataPoint(quote), (ticker, bid_price, ask_price, (bid_price + ask_price) / 2 ))

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceAskisZero(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      ticker = quote['stock']
      bid_price = quote['top_bid']['price'] 
      self.assertEqual(getDataPoint(quote), (ticker, bid_price, 0, bid_price))

  
  def test_getDataPoint_calculatePriceBidisZero(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      ticker = quote['stock']
      ask_price = quote['top_ask']['price'] 
      self.assertEqual(getDataPoint(quote), (ticker, 0, ask_price, ask_price))




if __name__ == '__main__':
    unittest.main()
