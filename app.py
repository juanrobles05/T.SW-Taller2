from flask import Flask, render_template, jsonify
import json
import random
import socket
import os
from models.pokenea import pokeneas_data

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def get_container_id():
    """Obtiene el ID del contenedor"""
    try:
        # En Docker, el hostname es el container ID
        container_id = socket.gethostname()
        return container_id[:12]  # Limitamos a 12 caracteres como Docker
    except:
        return "local-dev"

@app.route('/api/pokenea')
def get_random_pokenea_api():
    """Ruta que devuelve un JSON con id, nombre, altura y habilidad de un Pokenea aleatorio"""
    random_pokenea = random.choice(pokeneas_data)

    response_data = {
        "id": random_pokenea["id"],
        "nombre": random_pokenea["nombre"],
        "altura": random_pokenea["altura"],
        "habilidad": random_pokenea["habilidad"],
        "container_id": get_container_id()
    }

    # Return pretty JSON with UTF-8 characters unescaped so accents/ñ appear correctly
    return app.response_class(
        json.dumps(response_data, ensure_ascii=False, indent=2),
        mimetype='application/json; charset=utf-8'
    )

@app.route('/')
def show_random_pokenea():
    """Ruta que muestra la imagen y frase filosófica de un Pokenea aleatorio"""
    random_pokenea = random.choice(pokeneas_data)
    container_id = get_container_id()

    return render_template('pokenea.html',
                         pokenea=random_pokenea,
                         container_id=container_id)

@app.route('/health')
def health_check():
    """Endpoint de verificación de salud"""
    payload = {"status": "healthy", "container_id": get_container_id()}
    return app.response_class(
        json.dumps(payload, ensure_ascii=False, indent=2),
        mimetype='application/json; charset=utf-8'
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
