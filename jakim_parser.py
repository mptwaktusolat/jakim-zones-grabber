import json
from bs4 import BeautifulSoup

# Read HTML content from file
with open('data.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
options = soup.find_all('option')

result = []

for option in options:
    if 'value' in option.attrs:
        jakim_code = option['value']
        negeri = option.parent['label']
        daerah = option.text.split(' - ')[1].strip()
        result.append({
            'jakimCode': jakim_code,
            'negeri': negeri,
            'daerah': daerah
        })

# Write the result to a JSON file
with open('new.json', 'w') as file:
    json.dump(result, file, indent=2)

print("Data has been written to new.json successfully.")
