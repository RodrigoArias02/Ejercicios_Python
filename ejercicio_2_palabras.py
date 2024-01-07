texto = str(input("Ingrese un texto:" ))
cadena_separada=texto.split(' ')
cantidad=len(cadena_separada)
print(f'La cantidad de palabras escritas son: {cantidad}')
segundos=cantidad/2
print(f'Tardaria {segundos}s en decirlas')
tiempo_dalto=segundos-(segundos*30/100)

print(f'dalto diria eso mismo en {tiempo_dalto}s')
if segundos>=60:
    print("hablas mucho bro")