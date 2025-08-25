# Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima
# un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función
def saludar(nombre: str) -> None:
    print(f'Hola! {nombre} buen día!')

usuario = input('Ingrese su nombre de usuario: ')
saludar(usuario)





