
import re
import os

path = os.getcwd()
arr = [f.name for f in os.scandir(path) if f.is_file() and f.name[-1]!='t' and f.name[-1]!='y']

tam_max = 0
cambs = []
for nom in arr:
    pos = nom.find('.')
    if (pos < 0):
        continue
    pos2 = nom.find('-')
    if (pos2 > 0 and pos2 < pos):
        pos = pos2
    if (pos>tam_max):
        tam_max = pos
    cambs.append([nom, pos])
#print(tam)
origs = []
for nom, tam  in cambs:
    cant = tam_max - tam
    if (cant > 0):
        #rellena de ceros
        match = re.search(r'\d', nom)
        if match.start() >= 0:
            nomdest = nom[:match.start()] + '0'*cant + nom[match.start():]
            print(nom, "=>", nomdest)
            os.rename(nom, nomdest)
    else:
        origs.append(nom)
print("sin cambios:", origs)
