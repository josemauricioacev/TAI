from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "supersecreto"

FASTAPI_URL = "http://127.0.0.1:5001"

# Ruta de inicio con formulario de registro
@app.route('/')
def home():
    return render_template('registro.html')

# Ruta para registrar usuario en FastAPI
@app.route('/usuariosFastAPI', methods=['POST'])
def post_usuario():
    usuarioNuevo = {
        "name": request.form['txtNombre'],
        "age": int(request.form['txtEdad']),
        "email": request.form['txtCorreo']
    }
    try:
        response = requests.post(f"{FASTAPI_URL}/usuarios/", json=usuarioNuevo)
        if response.status_code in [200, 201]:
            flash("Usuario guardado correctamente", "success")
        else:
            flash("Error al guardar usuario", "danger")
    except Exception as e:
        flash(f"Error de conexión: {e}", "danger")
    return redirect(url_for('home'))

# Ruta para mostrar la tabla de usuarios
@app.route('/Consultalsuarios')
def get_usuarios():
    try:
        response = requests.get(f"{FASTAPI_URL}/todosUsuarios/")
        response.raise_for_status()
        usuarios = response.json()
        return render_template('consulta.html', usuarios=usuarios)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta única para actualizar o eliminar según el botón presionado
@app.route('/accion/<int:id>', methods=['POST'])
def accion_usuario(id):
    accion = request.form.get('accion')

    if accion == 'eliminar':
        try:
            response = requests.delete(f"{FASTAPI_URL}/usuarios/{id}")
            if response.status_code == 200:
                flash("Usuario eliminado correctamente", "success")
            else:
                flash("Error al eliminar usuario", "danger")
        except Exception as e:
            flash(f"Error de conexión: {e}", "danger")

    elif accion == 'actualizar':
        data_actualizada = {
            "name": request.form['name'],
            "age": int(request.form['age']),
            "email": request.form['email']
        }
        try:
            response = requests.put(f"{FASTAPI_URL}/usuarios/{id}", json=data_actualizada)
            if response.status_code == 200:
                flash("Usuario actualizado correctamente", "success")
            else:
                flash("Error al actualizar usuario", "danger")
        except Exception as e:
            flash(f"Error de conexión: {e}", "danger")

    return redirect(url_for('get_usuarios'))

if __name__ == '__main__':
    app.run(debug=True, port=8002)
