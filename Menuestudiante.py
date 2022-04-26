from distutils.command.check import _Reporter
from math import dist
from time import sleep
from menuadministrador import r,r1,info
clave={"Nombre de curso: ", "créditos del curso: ","horas lectivas: ","fecha de inicio: ",
        "fecha de finalización: ","Horario de clases: ","carreras a la que pertenece: "}
matri=()
cu=[]
agre=[]
def limpiar_terminal():
    print (chr(27) + "[2J")
def menu_estu():#el menu principal del Estudiante
    print("*********************************************")
    print("** Bienvenido a tu administrador de tiempo **")
    print("*********************************************")
    print("(1).Cambio de Carrera------------------------")
    print("(2).Matricular cursus------------------------")
    print("(3).Marcar como aprovado un curso------------")
    print("(4).Agreegar Actividades---------------------")
    print("(5).Reportes---------------------------------")
    print("(6).Salir------------------------------------")
    opti=input("Ingrese su opción:  ")
    if opti=="1":#se direge a las diferentes funciones
           cambio_carrera()
           input("Se hanguadado corectamente los registros, presione enter para volver al menu ")
           limpiar_terminal()
           menu_estu()
    if opti=="2":#se direge a las diferentes funciones
           cu.append(matricula())
           input("Se hanguadado corectamente los registros, presione enter para volver al menu ")
           limpiar_terminal()
           menu_estu()
    if opti=="3":#se direge a las diferentes funciones
        input("Se hanguadado corectamente los registros, presione enter para volver al menu ")
        limpiar_terminal()
        menu_estu()
    if opti=="4":#se direge a las diferentes funciones
        Agregar_actividades()
        input("Se hanguadado corectamente los registros, presione enter para volver al menu ")
        limpiar_terminal()
        menu_estu()
    if opti=="5":#se direge a las diferentes funciones
        reportes()
        input("Se hanguadado corectamente los registros, presione enter para volver al menu ")
        limpiar_terminal()
        menu_estu()
    if opti=="6":#se direge a las diferentes funciones
        limpiar_terminal()
        if("S"==input('Decia regresar a el login (S o N):').upper()):
                from login import login
                login()
        else:
           limpiar_terminal()
           print("Hasta luego nos vemos")
def cambio_carrera():# funcion de cambiar de carrera
    for x in r1:
        print("------------------------")
        print("Nombre de las carrera disponlibles para cambiar: ", x)
        print("------------------------")
        sleep(2)
    posicion=input("ingrese la posicion en la que se encuentra carrera que decia cambiar:")
    global c
    c=[]
    if  posicion=="1":
        print("Su Careras es:",r1[0])
        c.append(r1[0])
    if posicion=="2":
        print("Su Careras es:",r1[1])
        c.append(r1[1])
    if posicion=="3":
        print("Su Careras es:",r1[2])
        c.append(r1[2])
    if posicion=="4":
        print("Su Careras es:",r1[3])
        c.append(r1[3])
    if posicion=="5":
        print("Su Careras es:",r1[4])
        c.append(r1[4])
def matricula():# funcion de matricular los cursos por su carrera
    global curso_carrera
    curso_carrera=[]
    for re in info:
            if type(re) is list: #Bucar elementos dentro de un sublista
              for x in c:
                for y in re:
                  if y==x:
                      curso_carrera.append(re)
    for m in curso_carrera:
          print("Estos son los cursoso disponibre a matricular")
          print("------------------------")
          print("Nombre de curso: ", m[0])
          print("créditos del curso: ",m[1])
          print("horas lectivas: ",m[2])
          print("fecha de inicio: ",m[3])
          print("fecha de finalización: ",m[4])
          print("Horario de clases: ",m[5])
          print("carreras a la que pertenece: ",m[6])
          print("------------------------")
          if ("S"==input('Desea matricular este curso (S o N):').upper()):
              print("-------------------------------------")
              print("El curso fue matriculado exitosamente")
              return m
def Marcar_apo():#funcion de marcar los cursos aprovados
    for y in cu:#Saca las fechas de finalisacion de los cursus matriculasdos
      ff=(y[4])
    for a in cu:#imprime todos los cursos matriculados
        if type(a) is list: #Bucar elementos dentro de un sublista
              for z in a:
               print("------------------------")
               print("Nombre de curso: ", z[0])
               print("créditos del curso: ",z[1])
               print("horas lectivas: ",z[2])
               print("fecha de inicio: ",z[3])
               print("fecha de finalización: ",z[4])
               print("Horario de clases: ",z[5])
               print("carreras a la que pertenece: ",z[6])
               print("------------------------")
               sleep(2)
               if ("S"==input('Ya paso la fecha definalización (S o N):').upper()):
                   cu.remove(a)
def Agregar_actividades():# menu de las diferendes funciones de las actividades
    print("*********************************************")
    print("***** Bienvenido a agregar actividades ******")
    print("*********************************************")
    print("(1).Agregar activiadesde---------------------")
    print("(2).Consultar actividades--------------------")
    print("(3).Salir------------------------------------")
    opti=input("Ingrese su opción:  ")
    if opti=="1":
        a=[]
        agre.append(agregar_acti())
    if opti=="2":
        Clases()
        consulta_activi()
    if opti=="3":
        if("S"==input('Decia regresar a el menu de Administracio (S o N):').upper()):
          limpiar_terminal()
          Agregar_actividades()
    def Clases():#saca los horario y horas lectivos de los cursos matriculados
     for x in cu:
       global horalec
       global hora
       horalec=(x[5])
       hora=(x[2])
    def agregar_acti():#funcion de agregar adtividades
     agre=[]
     agre.append(input("Descricion de la actividad"))
     agre.append(input("Curso asociado a la actividad"))
     agre.append(input("Horas de duracion de la actividad"))
     agre.append(input("Fecha de inicio de la actividade"))
     agre.append(input("Fecha de conclusión de la actividade"))
     return agre
    def consulta_activi():#funcion de consultar las actividades agregadas y las clases
        print("------------------------")
        print("---------Clases---------")
        print("------------------------")
        print("Horas de duracion de clase",hora )
        print("Horarios de clase",horalec )
        for o in agre:
         print("------------------------")
         print("-------Actividades------")
         print("------------------------")
         print("Descricion: ", o[0])
         print("curso asociado: ", o[1])
         print("Horas de duracion: ", o[2])
         print("Fecha de inicio: ", o[3])
         print("Fecha de conclusion: ", o[4])
         print("------------------------")
         sleep(3)
        if ("S"==input('Quiere marcarlas como ejecutada la actividad (S o N):').upper()):
           print("La actividad fue marcada como ejecutada")
           global marca
           marca=[]
           marca.append(o)
def reportes():#funciones de los diferentes reportes
    print("***************************************************")
    print("************* Bienvenido a Reportes ***************")
    print("***************************************************")
    print("(1).Reporte de actividades diario -----------------")
    print("(2).Porcentaje de tiempo ejecutado en actividades--")
    print("(3).tiempo disponible -----------------------------")
    print("(4).Salir------------------------------------------")
    opt3=input("Ingrese su opción:  ")
    if opt3=="1":
        fecha=input("Por Favor digite la fecha actual")
        for ree in agre:#Se sacan la fecha de inicio de las actividades y se comparar con la actual
         global he
         he=[]
         horaact=(ree[3])
         if horaact==fecha:
             he.append(ree)
        for v in cu:#se sacan la fecha de las clases y se comparar con la actual
            global hj
            hj=[]
            fc=(v[3])
            if fc==fecha:
                hj.append(v)
        for re in agre:#horas de duracion
         global ho
         ho=[]
         horaact=(re[2])
         ho.append(horaact)
        for d in he:#Se imprimen las actividades y clases del dia
            nombre=d[0]
            if nombre=="actividades extraclase":# se imprimen si hay a actividades llamadas extraclase
               print("------------------------")
               print("-------Actividades------")
               print("------------------------")
               print('\033[92m'+"Horas de duracion: ", d[2]+'\033[0m')#se imprimen de color Verde
               print('\033[92m'+"curso asociado: ", d[1]+'\033[0m')#se imprimen de color Verde
               print('\033[92m'+"La Carrera vinculada",c+'\033[0m')#se imprimen de color Verde
               print("------------------------")
               horasdia.append(d[2])
               sleep(3)
            if nombre=="actividades de ocio":# se imprimen las hactividades de actividad de ocio
               print("------------------------")
               print("-------Actividades------")
               print("------------------------")
               print('\033[93m'+"Horas de duracion: ", d[2]+'\033[0m')#se imprimen de color amarillo
               print('\033[93m'+"curso asociado: ", d[1]+'\033[0m')#se imprimen de color amarillo
               print('\033[93m'+"La Carrera vinculada",c+'\033[0m')#se imprimen de color amarillo
               print("------------------------")
               sleep(3)
               horasdia.append(d[2])
            print("------------------------")
            print("-------Actividades------")
            print("------------------------")
            print("Horas de duracion: ", d[2])
            print("curso asociado: ", d[1])
            print("La Carrera vinculada",c)
            print("------------------------")
            horasdia.append(d[2])
            sleep(3)
        for w in hj:
            print("------------------------")
            print("---------Clases---------")
            print("------------------------")
            print('\033[91m'+"Horas de duracion de clase",w[2]+'\033[0m' )#se imprimen de color rojo
            print('\033[91m'+"Horarios de clase",w[5]+'\033[0m' )#se imprimen de color rojo
            horasdia.append(w[2])
    if opt3=="2":# se saca el prsentaje de eficiencia del estudiante
        cont=0
        for q in marca:
            cont=cont+1
        print("Las activiades realisadas son",cont)
        cont2=0
        for t in horasdia:
            cont2=cont+1
        print("Las activiades que tenia de realuasr son",cont2)
        def resultado():
         fin=cont//cont2
         res=fin*10
         print("El porsentaje de eficiencia es:",res)
    if opt3=="3":# cantidad de tiempo que le queda en el dia.
        global horasdia
        horasdia=[]
        listhoras=sum(horasdia)
        lis=12-listhoras
        print["Las horas de tiene disponible son",lis]
    if opt3=="4":
        if("S"==input('Decia regresar a el menu de reportes (S o N):').upper()):
            limpiar_terminal()
            reportes()



