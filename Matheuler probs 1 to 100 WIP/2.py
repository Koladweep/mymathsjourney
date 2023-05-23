sumf = 0
tprev = 1
tnow = 2

while tprev <= 4000000:
    if tprev%2==0:
        sumf += tprev
    tprev, tnow = tnow, tprev + tnow

print(sumf)
