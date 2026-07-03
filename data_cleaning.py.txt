import pandas as pd

# Read both datasets
df1 = pd.read_csv("data/index_1.csv")
df2 = pd.read_csv("data/index_2.csv")

# Combine them
df = pd.concat([df1, df2], ignore_index=True)

print("Shape:", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicates:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("data/coffee_sales_cleaned.csv", index=False)

print("\nCleaning Completed Successfully!")