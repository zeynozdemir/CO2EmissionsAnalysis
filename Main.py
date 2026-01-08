import pandas as pd
import plotly.express as px

# Load dataset
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
df = pd.read_csv(url)

# Select countries
countries = ["United States", "China", "Germany", "Turkey"]
df = df[df["country"].isin(countries)]

# Remove missing values
df = df.dropna(subset=["co2"])

# Line plot
fig = px.line(
    df,
    x="year",
    y="co2",
    color="country",
    title="CO₂ Emissions Over Time",
    labels={
        "co2": "CO₂ emissions (million tonnes)",
        "year": "Year"
    }
)

fig.show()
