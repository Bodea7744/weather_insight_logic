from record_class import WeatherRecord
from record_storage import load_records, save_records

# Funcție care adaugă o înregistrare nouă
def add_record():
    print("\n🔹 Introducere înregistrare meteo:")
    date = input("Introduceți data (ex: 2025-07-28): ")
    location = input("Introduceți locația: ")
    temperature = input("Introduceți temperatura (°C): ")
    condition = input("Introduceți condițiile meteo (ex: senin, ploaie): ")

    # Construim un obiect WeatherRecord cu informațiile introduse
    record = WeatherRecord(date, location, temperature, condition)

    # Încărcăm lista existentă, adăugăm recordul nou și salvăm
    records = load_records()
    records.append(record)
    save_records(records)

    print("\n✅ Înregistrare meteo adăugată cu succes!\n")

# Funcție care afișează toate înregistrările existente
def view_records():
    records = load_records()
    if not records:
        print("\n⚠️ Nu există înregistrări meteo salvate.\n")
    else:
        print("\n📋 Înregistrări meteo:\n")
        for i, record in enumerate(records, start=1):
            print(f"Record #{i}")
            print(record)
            print('-' * 30)