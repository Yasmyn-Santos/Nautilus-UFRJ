#Exercício 03 - 2

def primos(n):
    """Retorna True se o número for primo, False caso contrário"""
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

soma = 0
for i in range(2, 1001):
    if primos(i):
        soma += i

print(soma)

