from . import db
from datetime import datetime

class Marcacion(db.Model):
    __tablename__ = 'marcaciones'
    id_marcacion = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    min_tarde = db.Column(db.Integer, nullable=True)
    est_falta = db.Column(db.Integer, nullable=True)
    usuario = db.relationship('Usuario', backref=db.backref('marcaciones', lazy=True))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}