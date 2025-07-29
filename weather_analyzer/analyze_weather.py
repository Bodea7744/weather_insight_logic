from weather_engine import (
    extract_weather_data,
    filter_weather_by_location,
    calculate_temperature_variation,
    export_top_10_days
)

# Extract data from the CSV file
df = extract_weather_data()

# List of target locations
locations = ['Iași', 'Bucharest', 'Cluj', 'Timișoara']

# Process weather records for each location
for location in locations:
    filtered = filter_weather_by_location(df, location)
    with_variation = calculate_temperature_variation(filtered)
    export_top_10_days(with_variation, location)
    print(f"File for {location} has been generated.")