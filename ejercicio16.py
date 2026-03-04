n1=float(input("Ingresa tu primera nota: "))
n2=float(input("Ingresa tu segunda nota: "))
n3=float(input("Ingresa tu tercera nota: "))
promedio=(n1+n2+n3)/3
if promedio>59:
    print("Usted aprobó")
elif promedio<55:
    print("Usted reprobó")
else:
    print("Usted va a habilitación")