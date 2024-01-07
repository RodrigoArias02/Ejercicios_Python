actual=float(1.5)
lista=[2.5,7,4]
lista_palabras=["mas rapido","mas lento","promedio"]
i=0
for valor in lista: 
    porcentaje=100-actual*100/ valor
    print(f'el curso actual es un {round(porcentaje,2)}% menos que el {lista_palabras[i]}({valor}hs)')
    i=i+1
    
print(f'ver 10hs del curso actual equivale a {round(lista[2]/actual*10,1)}hs de un curso promedio')