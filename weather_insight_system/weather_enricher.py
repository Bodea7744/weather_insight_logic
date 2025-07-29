import csv
import xml.etree.ElementTree as ET
from weather_api_client import get_weather_data

# Function that reads locations from CSV and generates enriched weather XML
def enrich_weather(locations_file, output_xml):
    root = ET.Element("locations")

    # Open the CSV file and read each location
    with open(locations_file, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            location = row["location"]
            data = get_weather_data(location)

            # Create XML element for each location
            loc_elem = ET.SubElement(root, "location", name=location)
            if data:
                ET.SubElement(loc_elem, "temperature").text = str(data["main"]["temp"])
                ET.SubElement(loc_elem, "humidity").text = str(data["main"]["humidity"])
                ET.SubElement(loc_elem, "condition").text = data["weather"][0]["description"]
            else:
                ET.SubElement(loc_elem, "temperature").text = "NaN"
                ET.SubElement(loc_elem, "humidity").text = "None"
                ET.SubElement(loc_elem, "condition").text = "None"

    # Save XML to file
    tree = ET.ElementTree(root)
    tree.write(output_xml, encoding="utf-8", xml_declaration=True)