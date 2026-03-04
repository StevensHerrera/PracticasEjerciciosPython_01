edad=int(input("Ingresa tu edad: "))
estrato=int(input("Ingresa tu estrato: "))
if 18>=edad<=25 and 1>=estrato<=3:
    print("Usted APLICA para el subsidio")
else:
    print("Usted NO APLICA para el subsidio")
