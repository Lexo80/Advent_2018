"""
Advent of Code 2018 day 2
"""

with open('puzzel.txt') as f:
    boxIDs = [ID for ID in f.read().split('\n')]

# boxIDs = ['abcdef',
#           'bababc',
#           'abbcde',
#           'abcccd',
#           'aabcdd',
#           'abcdee',
#           'ababab']

keys = [set(rowelements) for rowelements in boxIDs]

twoDetect = False
threeDetect = False
cntTwos = 0
cntThrees = 0
for row in boxIDs:
    for oneset in keys:
        for key in oneset:
            if row.count(key) == 2:
                twoDetect = True
            if row.count(key) == 3:
                threeDetect = True
    if twoDetect is True:
        cntTwos += 1
        twoDetect = False
    if threeDetect is True:
        cntThrees += 1
        threeDetect = False
print(cntTwos * cntThrees)
