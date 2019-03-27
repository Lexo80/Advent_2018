"""
Advent of code 2018
Day 1 star 1
"""

with open('puzzel.txt') as f:
    d= f.read()
    data = d.split('\n')
    frq = 0
    for element in data:
        if element[0] == '+':
            frq += int(element[1:len(element)])
        elif element[0] == '-':
            frq -= int(element[1:len(element)])
        else:
            pass       
    print(frq)
    