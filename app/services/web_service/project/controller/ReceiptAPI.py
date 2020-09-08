import datetime
import json
from datetime import datetime

from dateutil import parser

import pandas as pd
from flask import jsonify, render_template, request, session
from flask.views import MethodView
from flask_login import current_user, login_required
from project import create_app, db
from project.models.ReceiptData import ReceiptData


class ReceiptAPI(MethodView):

    def post(self):
        """Add new receipt"""
        receipt_data = request.get_json()

        if receipt_data:
            # if date is empty set to todays date
            if not receipt_data['date']:
                date = datetime.date.today()
                receipt_data['date'] = str(date)

            new_receipt = ReceiptData(
                image=receipt_data['image'],
                vendor=receipt_data['vendor'],
                price=receipt_data['price'],
                date=parser.parse(receipt_data['date']),
                category=receipt_data['category'],
                warranty='',
                user_id=receipt_data['user_id']
            )
            db.session.add(new_receipt)
            db.session.commit()
            return jsonify({'status': 'Receipt has been added'}), 200

        return jsonify({'status': 'Invalid request!'}), 400

    def put(self, id):
        receipt = ReceiptData.query.filter_by(id=id).first()

        req_data = request.get_json()

        receipt.vendor = req_data['vendor']
        receipt.price = req_data['amount']
        # receipt.warranty = req_data['warranty']
        receipt.date = parser.parse(req_data['date']).date()
        receipt.category = req_data['category']
        db.session.commit()
        
        return jsonify({'status': 'Updated!'}), 200

    def delete(self, id):
        ReceiptData.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({'status': f'Receipt with ID: {id} has been deleted'}), 200

    def calculate_sum(self, data):
        """Calculate total sum for specified month"""
        return sum([float(field.price)
                    for field in data if field.price]
                   )

    def monthly_spending_data(self, data):
        """Get spendings of each month of the current year"""
        monthly_spendgings = {
            'January': [],
            'February': [],
            'March': [],
            'April': [],
            'May': [],
            'June': [],
            'July': [],
            'August': [],
            'September': [],
            'October': [],
            'November': [],
            'December': []
        }
        for receipt in data:
            month = receipt.date.strftime("%B")
            amount = receipt.price if receipt.price else 0
            monthly_spendgings[month].append(float(amount))
        return monthly_spendgings

    def get_categories(self, id):
        receipts = ReceiptData.query.filter_by(user_id=id).all()
        categories = [cat.category for cat in receipts if cat.category]
        return categories

    def get(self, id):
        """Get users receipt data"""
        today = datetime.today()
        year = today.year

        yearly_data = ReceiptData.query.filter(ReceiptData.user_id == id,
                                               ReceiptData.date.between(f'{year}-1-1', f'{year}-12-31')).all()
        monthy_spendings_data = self.monthly_spending_data(yearly_data)
        cat = self.get_categories(id)
        data = {
            'yearly': monthy_spendings_data,
            'categories': cat
        }
        return jsonify(data), 200
