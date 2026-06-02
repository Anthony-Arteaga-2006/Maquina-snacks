print("hola")
print("Mucho gusto")
Saldo= float(5.00)
print("Tienes un saldo de:", Saldo, "bs")
contador = 0
while Saldo >= 0:
    print("que desearihas comprar:")
    print("tenemos:")
    print("1 -papas fritas de 1.50bs")
    print("2 -chocolate de 2.00bs")
    print("3 -refresco de 2.50bs")
    Snack=input("seleccione la opción (1-4): ")
    print("escoja 4 si ya no quiere comprar o quiere finalizar la compra")

    if Snack == "1":
        precio=1.50
        print("----------------------------------------------------------")
        print("Compra exitosa de Papas Fritas")
        print("----------------------------------------------------------")
    elif Snack == "2":
        precio=2.00
        print("----------------------------------------------------------")
        print("Compra exitosa de Chocolate")
        print("----------------------------------------------------------")
    elif Snack == "3":
        precio=2.50
        print("----------------------------------------------------------")
        print("Compra exitosa de Refresco: Coca Cola")
        print("----------------------------------------------------------")
    elif Snack == "4":
        precio=0.00
        print("----------------------------------------------------------")
        print("compra finalizada")
        print("Gracias por su compra")
        print("----------------------------------------------------------")
        break
    else:
        print("Compra invalida")
        continue
    
    if Saldo >= precio:
        Saldo-=precio
        contador += 1
        precio+=precio
    else:
        print("Saldo insuficiente para comprar este producto")
print("----------------------------------------------------------")
print("cantidad total de productos comprados:", contador)
print("Pago total", precio,"bs")
print("Saldo Final: ", Saldo,"bs")
print("----------------------------------------------------------")
    
    
