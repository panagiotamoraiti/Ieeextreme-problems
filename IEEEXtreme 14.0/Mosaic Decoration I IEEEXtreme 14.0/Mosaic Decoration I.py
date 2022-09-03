N, Cb, Cp = input().split()
N = int(N)
Cb = int(Cb)
Cp = int(Cp)

blist = []
plist = []

for i in range(N):
    B, P = input().split()
    B = int(B)
    P = int(P)
    blist.append(B)
    plist.append(P)

sumB = sum(blist)
sumP = sum(plist)


if sumP !=0:
    if sumP%10 == 0:
        a1 = sumP/10
    else:
        a1 = int(sumP/10 + 1)
else:
    a1 = 0
if sumB != 0:
    if sumB%10 == 0:
        b1 = sumB/10
    else:
        b1 = int(sumB/10 + 1)
else:
    b1 = 0

dollars = Cp*a1 + Cb*b1
print(int(dollars))