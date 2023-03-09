#Exercício 03

lista = list(range(1,1001))

lista_pares = []
lista_impares = []

i = 0

for a in lista:
    if lista[i]%2 == 0:
        lista_pares.append(lista[i])
    else: lista_impares.append(lista[i])
    i+=1

print(lista_pares)
print("\n\n\n")
print(lista_impares)
        
