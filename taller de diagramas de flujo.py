# #ejercicio con condicionales y operaciones matematicas
# #1
# numero=float(input("ingrese un numero "))
# if numero < 0 :
#     print("el numero ingresado es negativo")
# elif numero== 0 :
#     print("el numero ingresado es cero")
# else :
#     print ("el numero es positivo")
# #2
# num1,num2 = int(input("ingresa un numero")),int(input("ingresa un segundo numero"))
# resul = (num1 * (num1 > num2)) + (num2 * (num2 > num1))
# print (f"el mayor de los numeros ingresados es {resul}")
# #3
# numero_par = int(input("ingrese un numero "))
# numero_par_proceso = (numero_par // 2) * 2
# if numero_par_proceso == numero_par :
#     print ("el numero es par")
# else :
#     print("el numero es impar")
# #4
# nume = int(input("ingrese un numero "))
# if nume >= 10 and nume <=20 : 
#     print ("el numero esta entre 10 y 20")
# else :
#     print("El numero no esta entre 10 y 20")
# #5
# nume1,nume2,nume3 = int(input("ingresa un numero")),int(input("ingresa un segundo numero")),int(input("ingresa un tercer numero"))
# if nume1 > nume2 and nume1 > nume3 :
#     print(f"el numero {nume1} es el mayor de todos")
# elif nume2 > nume1 and nume2 > nume3 :
#     print(f"el numero {nume2} es el mayor de todos")
# if :
#     print(f"el numero {nume3} es el mayor de todos")
# #6
# la_mari = [int(input("ingresa el precio del primer producto")),int(input("ingresa el precio del segundo producto")),int(input("ingresa el precio del tercer producto")),]
# la_marit = la_mari[0] + la_mari[1] + la_mari[2]
# if la_marit < 100:
#     print(f"el precio de sus productos con descuento incluido es de {la_mari - 10%}")
# else:
#     print(f"el precio de su producto es {la_mari}")
    
# #7
# edd = int(input("ingrese su edad "))
# if edd >= 18:
#     print("usted es mayor de edad, usted purde votar")
# else :
#     print("usted no puede votar")
#8 
cliente = [float(input("ingrese el total de sus compras")),input("usted es vip, ¿si o no?").upper]
if cliente[1] == "SI":
    print(f"su total es de {cliente[0] - 20} que tenga un buen dia")
else :
    print(f"su total es {cliente} que tenga un buen dia")
#9
# nume4 = int(input("ingrese el num"))