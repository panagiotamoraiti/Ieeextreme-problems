W, H, A, B, M, C = input().split()
W = int(W)
H = int(H)
A = int(A)
B = int(B)
M = int(M)
C = int(C)

x = (W*H)/(A*B)
s1=W/A
s2=H/B

if W%A == 0:
    tiles1 = s1
else:
    tiles1 = int(s1+1)

if H%B == 0:
    tiles2 = s2
else:
    tiles2 = int(s2+1)
tiles = tiles1*tiles2

if tiles%10 == 0:
    piles_of_tiles = tiles /10
else:
    piles_of_tiles = int(tiles /10+1)

sl1=0
sl2=0
if tiles1*A-W>0:
    sl1 = H
if tiles2*B-H>0:
    sl2 = W
slicing = sl1 + sl2

dollars = piles_of_tiles*M + C*slicing
print(int(dollars))