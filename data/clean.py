import pandas as pd

# Load the raw CSV
df = pd.read_csv("kenya_external_debt.csv")

# Show initial data
print("🔍 Raw data preview:")
print(df.head())

# Drop rows with missing debt values
df = df.dropna(subset=['debt_value'])

# Ensure year is int, debt is float
df['year'] = df['year'].astype(int)
df['debt_value'] = df['debt_value'].astype(float).round(2)

# Sort by year
df = df.sort_values(by='year')

# Preview cleaned data
print("\n✅ Cleaned data:")
print(df)

# Save cleaned CSV
df.to_csv("data/kenya_external_debt_cleaned.csv", index=False)
print("\n📁 Cleaned CSV saved as: kenya_external_debt_cleaned.csv")
