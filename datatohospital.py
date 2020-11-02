import pandas as pd
import sqlite3

conn = sqlite3.connect("/Users/George/Desktop/hospital.db")
df = pd.read_csv("processed.cleveland.data.csv")

df.to_sql('records', con=conn)
