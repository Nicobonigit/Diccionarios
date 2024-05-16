#1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
#mejor organizado sus datos.
#a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
#características que se consideren más relevantes para identificar a una persona (su nombre, DNI, edad, etc).
#b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso del
#estudiante y sus características (año, división, orientación, etc).
#c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad e
#imprimirla por pantalla.

escuela={}
maxima_edad = 0
estudiante_mayor_edad = ""
print("Ingresa a una persona o * para finalizar")
dni=input("Ingresa su dni: ")
while dni != "*":
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    edad=int(input("Ingrese su edad: "))
    while edad not in range (18,100):
        edad=input("Ingrese su edad: ")
    curso = {}
    curso['año'] = input("Ingrese el año del curso: ")
    curso['división'] = input("Ingrese la división del curso: ")
    curso['orientación'] = input("Ingrese la orientación del curso: ")
    escuela[dni] = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'curso': curso}
    dni = input("Ingrese su dni: ")

print("Lista completa de estudiantes")
for dni, datos in escuela.items():
    print("DNI:", dni)
    print("Nombre:", datos['nombre'])
    print("Apellido:", datos['apellido'])
    print("Edad:", datos['edad'])
    print("Curso:", datos['curso'])
    print("////////////////////////////")

print("Estudiante con la mayor edad")
for dni, datos in escuela.items():    
    if datos['edad'] > maxima_edad:        
        maxima_edad = datos['edad']
        estudiante_mayor_edad = datos
        
print("DNI:", dni)
print("Nombre:", estudiante_mayor_edad['nombre'])
print("Apellido:", estudiante_mayor_edad['apellido'])
print("Edad:", estudiante_mayor_edad['edad'])
print("Curso:", estudiante_mayor_edad['curso'])



    
  

