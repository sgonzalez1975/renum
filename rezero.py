
import re
import os

path = os.getcwd()
arr = [f.name for f in os.scandir(path) if f.is_file() and f.name[-1] not in ['t', 'y', 'd']]

tam_max = 0
cambs = []
for nom in arr:
    pos = nom.rfind('.')
    if (pos < 0):
        continue
    match = re.search(r'\d', nom)
    if not match:
        continue
    pos_n = match.start()
    #print(pos_n)
    if (pos_n < 0):
        continue    
    pos2 = pos_n
    resto = nom[pos_n:]
    match = re.search(r'\D', resto) #localiza un no digito
    pos2 = match.start()
    if (pos2 > 0 and pos2 + pos_n < pos):
        pos = pos2 + pos_n
    if (pos > tam_max):
        tam_max = pos
    cambs.append([nom, pos, pos_n])
#print(tam_max)
origs = []
for nom, tam, pos_n in cambs:
    cant = tam_max - tam
    if (cant > 0):
        #rellena de ceros
        nomdest = nom[:pos_n] + '0'*cant + nom[pos_n:]
        print(nom, "=>", nomdest)
        os.rename(nom, nomdest)
    else:
        origs.append(nom)
print("sin cambios:", origs)
