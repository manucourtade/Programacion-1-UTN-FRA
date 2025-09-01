def mostrar_atraccion() -> str:    
    atraccion = input('''
    ¿Cuál atracción desea usar? 
    (Montaña rusa / Casa del terror / Carrusel): ''').lower()
    return atraccion


def puede_subir(edad:int, atraccion: str) -> bool:
    match atraccion:
        case "montaña rusa":
            return edad >= 12
        case "casa del terror":
            return edad >= 6
        case "carrusel":
            return True
    return False


def calcular_precio(atraccion: str) -> int:
    if atraccion == "montaña rusa":
        return 1500
    elif atraccion == "casa del terror":
        return 1200
    else:
        return 800


def calc_descuento(cant_atracciones: int, total: int) -> int:
    if cant_atracciones >= 3:
        return int(total * 0.9)  
    return total


def registrar_visita():
    nombre = input('Ingrese su nombre: ')
    edad = int(input('Ingrese su edad: '))
    atracciones_elegidas = ""   
    total = 0
    contador = 0                 

    while True:
        atraccion = mostrar_atraccion()

        if puede_subir(edad, atraccion):
            total += calcular_precio(atraccion)
            contador += 1
            if atracciones_elegidas == "":
                atracciones_elegidas = atraccion
            else:
                atracciones_elegidas += ", " + atraccion
            print(f"✅ {nombre} puede subir a {atraccion}")
        else:
            print(f"❌ {nombre} no cumple con la edad mínima para {atraccion}")
            
        seguir = input("¿Desea usar otra atracción? (si/no): ").lower()
        if seguir == "no":
            break

    monto_final = calc_descuento(contador, total)
    mostrar_resumen(nombre, atracciones_elegidas, monto_final)


def mostrar_resumen(nombre:str, atracciones_elegidas:str, monto_final:int):
    print("\n--- RESUMEN DE VISITA ---")
    print(f"Visitante: {nombre}")
    print("Atracciones elegidas:", atracciones_elegidas)
    print(f"COSTO TOTAL A PAGAR: ${monto_final}")

