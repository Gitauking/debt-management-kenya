import requests
import pandas as pd

url = "https://api.worldbank.org/v2/country/KE/indicator/DT.DOD.DECT.CD?date=2010:2024&format=json&per_page=100"

try:
    response = requests.get(url, timeout=10)  # 10-second timeout
    response.raise_for_status()

    data = response.json()[1]  # actual data is in second element
    extracted = []

    for entry in data:
        extracted.append({
            "country": entry["country"]["value"],
            "year": int(entry["date"]),
            "debt_value": entry["value"]
        })

    df = pd.DataFrame(extracted).sort_values(by="year")
    df.to_csv("data/kenya_external_debt.csv", index=False)
    print(df)

except requests.exceptions.RequestException as e:
    print("❌ API request failed:", e)

