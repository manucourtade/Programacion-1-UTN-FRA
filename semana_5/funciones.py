

def cargar_tit_ej(titulos, ejemplares):
    for i in range(len(titulos)):
        titulos[i] = input(f'Ingresar el título {i + 1}: ')
        ejemplares[i] = int(input(f'Cantidad de ejemplares de "{titulos[i]}": '))
        salir = input('Quiere seguir agregando? (s/n) : ').lower()
        if salir == 'n':
            break
    return titulos, ejemplares

def mostrar_catalogo(titulos, ejemplares):
    for i in range(len(titulos)):
        if titulos[i]:  
            print(f'{titulos[i]} => {ejemplares[i]} copias')

def consultar_disp(titulos, ejemplares):
    buscar = input('Ingrese el título a buscar: ').lower()

    for i in range(len(titulos)):
        if buscar == titulos[i].lower():
            return f'"{titulos[i]}" tiene {ejemplares[i]} copias'
    
    return f'"{buscar}" no se encuentra en nuestro catálogo'


def listar_agotados(titulos, ejemplares):
    for i in range(len(titulos)):
        if titulos[i] and ejemplares[i] == 0:
            print(titulos[i])
        return 'Todos los libros tienen copias!'


def agregar_nuevo(titulos, ejemplares):
    for i in range(len(titulos)):
        if not titulos[i]:                     
            titulos[i] = input('Ingrese un nuevo título: ')
            ejemplares[i] = int(input(f'Ingrese la cantidad de ejemplares de "{titulos[i]}": '))
            return titulos, ejemplares     
    return '¡Ya se alcanzó el máximo de libros ingresados!'


def act_ejemplares(titulos, ejemplares):
    buscar = input('Ingrese el libro a actualizar: ').lower()
    
    for i in range(len(titulos)):
        if buscar == titulos[i].lower():
            ejemplares[i] = int(input(f'Ingrese la nueva cantidad de copias de "{titulos[i]}": '))
            return titulos, ejemplares  
        return 'No existe ese libro en nuestro catalogo!'

    return 'No existe el libro buscado'

        



