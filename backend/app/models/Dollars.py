import os
from datetime import datetime
from datetime import timedelta

from backend.app.utils.SIEUtils import SIEUtils
from backend.app.utils.SIEUtils import SIESeries
from backend.app import db


class Dollars(db.Model):
    """This class represents the power plant table."""

    __tablename__ = 'dollars'
    __bind_key__ = 'dollars'

    date = db.Column(db.Date(), primary_key=True, index=True)
    value = db.Column(db.Float)

    def __init__(self, date, value):
        self.date = datetime.strptime(date, '%d/%m/%Y').date() if isinstance(date, str) else date
        self.value = value

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def save_from_list(dollars):
        added = []
        for dollar in dollars:
            try:
                value = float(dollar.get('dato'))
            except (ValueError, TypeError):
                value = 0

            obj = Dollars(dollar.get('fecha'), value)
            obj.save()
            added.append(obj.as_dict())

        return added

    @staticmethod
    def get_dollars_from_range(start_range, end_range):
        # Get the data saved on the db that match in the user's range
        dollars = db.session.query(Dollars).filter(Dollars.date.between(start_range, end_range)).all()
        if dollars:
            result = []
            for dollar in dollars:
                result.append(dollar.as_dict())

            # Verify the begging and ending of the range
            query_start_date = result[0].get('date')
            query_end_date = result[-1].get('date')
            begin_range_data = []
            end_range_data = []

            # If the user range starts before the query results then we need to request the missing data.
            start_date = datetime.strptime(start_range, '%Y-%m-%d').date()
            if query_start_date > start_date:
                begin_range_data = SIEUtils.get_data(
                    SIESeries.Dollars, start_date, (query_start_date - timedelta(days=1)).strftime('%Y-%m-%d'))

                begin_range_data = Dollars.save_from_list(begin_range_data)

            # If the user range ends after the query results then we need to request the missing data.
            end_date = datetime.strptime(end_range, '%Y-%m-%d').date()
            if query_end_date < end_date:
                end_range_data = SIEUtils.get_data(
                    SIESeries.Dollars, (query_end_date + timedelta(days=1)).strftime('%Y-%m-%d'), end_range)

                end_range_data = Dollars.save_from_list(end_range_data)

            return begin_range_data + result + end_range_data

        # If no previous record inside the range.
        else:
            data = SIEUtils.get_data(SIESeries.Dollars, start_range, end_range)
            data = Dollars.save_from_list(data)
            return data

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Dolar: {self.date} Value: {self.value}>"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
