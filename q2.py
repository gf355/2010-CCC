a = int(input(''))
b = int(input(''))
c = int(input(''))
d = int(input(''))
s = int(input(''))
roundn = s // (a+b)
leftn = s - roundn * (a + b)
roundb = s // (c+d)
leftb = s - roundb * (c + d)
if leftn > a:
    forwardn = a
    backn = leftn - a
else:
    forwardn = leftn
    backn = 0

if leftb > c:
    forwardb = c
    backb = leftb - c
else:
    forwardb = leftb
    backb = 0

resultn = roundn * (a - b) + forwardn - backn
resultb = roundb * (c - d) + forwardb - backb

if resultn > resultb:
    print('Nikky')
else:
    print('Byron')

