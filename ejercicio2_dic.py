#2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
#necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es
#verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
#hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
#esa planta a la lista de diccionarios.

def agregar_plantas(lista_plantas):
    especie = input("Ingrese la especie de la planta o * para terminar: ")
    while especie != "*":   
        necesita_luz_solar_input = input("La planta necesita luz solar? si o no ").lower()
        necesita_luz_solar = necesita_luz_solar_input == "si"
        while necesita_luz_solar_input not in ["si", "no"]:
            print("Por favor, responda con 'si' o 'No'.")
            necesita_luz_solar_input = input("La planta necesita luz solar? si o no ").lower()
            necesita_luz_solar = necesita_luz_solar_input == "si"
        
        precio = float(input("Ingrese el precio de la planta: "))
        nueva_planta = {
            "nombre": especie,
            "necesita_luz_solar": necesita_luz_solar,
            "precio": precio}        
        especie = input("Ingrese la especie de la planta o * para terminar: ")
        lista_plantas.append(nueva_planta)                     
    return lista_plantas
lista_plantas = []
lista_plantas_actualizada = agregar_plantas(lista_plantas)
print("Lista de plantas actualizada:",lista_plantas_actualizada)



