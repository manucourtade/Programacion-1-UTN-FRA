def dados_invalidos(seleccion):
    if seleccion.isdigit():                
        seleccion = int(seleccion)
        return 1 <= seleccion <= 5         
    else:
        return False                    
