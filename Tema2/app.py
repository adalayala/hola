from flask import Flask, render_template, request, redirect, url_for

# --- CONFIGURACIÓN DE LA APLICACIÓN ---
app = Flask(__name__)

# Datos estáticos de los lotes de ganado para el Dashboard
LOTES_GANADO = [
    {"nombre": "Ternero", "cantidad": 50, "precio": "Consultar", "detalle": "Lotes de terneros machos y hembras, peso promedio 180kg.", "imagen": "ternero.jpg"},
    {"nombre": "Novillito", "cantidad": 80, "precio": "$850/cabeza", "detalle": "Novillitos de 24 meses, listos para engorde. Sanidad al día.", "imagen": "novillito.jpg"},
    {"nombre": "Novillo", "cantidad": 30, "precio": "$1200/cabeza", "detalle": "Novillos terminados, peso promedio 480kg. Excelente genética.", "imagen": "novillo.jpg"},
    {"nombre": "Vaquillona", "cantidad": 65, "precio": "$750/cabeza", "detalle": "Vaquillonas preñadas (garantía de preñez), edad 30 meses.", "imagen": "vaquillona.jpg"},
    {"nombre": "Vaca", "cantidad": 40, "precio": "$900/cabeza", "detalle": "Vacas de descarte y vacas con cría al pie. Buen estado corporal.", "imagen": "vaca.jpg"},
    {"nombre": "Toro", "cantidad": 15, "precio": "$2500/cabeza", "detalle": "Toros reproductores puros de pedigree (PP). Variedad de razas.", "imagen": "toro.jpg"},
]

# --- RUTAS DE LA APLICACIÓN ---

# 1. Ruta principal (Dashboard)
# Requisito: Al colocar la IP debe abrir directo el dashboard.
@app.route('/')
def index():
    """Muestra la página principal con los lotes."""
    return render_template('dashboard.html', lotes=LOTES_GANADO)

# 2. Ruta para manejar el formulario de contacto (Opción de pedir mas info.)
@app.route('/contacto', methods=['POST'])
def contacto():
    """Simula el procesamiento del formulario (ya no guarda en DB)."""
    if request.method == 'POST':
    
        return redirect(url_for('index', success='true'))

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)