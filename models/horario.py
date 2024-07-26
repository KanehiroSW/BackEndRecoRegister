from . import db
from datetime import datetime


class Horario(db.Model):
    __tablename__ = 'horarios'
    id_horario = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('horarios', lazy=True))
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}