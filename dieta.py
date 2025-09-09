N, M = map(int, input().split())

total = 0
for _ in range(N):
    P, G, C = map(int, input().split())

    calorias = P * 4 + G * 9 + C * 4
    total += calorias
print(M - total)