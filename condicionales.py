# vocal=input("ingresa una vocal en minusculla : ")
# if vocal== "a":
#     print("A")
# elif vocal=="e":
#     print("E")
# elif vocal=="i":
#     print("I")
# elif vocal=="o":
#     print("O")
# elif vocal=="u":
#     print("U")
# else:
#     print("No es una vocal")















"----Ejercicios con Condicionales y Operaciones Matemáticas----------------------------------------------------"

# "---------Ejercicio 1---------------------------------"
# num=int(input("Ingresa un numero :"))
# if num<0:
#     print(f"Es negativo por que es {num}")
# elif num>0:
#      print(f"Es positivo por que es {num}")
# else:
#     print(f"Es cero porque es {num}")


# "---------Ejercicio 2---------------------------------"

# a=int(input("ingresa un numero A :"))
# b=int(input("ingresa otro numero B :"))
# if a>b:
#     print(f"A es mayor porque es {a}")
# elif b>a:
#     print(f"B es mayor porque es {b}")
# else:
#      print(f"son iguales {a} y {b}")

# "---------Ejercicio 3---------------------------------"

# num=int(input("Ingresa un numero par :"))
# if num % 2 ==0:
#     print(f"el numero {num} es par ")
# else:
#     print(f"el {num}  no es par")

# "---------Ejercicio 4---------------------------------"
# num=int(input("Ingrese un numero que este entre 10 y 20 :"))
# if num>=10 and num<=20:
#     print(f"Si esta en el rango de 10 a 20 el numero {num}")
# else:
#     print(f"no esta dentro del rango")

# "---------Ejercicio 5---------------------------------"

# num1=int(input("Ingrese un numero A :"))
# num2=int(input("Ingrese un numero B :"))
# num3=int(input("Ingrese un numero C :"))

# if num1>num2 and num1>num3:
#     print(f"Este numero  A es mayor de los tres {num1}")
# elif num2>num1 and num2>num3:
#     print(f"Este numero  B es mayor de los tres {num2}")
# elif num3>num1 and num3>num2:
#     print(f"Este numero C es mayor de los tres {num3}")
# else:
#     print(f"todos son iguales {num1} y {num2} y el numero {num3}")

# "---------Ejercicio 6---------------------------------"

# precio=float(input(" Ingresa el precio de un producto: "))
# if precio>=100:
#     des=precio*0.10
#     print(f"esl costo es de {precio} y tineens un descuento del 10% te queda en {des}")
# else:
#     print(f"non tienes descuento {precio}")

# "---------Ejercicio 7---------------------------------"
# nobre=input("Como te llamas :")
# edad=int(input("Cuantos años tienes :"))
# if edad>=18:
#     print(f"Tu tines {edad} entonces puedes votar")
# else:
#     print(f"eres menor de eadd para votar  porque tines {edad}")

#"---------Ejercicio 8---------------------------------"
# Nombre=input("Ingresa tu nonbre : ")
# pre=float(input("ingresa el precio del libro :"))
# print("menbrecia  1 VIP  2 Normal :")
# men=int(input("cual es la tuya :"))
# if men==1:
#     des=pre*0.20
#     print(f"Tu libro queda en {des}")
# elif men==2:
#     print(f"Tu precio a pagar es {pre}")
# else:
#     (f"pon  1 o 2 no {men}")

# "---------Ejercicio 9---------------------------------"

# num=int(input("Ingresa un numero :"))
# if num % 5==0:
#     print(f"Este numero {num} es multiplo de 5") 
# elif num % 3==0:
#     print(f"Este numero {num} es multiplo de 3")
# else:
#     print(f"Es multiplo de 3 y 5 el numero {num}") 

#"---------Ejercicio 10---------------------------------"

# num1=int(input("Ingresa un numero :"))
# num2=int(input("Ingresa un numero :"))
# if num1 % 2 ==0 and num2 % 2 ==0:
#  print(f"ambos numero son divicibles  ")
# else:
#      print(f"no son divisibles")


"---------------Ejercicios con Listas (con condicionales)----------------------------------------------------"


#"-----------Ejercicio 11-----------------------------------------------------"
# num1=int(input("Ingresa un numero :"))
# num2=int(input("Ingresa otro numero :"))
# num3=int(input("Ingresa otro mas numero :"))
# num4=int(input("Ingresa otrico numero :"))
# num5=int(input("Ingresa ultimo numero :"))
# numeros=[]
# numeros.append(num1)
# numeros.append(num2)
# numeros.append(num3)
# numeros.append(num4)
# numeros.append(num5)
# print(numeros)

# if numeros[2]>10:
#     print(f"Este numero {num3} es mayor que 10")
# elif numeros[2]<10:
#     print(f"Este numero {num3} e smenor que 10")
# else:
#     print(f"este numero {num3}  igual a 10")

# "----------------------------Ejercicio 12------------"
# lista=[3,5,7,9]
# print(f"esta es la lista {lista}")
# if lista[2]==7:
#     print("el numero 7 esta en la lista")
# else:
#     print("no esta el 7")

# "----------------------------Ejercicio 13------------"

# numero=[4, 6, 2, 8]
# operacion=numero[0]+numero[1]
# if operacion>10:
#     print(f"Suma muy alta ")
# else:
#     print(f"suma muy baja")

# "----------------------------Ejercicio 14------------"

# nombres=["Ana", "Luis", "Pedro", "Marta"]

# if nombres[-1]=="Marta":
#     print(f"Nombre correcto {nombres[-1]}")
# else:
#     print(f"intruso")

"-------------------------EJERCICIO 15-----------------"

# colores=["Amerillo","Azul","Verde"]
# print(colores)
# if colores[1]=="Azul":
#     colores[1]="rojo"
#     print(f"la lista de colores queda asi {colores}")
# else:
#     print("No es azul ")

"--------------------------------------Ejercicios con Tuplas (con condicionales)------------------"

"-------------------------EJERCICIO 16-----------------"
# num=(5, 8, 12, 20)
# if num[0]<num[-1]:
#     print("orden acendente")
# else:
#     print("orden decendente")


"-----------------------Ejercicio 17-------------------------------------------------"
# edades=(25, 32, 28)
# if edades[1]>30:
#     print(f"edad mayor a 30 ")
# else:
#     print(f"edad menor igual a 30 ")

"-----------------------Ejercicio 18-------------------------------------------------"
# num=(1,2,3)
# print(num)
# mi_lista=list(num)
# print(mi_lista)
# if mi_lista[1]==2:
#     mi_lista[1]=10
#     tupla=tuple(mi_lista)
#     print(f"la lista qieda {mi_lista}  y la tupla en {tupla}")
# else:
#     print("no se cambia ningun valor")

"-----------------------Ejercicio 19-------------------------------------------------"

# num=(4,9)
# if num[1]> 5:
#     print(f"cordenada alta {num[1]}")
# else:
#     print(f"cordeenada baja {num[1]}")

"-----------------------Ejercicio 20-------------------------------------------------"

# num1=(3,4)
# num2=(3,5)

# if num1==num2:
#     print(f"tuplas iguales {num1} {num2} ")
# else:
#      print(f"tuplas  no son iguales {num1} {num2} ")



"----------------Ejercicios con Diccionarios (con condicionales)----------------"


"-----------------------Ejercicio 21-------------------------------------------------"

# datos={"nombre":"juan","edad":17}
# if datos["edad"]>=18:
#     print("Mayor de edad ")
# else:
#     print("Menor de edad")


"-----------------------Ejercicio 22-------------------------------------------------"


# datos1={"nombre": "Lucía", "edad": 20}
# print(datos1)
# if datos1["edad"]>18:
#     datos1["edad"]=21
#     print("mayor de edad")
#     print(datos1)
# else:
#     print("es menor de edad")


"-----------------------Ejercicio 23-------------------------------------------------"

# ciudad = {"nombre": "Carlos"}
# print(ciudad)
# if "ciudad" not in ciudad:
#     ciudad["ciudad"] = "Bogotá"

# print(ciudad)

"-----------------------Ejercicio 24-------------------------------------------------"


# producto = {"producto": "pan", "precio": 1200}
# print(producto)
# if "precio" in producto:
#     print(producto["precio"])
# else:
#     print("No hay precio")




"-----------------------Ejercicio 25-------------------------------------------------"
# ingredientes={"pan": 1200, "leche": 2000}
# print(ingredientes)

# if "pan" in ingredientes:
#      print(f"el precio es {ingredientes['pan']}")
# else:
#     print("no disponible")

#buecles 

    



















