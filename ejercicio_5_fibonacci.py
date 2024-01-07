def suma(num1,num2):
    resultado= num1+num2
    return resultado
    

def fibo(numero):
    a,b=0,1
    fibonacci=[0]
    for i in range(numero):
        if b > numero: return fibonacci
        else:
            fibonacci.append(b)
            a,b = b,a+b
        


resultado=fibo(20)
print(resultado)
        
        
        
        
