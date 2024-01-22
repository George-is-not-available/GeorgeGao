import requests
import pandas as pd
import json

coords = {}

# Assuming your CSV file has a column named 'ip_label'
data = pd.read_csv('The data/comments.csv')['ip_label']

for ip in set(data):
    response = requests.get(
        f'http://api.tianditu.gov.cn/geocoder?ds={{"keyWord":"{ip}"}}&tk=7e0ab0f65d4c0c55c82258fb79f7e100')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        xy = response.json()

        # Extract relevant information from the response and store it in coords
        coords[ip] = {
            'latitude': xy.get('location', {}).get('lat', None),
            'longitude': xy.get('location', {}).get('lon', None),
        }
    else:
        print(f"Error for IP address {ip}. Status code: {response.status_code}")

# Save the coords dictionary to a JSON file
with open('The data/location.json', 'w', encoding='utf-8') as f:
    json.dump(coords, f, ensure_ascii=False)

print("Geolocation data has been saved to 'The data/location.json'")
