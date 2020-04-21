from flask import jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from project import db


class User(db.Model):

    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(70))
    password = db.Column(db.String(255))
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User name: {} \n email: {} \n password:{}>' \
            .format(self.name, self.email, self.password)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def get_password(self, password):
        return check_password_hash(self.password, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.user_id}).decode("utf-8")


    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False

        if data.get('confirm') != self.user_id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
