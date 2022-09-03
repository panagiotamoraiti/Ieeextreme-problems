T = int(input())
result = []
for i in range(T):
    M, N, K = input().split()
    M = int(M)
    N = int(N)
    K = int(K)

    floors = []
    for i in range(M):
        correct_rooms = int(input())
        while True:
            if correct_rooms>N or correct_rooms<0:
                correct_rooms = int(input())
            else:
                floors.append(correct_rooms)
                break
    floors.sort()
    res1=0
    res2=0
    for i in range(K):
        res1 = res1 + (N-floors[i])
    for i in range(K, len(floors)):
        res2 = res2 + floors[i]
    res = res1 + res2
    result.append(res)
for i in result:
    print(i)