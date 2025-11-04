real_user = "edu"
real_password = "1234"
user = input("Introduce usuario: ")
password = input("Introduce contraseña: ")
if user == real_user and password == real_password:
    print("Inicio de sesion correcto")
elif user == real_user and password != real_password:
  print("Contraseña erronea")
elif user != real_user:
    print("usuario incorrecto")