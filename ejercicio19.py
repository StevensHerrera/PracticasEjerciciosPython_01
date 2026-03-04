usuario=input("Ingresa tu usuario: ")
contra=int(input("Ingresa tu contraseña: "))
if usuario=="admin" and contra==1234:
    print("Acceso concedido")
else:
    print("Acceso denegado")