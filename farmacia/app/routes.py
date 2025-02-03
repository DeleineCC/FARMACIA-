from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask import current_app as app
from flask import abort
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

main = Blueprint('main', __name__)

PREDEFINED_USERNAME = "admin"
PREDEFINED_PASSWORD = "admin123"

# Función para verificar autenticación
def check_authentication():
    if 'user' not in session:
        abort(401)  # Genera el error 401 si el usuario no está autenticado

# Ruta principal
@main.route('/')
def index():
    return render_template('index.html')

# Ruta para login
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
            session['user'] = username  # Usamos session para almacenar información de usuario
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

# Ruta de home
@main.route('/home')
def home():
    return render_template('home.html')

# Ruta para productos (protegida)
@main.route('/productos')
def productos():
    # Verificar autenticación antes de mostrar el contenido
    check_authentication()
    return render_template('productos.html')

# Manejo de error 404
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Manejo de error 401
@main.app_errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401
