n = int(input())
valores = list(map(int, input().split()))
h = max(valores)


for i in range(h):
    linha = []
    for valor in valores:
        if valor >= h - i:
            linha.append('1')
        else:
            linha.append('0')
    print(' '.join(linha))