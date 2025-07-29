 🌦️ Weather Data Manager

This module represents a simple, file-based weather logging system built using Python. It allows users to input, save, and review localized climate entries — such as temperature, date, and weather conditions — through a text-based interface. Weather records are structured as objects and stored persistently in a `.pkl` file using binary serialization for reuse and further analysis.

## 📌 Key Features
- Log custom weather entries containing date, location, temperature, and atmospheric condition  
- Persist data locally using the `pickle` module for quick reloading  
- View all saved entries with structured formatting by record index  
- Interactive CLI design using basic input prompts  
- Clear module separation: data model, storage layer, logic, and main runner

## 🛠️ Technologies Used
- Python 3  
- `pickle` for binary serialization  
- `os.path` for verifying file existence  
- Command-line interface (CLI)  
- Structured modular design with functional separation

## ▶️ How to Run
1. Make sure Python 3 is installed  
2. Ensure all files are placed in the same working directory:  
   - `weather_hub.py`  
   - `record_class.py`  
   - `record_storage.py`  
   - `record_actions.py`  
3. Run the application by executing:

   `python weather_hub.py`

4. Follow the CLI prompts to enter and view saved weather logs

## 💡 Skills Showcased
- Modular code architecture based on responsibility separation  
- Data persistence using local serialization  
- Basic validation and user-driven flow control  
- Text-based application interaction for rapid testing  
- File integrity and session continuity using `os.path`

## 📁 Project Structure
weather_data_manager/  
├── weather_hub.py 
├── record_class.py 
├── record_storage.py  
├── record_actions.py
└── .gitignore

## 👤 Author
**Name**: Marian-Daniel Bodea  
**Email**: bodea7744@gmail.com  
**GitHub**: [github.com/Bodea7744](https://github.com/Bodea7744)  
**LinkedIn**: [linkedin.com/in/marian-daniel-bodea](https://linkedin.com/in/marian-daniel-bodea)

## ⚖️ License
This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/). Provided solely for educational and portfolio purposes. Commercial usage or modifications are prohibited without author consent.