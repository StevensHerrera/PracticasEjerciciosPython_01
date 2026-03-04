precioproducto=float(input("Ingresa el precio del producto: "))
descuento=precioproducto*0.10
preciofinal=precioproducto+descuento
if precioproducto>100000:
    print(f"Precio final: ${preciofinal:,.2f}")
elif precioproducto<=100000:
    print(f"Precio final: ${precioproducto:,.2f}")