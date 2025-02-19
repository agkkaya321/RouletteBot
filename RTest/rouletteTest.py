from commonFunc import * 
from Strategys import *

positive = 0
negative = 0
pourcent = 10000

for i in range(pourcent):
    b = classiqueRNCustom()
    if b:
        positive +=1
    else:
        negative +=1

print(str(positive/pourcent))
