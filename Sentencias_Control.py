"""
num=int(input('Ingrese un numero: '))

if num !=0:
    if num>0:
        if num%2==0:
            print(f'El numero {num} es par positivo')
        else:
            print(f'El numero {num} es impar positivo')
    elif num%2==0:
            print(f'El numero {num} es par negativo')
    else:
            print(f'El numero {num} es impar negativo')
else: 
    print(f'El numero {num} es neutro')   
"""
"""
vocal=input('Ingrese un dato: ')

if vocal=='a':
    print(vocal, 'Es vocal')
elif vocal=='e':
    print(vocal, 'Es vocal')
elif vocal=='i':
    print(vocal, 'Es vocal') 
elif vocal=='o':
    print(vocal, 'Es vocal')  
elif vocal=='u':
    print(vocal, 'Es vocal') 
else:
    print(vocal, 'No es vocal') 
"""
"""
con=1
while con<=10:
    print(con)
"""

"""
con=1
while con<=10:
    print(con)
    con+=1
"""

"""
num=int(input('Ingrese un numero: '))
con=1
suma=0
while con<=num:
    suma+=con
    con+=1

print(suma)
"""

"""
n=int(input('cantidad de numeros: '))
menor=0
i=1
while(i<=n):
    numero=int(input('Numero: '))
    if i==1:
        menor=numero
    elif numero<menor:
        menor=numero    
    i+=1
print(f'El numero menor es: {menor}')
"""

"""
palabra=['perro', 'gato', 'tigre']
for p in palabra:
    print(p, len(p))
"""

for i in range(5):
    print(i)