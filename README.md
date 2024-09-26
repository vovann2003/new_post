# Nova Poshta API Data Extraction

This Python application retrieves data from the Nova Poshta API and exports information about areas, cities, and warehouses into an Excel file. It fetches and organizes the data in a structured format for easier analysis and use.

## Features
- Retrieves areas (regions) from Nova Poshta's API.
- Fetches all cities within a given area.
- Retrieves all warehouses in each city.
- Exports the area, city, and warehouse data into an Excel file.

## Requirements
The project depends on several Python libraries. These can be installed via pip from the `requirements.txt` file.

## Installation of dependencies:
```
pip install -r requirements.txt
```
## Setup
1. Clone the repository or download the project files.
2. In the root directory, create a .env file to store your API key and the Nova Poshta API base URL.
Example .env file:
```python
API_KEY="YOUR API KEY"
BASE_URL="https://api.novaposhta.ua/v2.0/json/"
```
3. Ensure your config.py file loads the environment variables from .env and stores them in a Config class. Here is the configuration structure:
```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    BASE_URL = os.getenv("BASE_URL")

config = Config()
```

## Running the Application

After setting up the environment variables and installing the necessary dependencies, you can run the script to collect data and save it to an Excel file:
```
python main.py
```
The program will fetch the following information:
- Area (Область): The name of the area (region).
- City (Місто): The name of the city within the area.
- Warehouse (Відділення): The name of the warehouse within the city.

All the data will be saved in an Excel file called `new_post.xlsx`.