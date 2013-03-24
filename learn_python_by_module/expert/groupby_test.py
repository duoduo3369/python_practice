from itertools import groupby

data = '11111111111gggg get sadfffffff'
L = [(name, len(list(group)))for name, group in groupby(data)]
print L
    
