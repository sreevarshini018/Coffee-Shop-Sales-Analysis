import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/coffee_sales_cleaned.csv")

print(df.head())

print("\nDataset Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# ----------------------------
# Total Sales
# ----------------------------

print("\nTotal Sales")
print(df["money"].sum())

# ----------------------------
# Average Sale
# ----------------------------

print("\nAverage Sale")
print(df["money"].mean())

# ----------------------------
# Top Selling Coffee
# ----------------------------

top = df.groupby("coffee_name")["money"].sum().sort_values(ascending=False)

print(top)

plt.figure(figsize=(8,5))
top.plot(kind="bar")
plt.title("Top Selling Coffee")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/top_products.png")
plt.close()

# ----------------------------
# Payment Method
# ----------------------------

payment = df["cash_type"].value_counts()

plt.figure(figsize=(6,6))
payment.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Payment Method")
plt.savefig("images/payment_methods.png")
plt.close()

# ----------------------------
# Daily Sales
# ----------------------------

df["date"] = pd.to_datetime(df["date"])

daily = df.groupby("date")["money"].sum()

plt.figure(figsize=(10,5))
daily.plot()
plt.title("Daily Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/daily_sales.png")
plt.close()

print("\nAnalysis Completed Successfully!")