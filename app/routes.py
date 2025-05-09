from .pokeneas import get_pokeneas
import random, socket
from flask import Blueprint, jsonify, render_template

main = Blueprint('main', __name__)

pokeneas = get_pokeneas()

#Funcion para obtener el ID del contenedor
def get_container_id():
    try:
        container_id = socket.gethostname()
    except Exception as e:
        container_id = "Unknown"
    return container_id

#Ruta 1
@main.route('/')
def pokenea_json():
    p = random.choice(pokeneas)
    return jsonify(p)

#Ruta 2
@main.route('/pokenea-view')
def pokenea_view():
    p = random.choice(pokeneas)
    container_id = get_container_id()
    return render_template('pokenea_view.html', pokenea=p, container_id=container_id)

