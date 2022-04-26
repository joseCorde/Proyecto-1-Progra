def limpiar_terminal():
    print (chr(27) + "[2J")
def login():
 print("---------------------------------------------")
 print("** Bienvenido a tu administrador de tiempo **")
 print("---------------------------------------------")
 print("------Por favor ingrese su usuario-----------")
 usua=input()
 print("------Por favor ingrese su contraseña--------")
 contra=input()
 from menuadministrador import menu_adminis
 from Menuestudiante import menu_estu
 if usua=="yindra" and contra=="yindra9":
   limpiar_terminal()
   menu_adminis()
 if usua=="Luis" and contra=="Luis12":
   limpiar_terminal()
   menu_estu()
 if usua=="" and contra=="":
    print("Usuario y contraseña incorrecta vuelva a intertar")
    login()
login()
 


