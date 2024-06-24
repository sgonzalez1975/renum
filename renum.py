import os
import sys

cnt = 1
if len(sys.argv) > 1:
    cnt = int(sys.argv[1])
path = os.getcwd()
arr = [[f.stat().st_mtime_ns, f.name] for f in os.scandir(path) if f.is_file() and f.name[-1] not in ['t', 'y', 'd']]
arr.sort(reverse = True)
cant = len(str(len(arr)+1+cnt))
cnt = cnt + len(arr)
#print(cant) 
for f in arr:
    pos = f[1].rfind(".")
    if pos <= 0:
        continue
    pos += 1
    cnt -= 1
    nomdest = str(cnt).zfill(cant) + "." + f[1][pos:]
    print(f[1], nomdest)
    os.rename(f[1], nomdest)
