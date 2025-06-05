cliente = [float(input("ingrese el total de sus compras ")),input("¿usted es cliente vip, si o no? ").upper()]
if cliente[1] == "SI":
    print(f"su total es de {cliente[0] - 20%} que tenga un buen dia")
else :
    print(f"su total es {cliente} que tenga un buen dia")