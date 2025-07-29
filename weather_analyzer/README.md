🌦️ Weather Analyzer

This module analyzes weather records from a CSV source and identifies the top 10 most extreme temperature variation days for each location. It is built using Python and leverages structured data processing with Pandas. The analysis results are exported as Excel files for easy viewing.

## 📌 Key Features
- Read structured weather data from `weather.csv`
- Filter entries by city name and compute daily temperature variation
- Automatically export top 10 most extreme temperature days per city into Excel files
- Reusable, modular functions: extraction, filtering, calculation, and export
- Clear separation of analysis logic (`weather_engine.py`) and runner script (`analyze_weather.py`)

## 🛠️ Technologies Used
- Python 3
- `pandas` for data manipulation
- `openpyxl` for Excel file generation
- CSV file input/output for data handling
- Modular functional architecture for clarity and reusability

## ▶️ How to Run
1. Make sure Python 3 is installed
2. Ensure all files are placed in the same working directory:
   - `analyze_weather.py`
   - `weather_engine.py`
   - `weather.csv`
3. Run the application by executing:

   `python analyze_weather.py`

4. Resulting files will be generated per city (e.g. `Iași_top_10_days.xlsx`)

## 💡 Skills Showcased
- Clean separation of data logic and orchestration
- Applied data transformation techniques using Pandas
- Excel export automation and top-N record sorting
- Scalable filtering based on geographic criteria
- Easily extendable structure for more metrics (e.g. humidity scoring)

## 📁 Project Structure
weather_analyzer/
├── analyze_weather.py
├── weather_engine.py
├── weather.csv
├── Iași_top_10_days.xlsx
├── Cluj_top_10_days.xlsx
├── Bucharest_top_10_days.xlsx
├── Timișoara_top_10_days.xlsx
└── .gitignore

## 👤 Author
**Name**: Marian-Daniel Bodea  
**Email**: bodea7744@gmail.com  
**GitHub**: [github.com/Bodea7744](https://github.com/Bodea7744)  
**LinkedIn**: [linkedin.com/in/marian-daniel-bodea](https://linkedin.com/in/marian-daniel-bodea)

## ⚖️ License
This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/). Provided solely for educational and portfolio purposes. Commercial usage or modifications are prohibited without author consent.