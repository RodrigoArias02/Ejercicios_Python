from prettytable import PrettyTable
myTable = PrettyTable(["Producto", "Cantidad", "Precio x unidad"])
Lista_productos=[]
Lista_cantidad=[]
lista_precio_unidad=[]
valor='si'

while valor=="si":
    Lista_productos.append(input("Ingrese producto: "))
    print("\n")
    Lista_cantidad.append(int(input("Ingrese la cantidad comprada del producto: ")))
    print("\n")
    lista_precio_unidad.append(int(input("Ingrese precio por unidad ")))
    print("\n")
    valor = input("Desea ingresar otro producto? si/no: ")
    print("\n")

total=float(0)
for valor_a, valor_b in zip(lista_precio_unidad, Lista_cantidad): #obtenemos los valores en cada iteración
    multi=valor_a * valor_b
    total=total+multi

iva=total*0.19

for valor_a, valor_b, valor_c in zip(Lista_productos, lista_precio_unidad, Lista_cantidad):
    myTable.add_row([valor_a, valor_b, valor_c])
    
print(myTable)
print("El total es: ", total+iva)
    