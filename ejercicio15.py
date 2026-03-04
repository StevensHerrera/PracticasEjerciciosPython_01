sueldo_mensual=float(input("Ingresa su sueldo mensual: "))
if sueldo_mensual>1500000<3500000:
    impuesto=sueldo_mensual*0.05
    print(f"Usted paga en impuestos: ${impuesto:,.2f} y sueldo neto es de: ${sueldo_mensual:,.2f}")
elif sueldo_mensual>3500000:
    impuesto=sueldo_mensual*0.10
    print(f"Usted paga en impuestos: ${impuesto:,.2f} y sueldo neto es de: ${sueldo_mensual:,.2f}")
else:
    print(f"Usted no paga impuestos y su saldo neto es de: $ {sueldo_mensual:,.2f}")