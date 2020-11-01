from backend.app import db


class UDIS(db.Model):
    """This class represents the power plant table."""

    __tablename__ = 'udis'
    __bind_key__ = 'udis'

    date = db.Column(db.Date(), primary_key=True, index=True)
    value = db.Column(db.Integer)

    def __init__(self, date, value):
        self.date = date
        self.value = value

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_udis_from_range(start_date=None, end_range=None):
        return [{'date': '12/12/12', 'value': 6.4}, {'date': '13/12/12', 'value': 6.5}]

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<UDIS: {self.date} Value: {self.value}>"
