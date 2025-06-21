turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
                  "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
      "012": ["Julian Martinez", "Argentina", "19-09-2023"],
      "014": ["Agustin Morales", "Argentina", "28-03-2024"],
                  "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
      "006": ["Maria Lopez", "Mexico", "08-12-2023"],
      "007": ["Joao Silva", "Brasil", "20-06-2024"],
	      "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	      "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
                  "008": ["Ana Santos", "Brasil", "03-10-2023"],
      "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
      "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
     }

def turistas_por_pais(pais):
    encontrados=[]
    for datos in turistas.values():
        if datos[1].lower() == pais.lower():
            encontrados.append(datos[0])

    if len(encontrados) == 0:
        print("No hay turistas de ese pais")
    else:
        print(encontrados)

def turistas_por_mes(mes):
    while mes < 1 or mes > 12:
        print("Debe ingresar un valor entre 1 y 12, intentelo nuevamente")
        try:
            mes = int(input("Ingrese el mes a buscar: "))
        except:
            mes = -1
            continue

    total = len(turistas)
    contador = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            contador += 1


    porcentaje = (contador / total) * 100
    return round(porcentaje, 1)


def eliminar_turista():
    nombre=input("Ingrese el nombre del turista que desea elimminar: ").lower()
    encontrado = False

    for clave in list(turistas.keys()):
        if turistas[clave][0].lower() == nombre:
            del turistas[clave]
            encontrado = True
            print("Turista eliminado con exito")
            break

    if not encontrado:
        print("El turista no se puede eliminar por que no ha sido encontrado")


def main():
    while True:
        print("\n***MENU PRINCIPAL***")
        print("1.- Turistas por país")
        print("2.- Turistas por mes")
        print("3.- Eliminar turista")
        print("4.- Salir")


        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            pais = input("\nIngrese pais a buscar: ")
            turistas_por_pais(pais)


        elif opcion == "2":
            try:
                mes = int(input("\nIngrese el mes a buscar: "))
            except:
                mes = -1
            porcentaje = turistas_por_mes(mes)
            print(f"El numero de turistas equivale al {porcentaje}% del total")

        elif opcion == "3":
            eliminar_turista()

        elif opcion == "4":
            print("Programa terminando.....")
            break

        else:
            print("Opcion no valida!")

main()
