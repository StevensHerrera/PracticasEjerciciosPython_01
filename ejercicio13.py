precio_producto=float(input("Ingresa el precio del producto: "))
descuento=precio_producto*0.10
precio_final=precio_producto+descuento
if precio_producto>100000:
    print(f"Precio final: ${precio_final:,.2f}")
elif precio_producto<=100000:
    print(f"Precio final: ${precio_producto:,.2f}")