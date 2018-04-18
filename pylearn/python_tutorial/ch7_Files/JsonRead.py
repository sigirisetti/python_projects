import json

with open('c:\\temp\\mr.txt', 'r') as f:
    jsonData = json.load(f)
f.closed

print(jsonData['data']['requestRef'])