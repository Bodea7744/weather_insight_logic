# Clasa care definește o înregistrare meteo individuală
class WeatherRecord:
    def __init__(self, date, location, temperature, condition):
        # Inițializăm atributele unui record meteo
        self.date = date
        self.location = location
        self.temperature = temperature
        self.condition = condition

    # Metodă care returnează o reprezentare frumoasă a datelor
    def __str__(self):
        return (f'Dată: {self.date}\n'
                f'Locație: {self.location}\n'
                f'Temperatură: {self.temperature}°C\n'
                f'Condiții: {self.condition}\n')