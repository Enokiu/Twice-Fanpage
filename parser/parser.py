import os
import requests
from bs4 import BeautifulSoup
import json
import re

# Erstelle einen Ordner, wenn er nicht existiert
def create_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


# Extrahiert den Inhalt (Paragraph und Überschrift) der Wikipedia-Seite und speichert ihn in einer Textdatei
def extract_wiki(url, output_filename):
    # HTTP-Anfrage senden
    response = requests.get(url)

    # BeautifulSoup verwenden, um den HTML-Inhalt zu analysieren
    soup = BeautifulSoup(response.text, 'html.parser')

    # Den Inhalt mit dem angegebenen ID-Attribut extrahieren
    content = soup.find('div', {'id': 'mw-content-text'})

    # Textdatei öffnen, um den Inhalt zu speichern
    with open(output_filename, "w", encoding="utf-8") as file:
        # Alle Absätze, Überschriften (<h2>, <h3>) und anderen Inhalt durchgehen
        for element in content.find_all(['p', 'h2', 'h3']):
            if element.name == 'p':
                # Wenn es sich um einen Absatz handelt, Text speichern
                text = element.get_text(separator=' ', strip=True)  # Leerzeichen als Separator hinzufügen
                if text:
                    # Manuell Leerzeichen vor Klammern, Kommas und anderen Zeichen entfernen
                    text = re.sub(r'\s+([,])', r'\1', text)
                    text = re.sub(r'\s*([\'"\[\]])\s*', r'\1', text)
                    text = re.sub(r'\s*\(\s*', r' (', text)  # Nur ein Leerzeichen vor der öffnenden Klammer hinzufügen
                    text = re.sub(r'\s*(\)|\]|\}|\>)', r' \1', text)  # Leerzeichen vor Sonderzeichen hinzufügen
                    text = re.sub(r'\s*&\s*', r' & ', text)  # Leerzeichen vor und nach '&' hinzufügen
                    text = re.sub(r'"', r' " ', text)  # Leerzeichen vor und nach dem doppelten Anführungszeichen hinzufügen
                    text = re.sub(r'\s*\.\s*', r'.', text)  # Kein Leerzeichen vor dem Punkt hinzufügen
                    file.write(text + '\n')
            elif element.name in ['h2', 'h3']:
                # Wenn es sich um eine Überschrift handelt, einen Absatz erstellen und die Überschrift speichern
                header_text = element.get_text(strip=True)
                if header_text:
                    file.write(f'\n{header_text}\n')


# Extrahiert den Slogan in einer Textdatei
def extract_slogan(url, output_filename):
    # HTTP-Anfrage senden
    response = requests.get(url)

    # BeautifulSoup verwenden, um den HTML-Inhalt zu analysieren
    soup = BeautifulSoup(response.text, 'html.parser')

    # Das gewünschte Element finden
    target_element = soup.find('td', {'style': 'font-style:italic; padding:4px 2px; font-size:14px;'}).find('p')

    # Den Text ohne <br> und mit Zeilenumbruch erhalten
    text = target_element.get_text(separator='\n', strip=True)

    # Verzeichnis erstellen, wenn es nicht existiert
    output_dir = "parser/wiki"
    os.makedirs(output_dir, exist_ok=True)

    # Den Text in die Datei schreiben
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(text)

# Hauptfunktion
def main():
    # JSON-Datei lesen
    with open('parser/links.json', 'r') as json_file:
        data = json.load(json_file)

    # Zugriff auf die Links
    wiki_links = data['wiki_links']
    slogan_url = data['slogan_link']

    # Erstellen Sie den Ordner "parser/wiki", wenn er nicht existiert
    output_folder = "parser/wiki"
    create_output_folder(output_folder)

    # Schleife durch die Liste der Wikipedia-Links
    for link in wiki_links:
        filename = os.path.join(output_folder, f"{os.path.basename(link)}.txt")
        extract_wiki(link, filename)
        print(f"{link} wurde erfolgreich extrahiert und in '{filename}' gespeichert.")

    # Dateiname für den Slogan
    slogan_filename = os.path.join(output_folder, "slogan.txt")

    extract_slogan(slogan_url, slogan_filename)
    print(f"Der Slogan wurde erfolgreich extrahiert und in '{slogan_filename}' gespeichert.")

if __name__ == "__main__":
    main()
