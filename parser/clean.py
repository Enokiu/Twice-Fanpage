import re
import os

# Annahme: Alle Textdateien befinden sich im gleichen Verzeichnis wie dein Python-Skript.
# Du kannst auch ein bestimmtes Verzeichnis angeben, in dem die Dateien liegen.

# Verzeichnis mit den Textdateien
directory = "parser/wiki/"  # Aktuelles Verzeichnis

# Regulären Ausdruck definieren, um Text in eckigen Klammern zu finden und entfernen
pattern = r'\[.*?\]'

# Schleife über alle Textdateien im Verzeichnis
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
            text = file.read()
        
        # Text säubern
        cleaned_text = re.sub(pattern, '', text)
        
        # Gesäuberten Text in die Originaldatei schreiben (überschreiben)
        with open(os.path.join(directory, filename), "w", encoding="utf-8") as file:
            file.write(cleaned_text)

print("Alle Textdateien wurden gesäubert und die Originaldateien wurden überschrieben.")
