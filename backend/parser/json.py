import os
import json

#Ändert TXT-Datei in JSON-Datei um für MongoDB Datenbank
def create_json_files_for_wiki_folder(input_folder, output_folder):
    # Überprüfen Sie, ob der Ausgabeordner existiert, andernfalls erstellen Sie ihn
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Durchsuchen Sie alle Dateien im Eingabeordner
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json")

            with open(input_file_path, "r", encoding="utf-8") as file:
                text = file.read()

            sections = [section.strip() for section in text.split('\n\n')]

            data = []
            id_counter = 1

            for section in sections:
                content = section.strip()
                if '\n' in content:
                    headline = content.split('\n')[0]
                else:
                    headline = None

                data.append({"id": id_counter, "section": headline, "content": content})
                id_counter += 1

            with open(output_file_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=2)

# Verwenden Sie die Funktion für den "wiki" Ordner
input_folder = "backend/parser/wiki"
output_folder = "backend/mongoDB/wiki"

create_json_files_for_wiki_folder(input_folder, output_folder)
