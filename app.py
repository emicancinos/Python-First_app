import os         #importo una libreria que me permite ejecutar comandos de linux o windows o cualquier sistema

os.system('cls')   
print ("")
print("┌────────────────────────────────────────────────────────┐ ")
print("|Bienvenido al sistema de historias clinicas del hospital|")
print("└────────────────────────────────────────────────────────┘")

running = True

database = list()

#*******************
#*  FUNCIONES      *
#*******************

def show_menu():
    print("")
    print("")
    print("\t\t ■  1-Cargar paciente")
    print("\t\t ■  2-Buscar paciente por nombre")
    print("\t\t ■  3-Listar paciente")
    print("\t\t ■  4-Salir")
    print("")
    print("")
    res= input("INGRESE UNA OPCIÓN->")
    os.system('cls')    #aca con el import os del line1 voy a limpiar la pantalla cada vez que el usuario elije una opcion del menu
    return res

def response_validate(r):
    validated= False
    num_res= 0      #tiene valor 0 el num_res porque sino, en caso de no ejecutarse, no va a tener un valor para return al final de la funcion

    if response.isdigit():                  #la respuesta tiene que ser un  numero tomado como texto
        num_res = int(response)                #aca transforma la respuesta en un entero
        if num_res >= 1 and num_res <=4:      
            msg = "Esta en rango"
            validated= True
        else:
            msg = "No esta en rango"
    else:
        msg = "Entrada incorrecta"

    return validated, num_res , msg      


#*******************
#* LOOP PRINCIPAL  *
#*******************
while running: 
    response = show_menu()             
    validated, num_res , msg = response_validate(response)  #a esta altura ya tenemos validado el dato
    if validated:
        if num_res == 1:
            name = input("Ingrese el nombre del paciente ->")
            history = input("Ingrese la historia clinica del paciente ->")
            paciente = {"nombre": name , "historia": history}
            database.append(paciente)       #aca estoy cargando el paciente a la lista de database
            print(database)

        elif num_res == 2:
            name = input("Ingrese el nombre del paciente->")
            
            finded = True
            for x in range (len(database)):              #con este for recorro las listas y diccionarios de
                
                if database[x]["nombre"].lower() == name.lower():
                    print("")
                    print("Paciente encontrado!")
                    print("PACIENTE ENONTRADO | HISTORIA CLINICA ->",database[x]["historia"])
                    
                else:
                    finded = False
            
            if not finded:
                print("Paciente no encontrado :(")

            
        
        elif num_res == 3:
            print("")
            print("┌──────────────────────────────┐ ")
            print("|     LISTADO DE PACIENTES     |")
            print("└──────────────────────────────┘")
            print("")
            for x in range (len(database)):
                print("Nombre -> :".rjust(10) ,database[x]["nombre"] , "\t\t Historia Clinica:".rjust(10) , database[x]["historia"] )

            print("FIN DE LISTA")

        elif num_res == 4:
            running = False

    else:
        print("Opcion incorrecta")
print("")
print("Aplicación finalizada")
print("")