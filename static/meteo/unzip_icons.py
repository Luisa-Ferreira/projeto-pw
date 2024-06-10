import zipfile
import os

# Define paths
zip_file_path = '/home/luisinha/a22209718/meteo/static/meteo/icons_ipma_weather.zip'
extract_to_path = '/home/luisinha/a22209718/meteo/static/meteo/'

# Create the directory if it does not exist
os.makedirs(extract_to_path, exist_ok=True)

# Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print("Unzipping completed successfully!")
