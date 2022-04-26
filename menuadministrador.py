from itertools import permutations
from time import sleep
from logging import PercentStyle
from math import perm
from pickle import PERSID
r=[]
r1=[]
info=[]
info2=[]
lisfina=[]
def limpiar_terminal():#limpia la terminarl
    print (chr(27) + "[2J")

def agregar_cursos():#funcio de agregar curso
  per=[]
  per.append(input("Escriba el nombre del curso : "))
  per.append(input("Escriba los créditos del curso: "))
  per.append(input("Escriba las horas lectivas: "))
  per.append(input("Escriba la fecha de inicio: "))
  per.append(input("Escriba la fecha de finalización: "))
  per.append(input("Escriba el Horario de clases: "))
  per.append(input("Escriba las Carrera o carreras a la que pertenece: "))
  print("***************************************************************")
  print("Sus datos han sido guardados exitosamente")
  print("***************************************************************")
  return per
def seguir():#funcion para volver al menu principal
    if("S"==input('Decia regresar a el menu (S o N):').upper()):
        limpiar_terminal()
        menu_adminis()
    else:
        print("Hasta luego nos vemos")
def agregar_carreras():#funcion de Agregar carrera
    car=[]
    car.append(input("Escriba el nombre de la carrera que desea agregar: "))
    print("***************************************************************")
    print("Sus datos han sido guardados exitosamente")
    print("***************************************************************")
    return car
def consultar_curso():#funcio de consultar los cursos agregadas
    for per in info:
        print("------------------------")
        print("Nombre de curso: ", per[0])
        print("créditos del curso: ",per[1])
        print("horas lectivas: ",per[2])
        print("fecha de inicio: ",per[3])
        print("fecha de finalización: ",per[4])
        print("Horario de clases: ",per[5])
        print("carreras a la que pertenece: ",per[6])
        print("------------------------")
        sleep(2)
def consultar_carera():#funcio de consultar los carrera agregadas
    for car in info2:
        print("------------------------")
        print("Nombre de la carrera: ", car[0])
        print("------------------------")
        sleep(3)
def motificar_curso():#funcion de modificar los cursos agregados
    if ("S"==input('Quiere motificar algun dato (S o N):').upper()):
          posicion=input("ingrese la posicion en la que se encuentra su curso:")
          if  posicion=="1":
               info[0]=agregar_cursos()
          if posicion=="2":
               info[0]=agregar_cursos()
          if posicion=="3":
            info[0]=agregar_cursos()
          if posicion=="4":
            info[0]=agregar_cursos()
          if posicion=="5":
            info[0]=agregar_cursos()
          if posicion=="6":
            info[0]=agregar_cursos()
          if posicion=="7":
            info[0]=agregar_cursos()
          if posicion=="8":
            info[0]=agregar_cursos()
          if posicion=="9":
            info[0]=agregar_cursos()
          if posicion=="10":
            info[0]=agregar_cursos()
def motificar_carera():#funcion de modificar los carrera agregados
    if ("S"==input('Quiere motificar alguna carrera (S o N):').upper()):
        posicion=input("ingrese la posicion en la que se encuentra su curso:")
        if posicion=="1":
            info2[0]=agregar_carreras()
        if posicion=="2":
            info2[1]=agregar_carreras()
        if posicion=="3":
            info2[3]=agregar_carreras()
        if posicion=="4":
            info2[4]=agregar_carreras()
        if posicion=="5":
            info2[5]=agregar_carreras()
        if posicion=="6":
            info2[6]=agregar_carreras()
        if posicion=="7":
            info2[7]=agregar_carreras()
        if posicion=="8":
            info2[8]=agregar_carreras()
        if posicion=="9":
            info2[9]=agregar_carreras()
        if posicion=="10":
            info2[10]=agregar_carreras()
def transformar():#funcion que nombla variable como global en ves de locales
    #pasa una lista con sublistas a una sola lista
  global r
  for item in info:
     r+=item
  global r1
  for item in info2:
     r1+=item

def menu_adminis():#el menu principal del administracion
     print("*********************************************")
     print("** Bienvenido a tu administrador de tiempo **")
     print("*********************************************")
     print("(1).Agregar cursos---------------------------")
     print("(2).Consultar y modificar cursos-------------")
     print("(3).Agregar carreras-------------------------")
     print("(4).Consultar y modificar carreras-----------")
     print("(5).Salir------------------------------------")
     print("*********************************************")
     opt=input("Ingrese su opción:  ")
     if opt=="1":#se direge a las diferentes funciones
         info.append(agregar_cursos())
         seguir()
     if opt=="2":#se direge a las diferentes funciones
           consultar_curso()
           motificar_curso()
           seguir()   
           
     if opt=="3":#se direge a las diferentes funciones
            info2.append(agregar_carreras())
            seguir()
            menu_adminis()
     if opt=="4":#se direge a las diferentes funciones
          consultar_carera()
          motificar_carera()
          seguir()
     if opt=="5":#se direge a las diferentes funciones
              limpiar_terminal()
              if("S"==input('Decia regresar a el login (S o N):').upper()):
                  lisfina.append(transformar())
                  from login import login
                  login()
              else:
                print("Hasta luego nos vemos")
