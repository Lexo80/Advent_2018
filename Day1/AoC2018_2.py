"""
Advent of code day 1 part 2
"""
freqencys = set()
freqencys.add(0)
with open('puzzel2.txt') as f:
    data = f.read().split('\n')

#data = [+7, +7, -2, -7, -4]
#data = [+3, +3, +4, -2, -4]
#data = [-6, +3, +8, +5, -6]

resultFreq = 0
found = False
index = 0
while found is False:
    index += 1
    for change in data:
        resultFreq += int(change)
        if resultFreq in freqencys and found is False:
            found = True
            print(resultFreq)
        else:
            freqencys.add(resultFreq)
print(f"Anzahl Schleifen = {index}")
