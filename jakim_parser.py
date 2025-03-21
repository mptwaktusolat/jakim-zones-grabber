import json
import requests
import os
from bs4 import BeautifulSoup

# First, read the existing locations.json if it exists
old_data = []
if os.path.exists('locations.json'):
    try:
        with open('locations.json', 'r') as file:
            old_data = json.load(file)
        print("Successfully loaded existing data from locations.json for comparison")
    except Exception as e:
        print(f"Error loading existing locations.json: {e}")
        old_data = []

# Fetch HTML content from the website
url = 'https://www.e-solat.gov.my/'
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    html_content = response.text
    print("Successfully fetched data from e-solat.gov.my")
except requests.exceptions.RequestException as e:
    print(f"Error fetching the website: {e}")
    exit(1)

soup = BeautifulSoup(html_content, 'html.parser')
# Find the inputzone element and extract options from it
input_zone = soup.select_one('#inputzone')
if not input_zone:
    print("Could not find #inputzone element on the page")
    exit(1)
    
options = input_zone.find_all('option')

result = []

for option in options:
    if 'value' in option.attrs and option['value']:  # Ensure value is not empty
        jakim_code = option['value']
        parent_element = option.find_parent('optgroup')
        if parent_element and 'label' in parent_element.attrs:
            negeri = parent_element['label']
            daerah_parts = option.text.strip().split(' - ')
            if len(daerah_parts) > 1:
                daerah = daerah_parts[1].strip()
            else:
                daerah = option.text.strip()
            
            result.append({
                'jakimCode': jakim_code,
                'negeri': negeri,
                'daerah': daerah
            })

# Write the result to a JSON file
with open('locations.json', 'w') as file:
    json.dump(result, file, indent=2)

print("Data has been written to locations.json successfully.")

# Compare with previously loaded data to detect zone changes
if old_data:
    # Extract jakimCodes from both old and new data
    old_codes = {item['jakimCode'] for item in old_data}
    new_codes = {item['jakimCode'] for item in result}
    
    # Find added and removed zones
    added_zones = new_codes - old_codes
    removed_zones = old_codes - new_codes
    
    # Print the changes
    if added_zones or removed_zones:
        print("\n--- ZONE CHANGES DETECTED ---")
        
        if added_zones:
            print("\nNEW ZONES ADDED:")
            for code in sorted(added_zones):
                zone = next(item for item in result if item['jakimCode'] == code)
                print(f"  + {code} - {zone['negeri']} ({zone['daerah']})")
        
        if removed_zones:
            print("\nZONES REMOVED:")
            for code in sorted(removed_zones):
                zone = next(item for item in old_data if item['jakimCode'] == code)
                print(f"  - {code} - {zone['negeri']} ({zone['daerah']})")
    else:
        print("No zone changes detected between previous and current data.")
else:
    print("\nNo previous data available for comparison. This appears to be the first run.")
