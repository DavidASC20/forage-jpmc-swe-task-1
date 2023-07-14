################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    #account for case where ask or bid is 0/not available, assuming that both arent zero
    if bid_price == 0:
        price = ask_price
    elif ask_price == 0:
        price = bid_price
    else:
        price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """

    #if the amount of asks are 0, a ratio cannot be calculated
    #return price a, if there are only bid price, theres no ratio
    if(price_b == 0):
        return price_a
    #otherwise, return the ratio of the bid price and ask price
    return price_a/price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    # For each query, 2 quotes
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        #create a dictionary to store the ticker of stock as the key and the price of the stock (average ofbid price + ask price) as value
        prices = {}
        #for each quote
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            #get the data from the tuple, store the stock and its price into the dictionary
            prices[stock] = price
            #print the data from the tuple
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        #this works because each quote has name ABC and DEF, updating the information in the dictionary
        print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
