from funciones import *
vec_titulos = [''] * 20
vec_ejemplares = [0] * 20

def sistema_catalogo():
    while True:
        opcion = input(
            "\n1. Cargar títulos y ejemplares"
            "\n2. Mostrar catálogo completo"
            "\n3. Consultar disponibilidad"
            "\n4. Listar títulos agotados"
            "\n5. Agregar un nuevo título"
            "\n6. Actualizar ejemplares (préstamo / devolución)"
            "\n7. Salir"
            "\n=> "
        )

        if opcion == '1':
            cargar_tit_ej(vec_titulos, vec_ejemplares)
            print("Se cargaron los títulos y ejemplares.")

        elif opcion == '2':
            mostrar_catalogo(vec_titulos, vec_ejemplares)

        elif opcion == '3':
            msg = consultar_disp(vec_titulos, vec_ejemplares)
            print(msg)

        elif opcion == '4':
            listar_agotados(vec_titulos, vec_ejemplares)

        elif opcion == '5':
            agregar_nuevo(vec_titulos, vec_ejemplares)
            print('Se agrego nuevos libros')

        elif opcion == '6':
            act_ejemplares(vec_titulos, vec_ejemplares)
            
        elif opcion == '7':
            print("Hasta luego, gracias!")
            break


sistema_catalogo()
