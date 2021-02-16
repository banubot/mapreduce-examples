#!/usr/bin/python3.6
import sys 
line = sys.stdin.readline()

'''
Map customer payment info from list of orders
to find highest paying customer for each month
in each country
Output:
month,country\tcustomer,amount paid 
'''
while line:
  orderInfo = line.split(',')
  invoiceNo = orderInfo[0]
  #skip the header
  if (invoiceNo != "InvoiceNo"):
    customerId = orderInfo[6]
    #invoices with C are returns (ignore)
    #ignore orders missing customer id
    if not (invoiceNo.startswith('C') or len(customerId) == 0):
      quantity = int(orderInfo[3])
      date = orderInfo[4]
      unitPrice = float(orderInfo[5])
      country = orderInfo[7].strip()
      date = date.split('/')
      month = date[0]
      amount = quantity * unitPrice
      key = month + ',' + country
      value = customerId + ',' + str(amount)
      print(key + '\t'  + value)
  line = sys.stdin.readline()