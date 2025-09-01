# Entrada
nombre =input('Ingerse su nombre: ')
edad = int(input('Ingrese su edad: '))
cant_atracciones = int(input('''
Cuántas atracciones quiere usar? 
El parque tiene solo 3 atracciones
=> '''))


# Proceso -- Uso de ciclos


contador = 0
acumulador = 0
atraccion_elegida = ""

while contador < cant_atracciones:
        
        atraccion = input('''
Cual atraccion desea usar? 
(Montaña Rusa/Casa del Terror/Carrusel): ''').lower()

    # Uso de condicionales
        match atraccion:
            case 'montaña rusa':
                if edad >= 12:  # Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más).
                        print('Puede subirse!')
                        contador += 1
                        acumulador += 1500
                        atraccion_elegida += '-Montaña rusa ✅\n'
                else:
                    atraccion_elegida += '-Montaña rusa ❌\n'
                    continue
            case 'casa del terror':
                if edad >= 6:    # Pueden acceder a todas las atracciones. (Entre 6 y 11 años, la minima de montaña rusa es 12 años)
                    contador += 1
                    atraccion_elegida += '-Casa del terror ✅\n'
                    acumulador += 1200
                else:
                    atraccion_elegida += '-Casa del terror ❌\n'
                    continue
            case 'carrusel':   # Si el visitante tiene menos de 6 años, solo puede subir al Carrusel.
                contador += 1        
                atraccion_elegida += 'Carrusel ✅\n'   
                acumulador += 800
    
    
print("\n--- RESUMEN ---")
print(f"Visitante: {nombre}")
print(f"Edad: {edad} años")
print("Atracciones elegidas:")
print(atraccion_elegida)
print(f"COSTO TOTAL A PAGAR: ${acumulador}")
