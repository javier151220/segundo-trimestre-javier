
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

#javier