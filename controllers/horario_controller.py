from flask import Blueprint, request,jsonify
from models import db
import cv2
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity,create_access_token
from models.horario import Horario
from werkzeug.security import check_password_hash,generate_password_hash
import face_recognition
import base64
import numpy as np
from io import BytesIO
from PIL import Image

horario_bp=Blueprint('horario_bp', __name__)

@horario_bp.route('/nuevo_horario',methods=['POST'])
def add_horario():
    data = request.get_json()
    idUser = data.get('idUsuario')
    start = data.get('hora_inicio')
    end = data.get('hora_fin')

    # if not idUser or not fecha or not minTarde or not estFalta:
    #     return jsonify({"error": "Faltan datos en la solicitud"}), 400

    nuevo_horario = Horario(
        idUsuario = idUser,
        hora_inicio = start,
        hora_fin = end
    )
    db.session.add(nuevo_horario)
    db.session.commit()

    return jsonify({'message': 'Horario creado exitosamente'}), 201