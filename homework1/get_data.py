import json
import numpy as np
import matplotlib.pyplot as plt

data_json = open('data_rank_default.json', encoding="utf-8")
data_csv = open('data_rank.csv', 'r')
data_txt = data_json.read()

j = json.loads(data_txt)
print(j[0])

scale = []

for obj in j:
    scale.append(float(obj["league"]["gamesPlayed"]))



data_json.close()