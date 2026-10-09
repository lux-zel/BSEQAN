import os

with open('sequences.txt', 'r') as file:
    data = file.readline().split(',')

for i, j in enumerate(data[1:]):
    with open(f'{i}', 'x') as file:
        file.write(data[i])