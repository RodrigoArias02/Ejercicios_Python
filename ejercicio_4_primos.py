# def primos(i):
#     lista_primos=[]
#     divisor=1
#     for valor in range(2,i+1):
#         divisor=1
#         acumulador=0 
#         while divisor<=valor:
#             if(valor%divisor==0):
#                 acumulador=acumulador+1
#             divisor=divisor+1
#         if acumulador==2:
#             lista_primos.append(valor)
#         elif acumulador>2:
#             acumulador=0
#     return lista_primos
        
# numeros_primos=primos(100)

# print(numeros_primos)

def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True
def primos_hasta(num):
    primos=[]
    for i in range(3,num+1):
        resultado=es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado=primos_hasta(100)
print(resultado)
        