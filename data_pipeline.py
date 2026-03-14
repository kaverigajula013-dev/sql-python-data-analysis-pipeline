import pandas as pd
import sqlite3

# connect to database
conn = sqlite3.connect("sales_database.db")

# query data
query = "SELECT * FROM sales"

data = pd.read_sql_query(query, conn)

print("Dataset preview:")
print(data.head())

# basic analysis
total_sales = data["sales_amount"].sum()
average_sales = data["sales_amount"].mean()

print("\nTotal Sales:", total_sales)
print("Average Sales:", average_sales)

# save report
summary = pd.DataFrame({
    "Metric": ["Total Sales", "Average Sales"],
    "Value": [total_sales, average_sales]
})

summary.to_csv("sales_summary_report.csv", index=False)

print("\nReport generated successfully.")
