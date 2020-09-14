
from flask import jsonify

from project import db


class ReceiptData(db.Model):
    __tablename__ = "receipt_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(255), nullable=False)
    vendor = db.Column(db.String(255))
    price = db.Column(db.String(20))
    date = db.Column(db.DateTime)
    category = db.Column(db.String(50))
    warranty = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, **kwargs):
        super(ReceiptData, self).__init__(**kwargs)

    def __repr__(self):
        return '<ReceiptData vendor: {} \n price: {} \n date: {} category: {}>' \
            .format(self.vendor, self.price, self.date, self.category)
