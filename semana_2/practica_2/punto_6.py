# Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
# cuántas horas y minutos sobran.
def convertir_minutos(minutos: int = 60) -> int:
    horas =  minutos // 60
    sobrantes = minutos % 60
    return horas, sobrantes

minutos = int(input('Ingrese la cantidad de minutos: '))
horas, sobrantes = convertir_minutos(minutos)
print(f'Tiempo: {horas} horas y {sobrantes} minutos')