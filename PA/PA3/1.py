import requests
import pandas as pd
import json

coords = {}
data = pd.read_csv('The data/comments.csv')['ip_label']

for ip in set(data):
    xy = requests.get(f'http://api.tianditu.gov.cn/geocoder?ds={{"keyWord":"{ip}"}}&tk=7e0ab0f65d4c0c55c82258fb79f7e100')
    xy = xy.json()

    print(xy)
with open('The data/location.json', 'w', encoding='utf-8') as f:
    json.dump(coords, f, ensure_ascii=False)
