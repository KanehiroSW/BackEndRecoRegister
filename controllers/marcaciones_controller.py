from flask import Blueprint, request,jsonify
from models import db
from datetime import datetime
import cv2
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity,create_access_token
from models.marcaciones import Marcacion
from werkzeug.security import check_password_hash,generate_password_hash
import face_recognition
import base64
import numpy as np
from io import BytesIO
from PIL import Image

marcaciones_bp=Blueprint('marcaciones_bp', __name__)

@marcaciones_bp.route('/nueva_marca',methods=['POST'])
def add_marca():
    data = request.get_json()
    idUser = data.get('idUsuario')
    fecha = datetime.now()
    minTarde = data.get('min_tarde')
    estFalta = data.get('est_falta')

    # if not idUser or not fecha or not minTarde or not estFalta:
    #     return jsonify({"error": "Faltan datos en la solicitud"}), 400

    nueva_marcacion = Marcacion(
        idUsuario = idUser,
        fecha = fecha,
        min_tarde = minTarde,
        est_falta = estFalta
    )
    db.session.add(nueva_marcacion)
    db.session.commit()

    return jsonify({'message': 'Nueva marcación exitosa'}), 201

