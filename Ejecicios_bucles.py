print("EJERCIICIOS CO WHILE, CONDICIONALE Y ESTRUCTURAS ")



# print("---------------------------------EJERCICIO 1 ---suma hasta cero -------------------------------------------- ")
# num=0

# while True:
#     Numero=int(input("ingresa un numero entero  :"))
#     if Numero>0:
#         num +=Numero
#     else:
#         break
# print(f"se cerro el promgrama")

    

# print("------------------------jercicio -2--------------------------------")

# contra=""
# while contra !="python1215":
#     contra=input("ingresa la contraseña : ")
# print("contraseña correcta")


# print("------------------------jercicio -3--------------------------------")

# productos=[]
# while True:
#     pro=input("ingresa un producto :")
#     if pro=="fin":
#         break
#     productos.append(pro)
# print(f"En total pediste: {productos}")

# print("------------------------jercicio 4--------------------------------")

# numero=[]
# numeros_pares=[]
# numeros_inpares=[]

# while True:
#     numeros=int(input("Ingresa un numero :"))
#     if numeros==10:
#         break
# if  numeros % 2 ==0:
#     numeros_pares.append(numeros)
#     print("Los numeros pares son ")
# else:
#     numero.append(numeros)
#     print(f"la lisat es  {numero} , los pares son {numeros_pares} y los numero impares son {numeros_inpares}")

# print("------------------------jercicio 5--------------------------------")

# notas=[]
# while True:
#     nota=float(input("ingresa tus notas : "))
#     pre=input("si deseas salir pon 'salir':")
#     if pre=="salir":
#         pro=sum(notas)/len(notas)
#         break
#     notas.append(nota)

# print(f"la lista  de las  notas queda asi {notas} y tu promedio queda {pro} ")




# print("------------------------jercicio 6--------------------------------")

# numero=int(input("Ingresa el numero de la tabla que vas a multiplicar  a multiplicar :"))
# i =1

# while i<= 10 : 
#     print(f"{numero}*{i} = {numero * i}")
#     i +=1


# print("------------------------jercicio 7--------------------------------")


# numero=17
# while True:
#     num=int(input("Ingresa el numero secreto :"))
#     if num>17:
#         print("menor")
#     elif num<17:
#         print("mayor")
#     else:
#         print("ganate la rifa ")
#         break


# print("------------------------jercicio 8--------------------------------")

# frutas="manzana"
# while True:
#      fru=input(" adivina la fruta :")
#      if fru!="manzana":
#          print("No es  esta fruta")
#      else:
#          print("felicidades esta es la fruta")
#          break



# print("------------------------jercicio 9--------------------------------")

# palabras={
#     "perro":  "dog",
#     "rojo":  "red",
#     "carro": "car",
#     "futbol": "socer",
#     "alegria": "happy"   
# }
# while True:
#     palabra=input("Ingresa una palabra en español ejemplo (perro, rojo,carro,futbol,alegria ) :")
#     if palabra in palabras:
#         print(f"la palabra que pusite es {palabra} y en ingles es {palabras[palabra]}")
#         break
#     else:
#         print("no esta aqui adentro")



# print("------------------------jercicio 10--------------------------------")


# operaciones={
#      "1": "Sumar",
#      "2": "Restar",
#      "3": "Multiplicar",
#      "4": "Dividir",
#      "5": "Salir"

#  }

# while True:
#     numero1=int(input("ingresa un numero :"))
#     numero2=int(input("ingresa otro numero :"))
#     print(operaciones)
#     pre=input("que operacion quieres : ")
#     if pre==1:
#         suma=numero1+numero2
#         print(f"la suam de {numero1} y {numero2} {suma}")
#     elif pre==2:
#         resta=numero1-numero2
#         print(f"la resta de {numero1} y {numero2} es {resta}")
#     elif pre==3:
#         multi=numero1*numero2
#         print(f"la multiplicacion de {numero1} y {numero2} es {multi}")
#     elif pre==4:
#         divi=numero1/numero2
#         print(f"la divicion de {numero1} y {numero2} es {divi}")
#     elif pre==5:
#         print("salir")
#     else:
#         break
#     print("se paso del  numero 5 ")



# print("------------------------jercicio 11--------------------------------")

# nombres={}

# while True:
#     persona=input("ingresa el nombre : ")
#     edad=int(input("ingresa la edad :"))
#     if persona=="salir":
#         break
#     nombres[persona]=edad
#     print(nombres)


# print("------------------------jercicio 12--------------------------------")

# colores=["azul","verde","rojo","amarillo","negro"]
# res=input("ingresa el color secreto :")
# while res.lower() not in colores:
#     print("color no encontrado")
#     res = input("ingresa otro color: ")
# print("perfecto si esta")


# print("------------------------jercicio 13--------------------------------")
# num=int(input("ingresa el numero"))
# a=1
# print(f"empezamos con la potencia del {num}")
# while a<=5:
#     print(f"el numero {num}**{a} va as er igual a {num**a} ")
#     a+=1

# print("------------------------jercicio 14--------------------------------")
# cuadrados = []
# contador = 0

# while contador < 5:
#     numero = float(input("Ingrese el número "))
#     cuadrados.append(numero ** 2)
#     contador += 1

# print(f"tu lista de cuadrador queda asi {cuadrados}")



# print("------------------------jercicio 15--------------------------------")


# estudiantes = {}

# while True:
#     nombre = input("nombre de estudiantes : ")
#     nota_final=float(input("ingresa su nota final :"))
#     if nombre=="fin":
#         break
#     estudiantes[nombre]=nota_final
#     print(estudiantes)

