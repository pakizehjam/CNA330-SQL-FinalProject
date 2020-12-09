import numpy as np
# import mysql.connector
# import json
# import csv, _sqlite3
# from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt

import pandas as pd


df = pd.read_csv(r'C:\Users\Luma\PycharmProjects\GroupProject\googleplaystore.csv')


# LUMA's PART
# 1. Count of Categorical
# To find the count of free Apps Vs. the Apps that need to pay for it.
print("'Value_Counts'")
print("'To Find The Count of Free Apps VS Paid Apps'")
print(df.Type.value_counts())


# Hasan
# 2. To find the count of Apps based on the price
print("'To Find The Count of Apps Based On Their Price'")
print(df.Price.value_counts())


# Mohammed
# 3. To sort the data by the size or by rating

print("'Sort The Apps By Rating'")
print(df.sort_values(by="Rating"))  # sort it by rating
print("'Sort The Apps By Size'")
print(df.sort_values(by="Size"))    # sort it by size






