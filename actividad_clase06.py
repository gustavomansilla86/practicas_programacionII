# while True:
#  n1=float(input("ingresar un numero: "))
#  n2=float(input("ingrese otro numero: "))
#  suma=n1+n2
#  print(f"la suma de {n1} y {n2} es:{int(suma)}")

#  if suma < 10:
#     print("la suma es menor que 10")   
#  else:
#    break    

# lista_comas=input("ingrese lista de numero separados por la coma ")
# lista=(lista_comas.split())
# print(lista)

def envio():
    peso=int(input("ingrese el peso de paquete a enviar en hasta 26 kg: "))
    destino=str(input("ingrese destino al que desea enviar santa cruz/ chubut/ rio negro: "))
    if peso <= 26 and peso >= 11 and destino.lower() =="santa cruz":
         print("el costo de envio es de $400")
    elif peso <= 25 and peso >= 16 and destino.lower()=="chubut":
         print("el costo de envio es de $420")
    elif peso <= 26 and peso >= 19 and destino.lower()=="rio negro":
         print("el costo de envio es de $510")
    elif peso <= 10 and peso >= 6 and destino.lower() =="santa cruz":
         print("el costo de envio es de $300")
    elif peso >= 5 and destino.lower() =="santa cruz":
         print("el costo de envio es de $200")
    elif peso <= 15 and peso >= 11 and destino.lower()=="chubut":
         print("el costo de envio es de $390")
    elif peso >= 10 and destino.lower()=="chubut":
         print("el costo de envio es de $350")
    elif peso <= 18 and peso >= 13 and destino.lower()=="rio negro":
         print("el costo de envio es de $480")
    elif peso >= 12 and destino.lower()=="rio negro":
         print("el costo de envio es de $400")
    else:
         print("estan mal los parametros")  

envio()                  
