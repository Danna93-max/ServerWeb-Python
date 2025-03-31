### Imports ################################################## 
import os   #per neteja la pantalla
import json
#Variables ###################################################

#Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json" 
alumnes = []
id_counter = 1

### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
#   
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    #Netejem la pantalla
    os.system('cls')            
    
    #Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    
    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #i retornem l'opció escollida per l'usuari
    return input()

### Programa ################################################

#Fins a l'infinit (i més enllà)
while True:

    opcio = menu()
    
    #Executem una opció funció del que hagi escollit l'usuari
    match opcio:

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")
            

            #Introduiu el vostre codi per mostrar alumnes aquí
            def mostrar_alumnes():
                
                if not alumnes:
                    print("No hi ha alumnes registrats.")
                else:
                    for alumne in alumnes:
                        print(f"ID: {alumne['id']}, Nom: {alumne['nom']}, Cognom: {alumne['cognom']}")
                input()
    
        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per afegir un alumne aquí
            def afegir_alumne():
                global id_counter
    
                nom = input("Nom: ")
                cognom = input("Cognom: ")
                dia = int(input("Dia de naixement: "))
                mes = int(input("Mes de naixement: "))
                any = int(input("Any de naixement: "))
                email = input("Email: ")
                feina = input("Treballa? (si/no): ").lower() == "si"
                curs = input("Curs: ")
                
                alumnes.append({
                    "id": id_counter,
                    "nom": nom,
                    "cognom": cognom,
                    "data": {"dia": dia, "mes": mes, "any": any},
                    "email": email,
                    "feina": feina,
                    "curs": curs
                })
                id_counter += 1
                print("\nAlumne afegit correctament!")
                input()
    
        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per veure un alumne aquí
            def veure_alumne():
                id_alumne = int(input("ID de l'alumne: "))
                alumne = next((a for a in alumnes if a['id'] == id_alumne), None)
                if alumne:
                    print(json.dumps(alumne, indent=4))
                else:
                    print("Alumne no trobat.")
                input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")
          
            #Introduiu el vostre codi per esborrar un alumne aquí
            def esborrar_alumne():
                global alumnes
                id_alumne = int(input("ID de l'alumne a esborrar: "))
                alumnes = [a for a in alumnes if a['id'] != id_alumne]
  
            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per desar a fitxer aquí
            def desar_a_fitxer():
                with open(nom_fitxer, "w") as f:
                    json.dump(alumnes, f, indent=4)
            
            input()

        # Llegir fitxer ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per llegir de fitxer aquí
            def llegir_fitxer():
                global alumnes, id_counter
                try:
                    with open(nom_fitxer, "r") as f:
                        alumnes = json.load(f)
                        if alumnes:
                            id_counter = max(a['id'] for a in alumnes) + 1
                except FileNotFoundError:
                    print("Fitxer no trobat.")

            input()

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Trenquem el bucle infinit
            break

        #Qualsevol altra cosa #####################   
        case _:
            print("\nOpció incorrecta\a")            
            input()

