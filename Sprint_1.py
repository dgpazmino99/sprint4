#%%
# Escriba un programa en Phyton que le pida al usuario que ingrese 5 nombres, 
# el programa debe imprimir el nombre y un mensaje que diga si su longitud es par o impar

nombres= []
contador= 0

while contador < 5 :
   nombre= input("Ingrese un nombre")
   nombres.append(nombre)
   contador += 1
print("Los nombres que ingresaste son: ", nombres)

for contador,nombres in enumerate(nombres,1):
   if contador%2==0: 
    print(nombres,"par")
   else:
    print(nombres,"impar")

# %%
