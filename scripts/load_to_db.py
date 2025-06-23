import pandas as pd
import psycopg2

# Load and clean CSV
df = pd.read_csv("data/kenya_external_debt.csv")
df.columns = df.columns.str.strip()
df['debt_value'] = df['debt_value'].str.replace(",", "").str.strip().astype(float)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="debt_kenya",
    user="postgres",     # ← replace with yours
    password="root"  # ← replace with yours
)

cur = conn.cursor()

# ✅ Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS external_debt (
        country TEXT,
        year INT,
        debt_value NUMERIC
    );
""")

# ✅ Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO external_debt (country, year, debt_value)
        VALUES (%s, %s, %s)
    """, (row['country'], int(row['year']), float(row['debt_value'])))

conn.commit()
cur.close()
conn.close()

print("✅ Data successfully loaded into PostgreSQL.")
