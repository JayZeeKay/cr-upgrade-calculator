#! python3
import requests
import json
import pyperclip
r=requests.get("https://api.clashroyale.com/v1/players/%23PLJRPG9J", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEwYmMwYTEyLWY1NTQtNDY3ZS04ZjQzLTRhNmU5MjYwNDM0MiIsImlhdCI6MTU2MDU0OTk4NSwic3ViIjoiZGV2ZWxvcGVyLzFlMjZmZTUwLWI1OTQtZTZkYy05ZDIxLTlmOGEyNDk4NmJjMCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0Ny4xNDUuNTUuMjIiXSwidHlwZSI6ImNsaWVudCJ9XX0.EQz-4iQf7Z7hKNptML692n7tSvP9tc9KypYRixqeqoWrmT3zVDXbqUYmrpH7Q8xhuTm1GHMPwyHVUu4D0UZSTg"}, params = {"limit":20})
print(json.dumps(r.json(), indent = 2))
pyperclip.copy(json.dumps(r.json(), indent = 2))

deck = {
  '1': {
    'name': '',
    'level': '',
    'cardAmount': '',
    'rarity': '',
    'cost': '',
    'cardNeeded': '',
    'time': '',
    'xp': ''
  },   
}

card_rarity = {
    'Poison': 'Epic'
    }

card_amount_epic = {
    '6': 1,
    '7': 2,
    '8': 4,
    '9': 10,
    '10': 20,
    '11': 50,
    '12': 100,
    '13': 200

card_amount_epic_total = 0

cards = r.json()["cards"]
for c in cards:
    if c["level"] != 13:
        level = c["level"]
        if card_rarity[c['name']] == 'Epic':
            
