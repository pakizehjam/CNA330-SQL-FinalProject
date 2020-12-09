import numpy as np
import pandas as pd
from sqlalchemy import create_engine


hostname = "18.217.178.166"
uname = "pythoneverything"
pwd = "python123"
dbname = "googleplaystore"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))


df = pd.read_sql('googleplaystore',engine)
connection = engine.connect()



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


connection.close()





