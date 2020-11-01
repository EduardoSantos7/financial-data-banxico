import os
from datetime import datetime

from backend.app.utils.SIEUtils import SIEUtils
from backend.app.utils.SIEUtils import SIESeries
from backend.app import db


class UDIS(db.Model):
    """This class represents the power plant table."""

    __tablename__ = 'udis'
    __bind_key__ = 'udis'

    date = db.Column(db.Date(), primary_key=True, index=True)
    value = db.Column(db.Float)

    def __init__(self, date, value):
        self.date = datetime.strptime(date, '%d/%m/%Y').date()
        self.value = value

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_udis_from_range(start_date, end_range):
        data = SIEUtils.get_data(SIESeries.UDIS, start_date, end_range)
        return data

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<UDIS: {self.date} Value: {self.value}>"
