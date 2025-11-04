"""
Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto  
"""
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