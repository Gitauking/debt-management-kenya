import pandas as pd

df = pd.read_csv("data/kenya_external_debt.csv")

# Show all columns exactly as they appear
print("🔍 Actual CSV column names:")
print(df.columns.tolist())