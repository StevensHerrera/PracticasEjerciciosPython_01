kilometros=float(input("Ingrese el numero de kilometros recorridos: "))
tiempo=float(input("Ingrese el tiempo empleado en el viaje: "))
if tiempo<10:
    print("Valor a pagar: $5.000")
else:
    total=kilometros*800
    print(f"Valor a pagar : ${total:,.2f}")