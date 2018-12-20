import json
from funcs import write_result

path = 'q.json'

with open(path) as f:
    data = json.load(f)
    for i in data:
        print(i['normalized_ean'])
        text = (i['normalized_ean']+',')
        p=(len(i['image_reserve']))
        for x in range (p):
            text = text + i['image_reserve'][x]+','
        text=text+'\n'
        print(text)
        write_result('items.csv',text)