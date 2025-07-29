import pandas as pd

# Extract data from the CSV file
def extract_weather_data():
    df = pd.read_csv("weather.csv")
    return df

# Filter weather data by location
def filter_weather_by_location(df, location_name):
    mask = df['location'] == location_name
    return df.loc[mask].copy()

# Calculate temperature variation (max - min)
def calculate_temperature_variation(df):
    df['max_temp'] = pd.to_numeric(df['max_temp'], errors='coerce')
    df['min_temp'] = pd.to_numeric(df['min_temp'], errors='coerce')
    df['variation'] = df['max_temp'] - df['min_temp']
    df.dropna(subset=['variation'], inplace=True)
    df.drop(columns=['humidity', 'condition', 'max_temp', 'min_temp'], inplace=True)
    return df

# Export top 10 extreme days to Excel file
def export_top_10_days(weather_df, location_name):
    selected_columns = ['date', 'location', 'variation']
    top_10 = weather_df[selected_columns].sort_values(by='variation', ascending=False).head(10)
    top_10.to_excel(f"{location_name}_top_10_days.xlsx", index=False)