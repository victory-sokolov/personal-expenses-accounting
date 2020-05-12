import datetime
import json

import pandas as pd
from dateutil import parser
from flask import (Flask, current_app, jsonify, render_template, request,
                   session)
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
                # warranty='',
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
        receipt.date = req_data['date']
        receipt.category = req_data['category']
        db.session.commit()
        return jsonify({'status': 'Updated!'}), 200

    def delete(self, id):
        ReceiptData.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({'status': f'Receipt with ID: {id} has been deleted'}), 200

    def get(self, id):
        today = datetime.datetime.today()
        year = today.year
        month = today.month

        monthly_data = ReceiptData.query.filter(ReceiptData.user_id == id,
            ReceiptData.date.between(f'{year}-{month}-1', f'{year}-{month+1}-1')).all()
        monthly_spendings = sum([float(field.price)
                             for field in monthly_data if field.price])

        data = {
            'monthly': monthly_spendings
        }
        return jsonify(data), 200
