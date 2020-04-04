from flask import jsonify

from project import db


class ReceiptData(db.Model):

    def __init__(self, vendor, price, date, category):
        self.vendor = vendor
        self.price = price
        self.date = date
        self.category = category

    __tablename__ = "receipt_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendor = db.Column(db.String(255))
    price = db.Column(db.String(20))
    date = db.Column(db.DateTime)
    category = db.Column(db.String(255))
