def cantidad_compañeros(cantidad):
    compañeros=[]
    for i in range(cantidad):
        nombre=input('Ingrese el nombre del compañero ')
        edad=(int(input('Ingrese la edad ')))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente=compañeros[0][0]
    profesor=compañeros[-1][0]
    return asistente,profesor,compañeros

cantidad=int(input('Ingrese la cantidad de compañeros'))
asistente,profesor,compa=cantidad_compañeros(cantidad)

print(f'El asistente es {asistente}')
print(f'El profesor es {profesor}')
print(compa)
    
    


