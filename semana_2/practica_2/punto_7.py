# Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si
# es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la
# edad al usuario y mostrar un mensaje apropiado.
def verificar_acceso(edad: int) -> bool:
    if edad >= 18:
        return True
    else:
        return False
    
edad = int(input('Ingrese su edad: '))
es_mayor = verificar_acceso(edad)

if es_mayor:
    print("Usted es mayor de edad. Acceso permitido.")
else:
    print("Usted es menor de edad. Acceso denegado.")