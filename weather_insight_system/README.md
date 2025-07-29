# 🌍 Weather Insight System

This project is a modular Python-based weather data pipeline designed to fetch, enrich, and analyze climate information from OpenWeatherMap. It reads location entries from a CSV file, retrieves live weather metrics via API, serializes the results into XML, and extracts actionable insights through Pandas-based filtering.

## 📌 Key Features
- Automatically enrich location data with live temperature, humidity, and conditions
- Sort and identify hottest regions using structured analysis in Pandas
- Persist enriched weather records as XML for downstream use
- Graceful handling of API failures with placeholder values
- Modular design: API client, data enrichment, and analytics separated cleanly

## 🛠️ Technologies Used
- Python 3  
- `pandas` for data handling  
- `xml.etree.ElementTree` for XML serialization  
- `requests` for RESTful API access  
- OpenWeatherMap API for live data retrieval

## ▶️ How to Run
1. Make sure Python 3 is installed  

2. Ensure the following files are placed in the same directory:
   - `analyse_weather_api.py`  
   - `weather_enricher.py`  
   - `weather_api_client.py`  
   - `locations.csv`  

3. Create a `.env` file in the project root containing your OpenWeatherMap API key:


4. Run the analysis script:
   - `python analyse_weather_api.py`

5. View the top 10 hottest locations printed to the console


## 💡 Skills Showcased
- REST API integration and JSON parsing  
- XML document generation and handling  
- Data cleansing, sorting and filtering with Pandas  
- Modular architecture for separation of concerns  
- Resilience strategies for API unavailability

## 📁 Project Structure
weather_insight_system/  
├── analyse_weather_api.py  
├── weather_enricher.py  
├── weather_api_client.py  
├── locations.csv  
└── weather_enriched.xml  

## 👤 Author
**Name**: Marian-Daniel Bodea  
**Email**: bodea7744@gmail.com  
**GitHub**: [github.com/Bodea7744](https://github.com/Bodea7744)  
**LinkedIn**: [linkedin.com/in/marian-daniel-bodea](https://linkedin.com/in/marian-daniel-bodea)  

## ⚖️ License
This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/). Provided solely for educational and portfolio purposes. Commercial usage or modifications are prohibited without author consent.