import pickle
import os

# Numele fișierului în care stocăm înregistrările
FILENAME = 'weather_records.pkl'

# Încărcăm toate înregistrările meteo din fișier
def load_records():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'rb') as f:
            return pickle.load(f)
    # Dacă fișierul nu există, returnăm o listă goală
    return []

# Salvăm lista actualizată de înregistrări meteo în fișier
def save_records(records):
    with open(FILENAME, 'wb') as f:
        pickle.dump(records, f)