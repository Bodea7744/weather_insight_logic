# Importăm funcțiile de acțiune pentru recorduri meteo
from record_actions import add_record, view_records

# Punctul de intrare principal în aplicație
def main():
    print("🌦️ Bine ați venit în Weather Hub!")
    while True:
        print("\nCe doriți să faceți?")
        print("1. Adăugați o înregistrare meteo")
        print("2. Vizualizați înregistrările salvate")
        print("3. Ieșiți din aplicație")

        choice = input("Alegeți o opțiune (1-3): ")

        if choice == '1':
            # Adăugăm o nouă înregistrare meteo
            add_record()
        elif choice == '2':
            # Afișăm toate înregistrările meteo salvate
            view_records()
        elif choice == '3':
            # Ieșire din aplicație
            print("\n👋 La revedere! Vă dorim vreme frumoasă!\n")
            break
        else:
            print("\n⚠️ Opțiune invalidă. Încercați din nou.\n")

# Rulăm funcția main doar dacă scriptul e apelat direct
if __name__ == '__main__':
    main()