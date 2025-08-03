from flask import Flask, render_template, request
from algoritmos_busqueda import busqueda_secuencial, busqueda_binaria

app = Flask(__name__)

# Datos simulados
estudiantes = [
    {"id": 1001, "nombre": "Ana"},
    {"id": 1002, "nombre": "Luis"},
    {"id": 1003, "nombre": "Carlos"},
    {"id": 1004, "nombre": "Sofía"},
    {"id": 1005, "nombre": "Mario"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_nombre', methods=['GET', 'POST'])
def buscar_nombre():
    clave = ""
    resultados = []
    search_attempted = False

    if request.method == 'POST':
        clave = request.form['nombre']
        resultados = busqueda_secuencial(estudiantes, clave, 'nombre')
        search_attempted = True
    else:  # GET request (carga inicial de la página)
        for i, estudiante in enumerate(estudiantes):
            resultados.append((i, estudiante, "Sin revisar"))
    
    return render_template('busqueda_secuencial.html', resultados=resultados, clave=clave, search_attempted=search_attempted)

@app.route('/buscar_id', methods=['GET', 'POST'])
def buscar_id():
    clave = ""
    resultados = []
    search_attempted = False
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['id'])
    
    if request.method == 'POST':
        try:
            clave = int(request.form['id'])
            resultados = busqueda_binaria(estudiantes_ordenados, clave, 'id')
            search_attempted = True
        except ValueError:
            clave = request.form['id']
            # Para entradas inválidas, mostramos la lista sin resultados de búsqueda
            for i, estudiante in enumerate(estudiantes_ordenados):
                resultados.append((i, estudiante, "No revisado"))
            search_attempted = False # No se consideró un intento de búsqueda válido
    else:  # GET request (carga inicial de la página)
        for i, estudiante in enumerate(estudiantes_ordenados):
            resultados.append((i, estudiante, "No revisado"))
    
    return render_template('busqueda_binaria.html', resultados=resultados, clave=clave, search_attempted=search_attempted)

if __name__ == '__main__':
    app.run(debug=True)