E = int(input())  
S = int(input()) 
L = int(input()) 


caminho1 = abs(E - S) + abs(S - L) + abs(L - E)

caminho2 = abs(E - L) + abs(L - S) + abs(S - E)

print(min(caminho1, caminho2))