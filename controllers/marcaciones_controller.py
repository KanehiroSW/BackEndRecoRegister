from flask import Blueprint, request,jsonify
from models import db
import cv2
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity,create_access_token
from models.usuario import Usuario
from werkzeug.security import check_password_hash,generate_password_hash
import face_recognition
import base64
import numpy as np
from io import BytesIO
from PIL import Image

marcaciones_bp=Blueprint('marcaciones_bp', __name__)