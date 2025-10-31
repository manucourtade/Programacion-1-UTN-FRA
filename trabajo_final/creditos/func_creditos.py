datos = {
    'autores': ('Manuel Courtade', 'Maximo Savall'),
    'fecha': '31/10/2025',
    'materia': 'Programacion I',
    'docentes': ('Martin Alejandro Garcia', 'Veronica'),
    'carrera': 'Tecnicatura en programacion',
    'contacto': ('courtademanuel@outlook.es', 'savallmaximo@gmail.com')
}


def creditos(datos):
    print('#' * 40)
    print('\tMINI GENERALA TEMATICA')
    print('#' * 40)
    
    print(f"\nAutor/es: {datos['autores'][0]} y {datos['autores'][1]}")
    print(f"Fecha: {datos['fecha']}")
    print(f"Materia: {datos['materia']}")
    print(f"Docentes: {datos['docentes'][0]} y {datos['docentes'][1]}")
    print(f"Carrera: {datos['carrera']}")
    print(f"Contacto: {datos['contacto'][0]} - {datos['contacto'][1]}\n")
    print('#' * 50)




