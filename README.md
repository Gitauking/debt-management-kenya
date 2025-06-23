# Debt Management Kenya 📊🇰🇪

This project tracks **Kenya’s external debt** from **2010 to 2024** using the World Bank API. It includes a full data pipeline: extraction, transformation, loading into PostgreSQL, and visualization using Grafana.

---

## 🚀 Tech Stack

- **Python** – For data extraction and transformation
- **wbgapi / requests** – To access World Bank API data
- **pandas** – Data wrangling
- **PostgreSQL** – Relational database storage
- **Grafana** – Interactive dashboards and visualizations

---

## 📦 Features

- Extracts debt data for Kenya (Indicator: `DT.DOD.DECT.CD`)
- Cleans and transforms it (handles commas, formats types)
- Loads into PostgreSQL database
- Visualized in Grafana as:
  - 📈 Line chart: Total external debt over time
  - 📊 Bar chart: Year-over-year debt change

---

## 🖼️ Dashboard Screenshots

| Line Chart                            | Year-over-Year Change                     |
|--------------------------------------|-------------------------------------------|
| ![line](screenshots/line_chart.png)  | ![bar](screenshots/yoy_change_chart.png)  |

---

## 📁 Project Setup

```bash
git clone https://github.com/your-username/debt-management-kenya.git
cd debt-management-kenya
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
