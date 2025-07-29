import pandas as pd
import xml.etree.ElementTree as ET
from weather_enricher import enrich_weather

# Paths to the input CSV and output XML
XML_FILE = "weather_enriched.xml"
CSV_LOCATIONS = "locations.csv"

# Call the weather enrichment function
enrich_weather(CSV_LOCATIONS, XML_FILE)

# Parse the enriched XML file
tree = ET.parse(XML_FILE)
root = tree.getroot()

# Extract weather data into a list of records
records = []
for loc in root.findall("location"):
    name = loc.get("name")
    temp = loc.find("temperature").text
    humidity = loc.find("humidity").text
    condition = loc.find("condition").text
    records.append({
        "location": name,
        "temperature": float(temp) if temp != "NaN" else None,
        "humidity": int(humidity) if humidity != "None" else None,
        "condition": condition
    })

# Convert to DataFrame and show top 10 hottest locations
df = pd.DataFrame(records)
df_sorted = df.sort_values(by="temperature", ascending=False)
print("\n🌡️ Top 10 hottest locations:")
print(df_sorted.head(10))

# Confirm XML was saved
print(f"\nXML file saved to: {XML_FILE}")