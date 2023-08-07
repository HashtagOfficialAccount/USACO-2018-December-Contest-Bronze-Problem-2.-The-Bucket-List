import sys

sys.stdin = open("blist.in","r")
sys.stdout = open("blist.out","w")

N = int(input())
y = []
for i in range(N):
    x = [int(x) for x in input().split()]
    y.append(x)

start = 1001
end = 0

for i in y:
    if (i[0]) < start:
        start = i[0]
    elif i[1] > end:
        end = i[1]
        
max_buckets = 0
buckets = 0
for i in range(start,end+1):
    buckets = 0
    for r in y:
        if i >= r[0] and i <= r[1]:
            buckets += r[2]
    if buckets > max_buckets:
        max_buckets = buckets
print(max_buckets)
