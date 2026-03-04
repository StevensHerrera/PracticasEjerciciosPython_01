ancho=float(input("Ingresa el ancho de tu cuarto: "))
largo=float(input("Ingresa el largo de tu cuarto: "))
area=ancho*largo
if area>20:
    print("Tu cuarto es grande")
elif area<12:
    print("Tu cuarto es pequeño")
else:
    print("Tu cuarto es mediano")