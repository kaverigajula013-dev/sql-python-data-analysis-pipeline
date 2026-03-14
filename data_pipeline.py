import pandas as pd

# load dataset
data = pd.read_csv("sales_data.csv")

print("Dataset preview:")
print(data.head())

# total sales
total_sales = data["SALES"].sum()

# average sales
average_sales = data["SALES"].mean()

print("\nTotal Sales:", total_sales)
print("Average Sales:", average_sales)

# sales by country
sales_country = data.groupby("COUNTRY")["SALES"].sum()

print("\nSales by Country:")
print(sales_country)

# save summary report
summary = pd.DataFrame({
    "Metric": ["Total Sales", "Average Sales"],
    "Value": [total_sales, average_sales]
})

summary.to_csv("sales_summary_report.csv", index=False)

print("\nReport generated successfully.")
