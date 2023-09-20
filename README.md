# Twice Fanpage Project

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Technologies Used](#technologies-used)
- [Program Execution Flow](#program-execution-flow)
- [Running the Program](#running-the-program)
- [Text File Cleaning (Optional)](#text-file-cleaning-optional)
- [Website](#website) <!-- Added this section -->
- [Note](#note)

## Project Overview

This provides an overview of the "Twice Fanpage" project, detailing the development process, technologies utilized, and the structure of the GitHub repository. The project aims to extract, clean, and store information from Wikipedia pages about the K-pop group Twice. The extracted data is then transformed into JSON format and inserted into a MongoDB database for future retrieval on a website.

## Repository Structure

The GitHub repository is organized as follows:

### `backend/parser`

This directory contains Python scripts responsible for parsing Wikipedia pages.

- **`wiki`**: A folder containing text files where information from Wikipedia pages is stored.

- **`links.json`**: A JSON file containing the Wikipedia links for Twice's pages and a link to their slogan.

### `backend/mongoDB`

Here, JSON files are generated for MongoDB and inserted into the database.

- **`wiki`**: A directory containing JSON files that store cleaned information from Wikipedia pages in a structured format for MongoDB.

## Technologies Used

The project leverages the following technologies and libraries:

- **Python**: The primary programming language for the project.

- **Requests**: A Python library for sending HTTP requests to retrieve content from Wikipedia pages.

- **BeautifulSoup**: A Python library used to parse HTML content for information extraction.

- **JSON**: Utilized for reading and writing JSON files.

- **MongoDB**: A NoSQL database used to store the cleaned data in the form of structured JSON documents.

## Program Execution Flow

The program follows these key steps:

1. **Extraction of Wikipedia Pages**: Wikipedia pages related to Twice are downloaded, and their content is saved in text files. This process includes extracting headers and paragraphs.

2. **Text Cleaning**: The text in the text files is cleaned to remove unwanted spaces and characters.

3. **Conversion to JSON**: The cleaned text is transformed into JSON files, with headers and paragraphs structured appropriately.

4. **Insertion into MongoDB**: The JSON files are inserted into the MongoDB database, with each Wikipedia page stored in its own collection.

## Running the Program

To execute the program, invoke the `main()` function in your Python script. This will initiate the entire process, including extraction, cleaning, JSON conversion, and insertion into MongoDB.

## Text File Cleaning (Optional)

If you wish to further clean the text files, a separate script in the code removes square brackets and specific characters.

## Website

- **Incoming** <!-- Added this section -->

## Note

- Ensure that MongoDB is running on your local system to enable successful database access.
- Verify that all required libraries (Requests, BeautifulSoup, pymongo) are installed for the script to function smoothly.

This provides a comprehensive overview of the Twice Fanpage project's structure, technologies, and execution flow. It serves as a valuable resource for contributors and users of the GitHub repository. Good luck with the development of your website!
