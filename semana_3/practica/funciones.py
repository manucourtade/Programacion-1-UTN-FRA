
def pedir_turno() -> str:
    nombre = input('Ingrese su nombre:')
    turno = input('Ingrese su turno d/n: ')
    return nombre, turno

def registrar_turno(nombre: str, turno: str):
    return f'Hola {nombre} ha seleccionado turno {turno}'

def pedir_pago():
    horas = int(input("Ingrese cantidad de hs trabajadas: "))
    turno = input("Ingrese turno trabajado (d/n)")
    return horas, turno    

def calc_pago(horas: int, turno: str) -> int:
    if turno == 'd':
        return horas * 100
    elif turno == 'n':
        return horas * 150
    else:
        return 0
    
def mensaje_agradecimiento(nombre: str) -> str:
    return f'Adios {nombre} muchas gracias por usar nuestro servicio!'