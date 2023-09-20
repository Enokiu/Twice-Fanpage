import pymongo
import json
import os

# Verbindung zur MongoDB auf localhost und Standardport 27017
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Pfad zum Ordner, der die JSON-Dateien enthält
json_folder_path = "backend/mongoDB/wiki/"

# Durchsuchen Sie alle JSON-Dateien im Ordner
for filename in os.listdir(json_folder_path):
    if filename.endswith(".json"):
        json_file_path = os.path.join(json_folder_path, filename)

        # Extrahieren des Dateinamens ohne Erweiterung (z.B., "Twice")
        file_name_without_extension = os.path.splitext(os.path.basename(json_file_path))[0]

        # Auswahl der Datenbank "twice_website"
        mydb = myclient["twice_website"]

        # Auswahl der Sammlung mit dem Namen des Dateinamens ohne Erweiterung
        mycol = mydb[file_name_without_extension]

        # Öffnen und Laden der JSON-Datei
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # Einfügen der geladenen Daten in die MongoDB
        x = mycol.insert_many(data)

        # Überprüfen, ob die Daten erfolgreich eingefügt wurden
        if x.inserted_ids:
            print(f"{len(x.inserted_ids)} Dokumente aus {filename} wurden erfolgreich in die MongoDB eingefügt.")
        else:
            print(f"Keine Dokumente aus {filename} wurden in die MongoDB eingefügt.")
