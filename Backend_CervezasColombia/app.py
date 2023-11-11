from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}) # Habilita CORS para rutas que comiencen con "/api"

# Configura la codificación para JSON
app.config['JSON_AS_ASCII'] = False

# Ruta para obtener el resumen
@app.route('/api/Resumen', methods=['GET'])
def obtener_resumen():
    try:
        conn = sqlite3.connect('CervezasColombia.sqlite', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        # Consultas para obtener el número de registros en las tablas
        cursor.execute("SELECT COUNT(*) FROM ubicaciones")
        ubicaciones_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM cervecerias")
        cervecerias_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM cervezas")
        cervezas_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM estilos")
        estilos_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM envasados")
        envasados_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM ingredientes")
        ingredientes_count = cursor.fetchone()[0]

        # Crear un diccionario con los totales
        resumen = {
            "ubicaciones": ubicaciones_count,
            "cervecerias": cervecerias_count,
            "cervezas": cervezas_count,
            "estilos": estilos_count,
            "envasados": envasados_count,
            "ingredientes": ingredientes_count
        }

        conn.close()

        return jsonify(resumen)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los registros de la vista "v_info_cervezas"
@app.route('/api/cervezas', methods=['GET'])
def obtener_cervezas():
    try:
        conn = sqlite3.connect('CervezasColombia.sqlite', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM v_info_cervezas")
        columnas = [description[0] for description in cursor.description]
        filas = cursor.fetchall()

        data = []
        for fila in filas:
            # Forzar la codificación de caracteres a UTF-8
            data.append({col: str(val).encode('utf-8').decode('utf-8') for col, val in zip(columnas, fila)})

        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los registros de la vista "v_info_cervecerias"
@app.route('/api/cervecerias', methods=['GET'])
def obtener_cervecerias():
    try:
        conn = sqlite3.connect('CervezasColombia.sqlite', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM v_info_cervecerias")
        columnas = [description[0] for description in cursor.description]
        filas = cursor.fetchall()

        data = []
        for fila in filas:
            # Forzar la codificación de caracteres a UTF-8
            data.append({col: str(val).encode('utf-8').decode('utf-8') for col, val in zip(columnas, fila)})

        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los registros de la vista "v_info_ingredientes"
@app.route('/api/ingredientes', methods=['GET'])
def obtener_ingredientes():
    try:
        conn = sqlite3.connect('CervezasColombia.sqlite', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM v_info_ingredientes")
        columnas = [description[0] for description in cursor.description]
        filas = cursor.fetchall()

        data = []
        for fila in filas:
            # Forzar la codificación de caracteres a UTF-8
            data.append({col: str(val).encode('utf-8').decode('utf-8') for col, val in zip(columnas, fila)})

        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los registros de la tabla "estilos"
@app.route('/api/estilos', methods=['GET'])
def obtener_estilos():
    try:
        conn = sqlite3.connect('CervezasColombia.sqlite', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM estilos")
        columnas = [description[0] for description in cursor.description]
        filas = cursor.fetchall()

        data = []
        for fila in filas:
            # Forzar la codificación de caracteres a UTF-8
            data.append({col: str(val).encode('utf-8').decode('utf-8') for col, val in zip(columnas, fila)})

        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los registros de la tabla "envasados"
@app.route('/api/envasados', methods=['GET'])
def obtener_envasados():
    try:
        conn = sqlite3.connect('CervezasColombia.sqlite', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM envasados")
        columnas = [description[0] for description in cursor.description]
        filas = cursor.fetchall()

        data = []
        for fila in filas:
            # Forzar la codificación de caracteres a UTF-8
            data.append({col: str(val).encode('utf-8').decode('utf-8') for col, val in zip(columnas, fila)})

        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ruta para obtener todos los registros de la tabla "ubicaciones"
@app.route('/api/ubicaciones', methods=['GET'])
def obtener_ubicaciones():
    try:
        conn = sqlite3.connect('CervezasColombia.sqlite', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ubicaciones")
        columnas = [description[0] for description in cursor.description]
        filas = cursor.fetchall()

        data = []
        for fila in filas:
            # Forzar la codificación de caracteres a UTF-8
            data.append({col: str(val).encode('utf-8').decode('utf-8') for col, val in zip(columnas, fila)})

        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7024)
