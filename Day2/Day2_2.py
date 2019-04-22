"""

Advent of code 2018 day 2 part 2

"""

with open('puzzel.txt') as f:
    boxIds = [Id for Id in f.read().split('\n')]

# boxIds = ['abcde',
#           'fghij',
#           'klmno',
#           'pqrst',
#           'fguij',
#           'axcye',
#           'wvxyz']
errors = 0
found = False
common = ''
for row in boxIds:
    for otherlines in boxIds:
        if row not in otherlines:
            for i in range(len(row)):
                if row[i] != otherlines[i]:
                    errors += 1
            if errors <= 1:
                found = True
                for i, c in enumerate(row):
                    if c is otherlines[i]:
                        common += c
            errors = 0
    if found is True:
        break
print(f'common Letters: {common}')
common = ''
