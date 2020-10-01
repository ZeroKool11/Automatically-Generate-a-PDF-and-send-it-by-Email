#!/usr/bin/env python3

import json
import locale
import sys
import subprocess
import os
import reports

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])

def years_sales(dic,key,value):
  """Creates a new element in the dictionary with his value or adding the value if the elemente already exists"""
  if not key in dic:
    dic[key] = value
  else:
    dic[key] = dic[key] + value
  return dic

def max_sales_year(dic):
  """Finds the year with the most sales"""
  year = max(dic, key=dic.get)
  sales = dic[year]
  result = {"year": year, "sales": sales}
  return result

def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"car_model": " ", "sales": 0}
  year_car_dic = {}
  max_sales_year_dic = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["sales"]:
      max_sales["car_model"] = item["car"]["car_model"]
      max_sales["sales"] = item["total_sales"]
    # TODO: also handle most popular car_year
    dic = years_sales(year_car_dic,item["car"]["car_year"],item["total_sales"])
  
  max_sales_year_dic = max_sales_year(dic)
  summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(max_sales["car_model"],max_sales["sales"]),
    "The most popular year was {} with {} sales.".format(max_sales_year_dic["year"],max_sales_year_dic["sales"])
  ]
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def change_environ_variable(variable, value):
  """Setting the correct environ variable"""
  try:
    os.environ[variable] = value
    return True
  except Exception as e:
    print("No se logro cambiar la variable de entorno " + variable + ". " + str(e))
    return False

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  carPath = os.path.realpath('../car_sales.json')

  #Changint the environ variable LC_ALL
  if not change_environ_variable('LC_ALL','en_US.UTF-8'): exit()
  #If the previous line does not work this will work  
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  
  data = load_data(carPath)
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report
  reportos.generated("/tmp/cars.pdf",)
  # TODO: send the PDF report as an email attachment


if __name__ == "__main__":
  main(sys.argv)
