A = int(input())
B = int(input())
C = int(input())
D = int(input())

achou = False
for x in range(C // D + 1):
    leite = C - x * D
    if A <= leite <= B:
        achou = True
        break

if achou:
    print("S")
else:
    print("N")
