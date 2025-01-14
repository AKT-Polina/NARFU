from functools import reduce
sectences = ["научиться плести рыболовные сети",
"обучать нейронные сети", 
"паук ловит в сети мух"]
sum = reduce(lambda sectence: sectence.count('сети'), sectences)
print(sum)