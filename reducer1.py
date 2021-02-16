#!/usr/bin/python3.6
import sys

'''
finds the customer(s) with the highest amount spent (in 1 month)
from a dict of customers and their payments
'''
def getMax(customerPayments):
  maxCust = []
  maxPay = 0
  for customer in customerPayments:
    payment = customerPayments[customer]
    if (payment > maxPay):
      maxCust = [customer]
      maxPay = payment
    elif (payment == maxPay):
      maxCust.append(customer)
  return(maxCust)

'''
Print top customers in sorted order
'''
def printMax(monthCountry, maxCust):
  maxCust.sort()
  print(monthCountry + ':' + ','.join(maxCust))


'''
Find the highest paying customer for each month in each country
from key/val pairs of a month and country mapped to a customer and single payment
'''
#won't know the max for this key (month/country) until we've seen all with this key
customerPayments = dict()
currentMonthCountry = None
for line in sys.stdin:
  line = line.strip()
  line = line.split('\t') 
  monthCountry = line[0] 
  # seen all payments for this month/country
  if (monthCountry != currentMonthCountry):
    if (currentMonthCountry):
      maxCust = getMax(customerPayments)
      printMax(currentMonthCountry, maxCust)
    currentMonthCountry = monthCountry
    customerPayments = dict()
  customerId, amount = line[1].split(',')
  amount = float(amount)
  #sum up all payments seen for each customer for each month/country
  if (customerId in customerPayments):
    customerPayments[customerId] = customerPayments[customerId] + amount
  else:
    customerPayments[customerId] = amount
#grab the last one
if (monthCountry == currentMonthCountry):
  maxCust = getMax(customerPayments)
  printMax(currentMonthCountry, maxCust)