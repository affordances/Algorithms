#!/usr/bin/python

import argparse

def find_max_profit(prices):
  highest = None
  for i, first_num in enumerate(prices):
      for second_num in prices[i + 1:]:
          current_profit = second_num - first_num
          if highest == None or current_profit > highest:
              highest = current_profit
  return highest


if __name__ == '__main__':
  # You can test your implementation by running
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
