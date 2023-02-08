import sys
a=sys.stdin.readline()
b=sys.stdin.readline().split()
max=int(b[0])
min=int(b[0])
for i in b:
    if min>int(i):
        min=int(i)
    if max<int(i):
        max=int(i)
print(min,max)