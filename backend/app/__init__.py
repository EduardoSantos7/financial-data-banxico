import sqlalchemy
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort


from backend.instance.config import app_config
from backend.app.schemas import UrlQuerySchema
from backend.app.utils.stats_utils import StatsUtils


# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from backend.app.models.UDIS import UDIS
    from backend.app.models.Dollars import Dollars

    app = FlaskAPI(__name__, instance_relative_config=True)
    print("FFF-------------------->", config_name)
    app.config.from_object(app_config['development'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/UDIS/', methods=['GET'])
    def udis():
        schema = UrlQuerySchema()

        errors = schema.validate(request.args)

        if errors:
            abort(400, str(errors))

        args = request.args

        udis = UDIS.get_udis_from_range(
            args.get('start_date', ''), args.get('end_date', ''))
        values = [udi.get('value') for udi in udis]
        _max, _min, avg = StatsUtils.max_min_avg(values)

        response = {'data': udis, 'max': _max, 'min': _min, 'avg': avg}
        response = jsonify(response)
        response.status_code = 200
        return response

    @app.route('/dollars/', methods=['GET'])
    def dolars():
        schema = UrlQuerySchema()

        errors = schema.validate(request.args)

        if errors:
            abort(400, str(errors))

        args = request.args

        dollars = Dollars.get_dollars_from_range(
            args.get('start_date', ''), args.get('end_date', ''))
        values = [dollar.get('value') for dollar in dollars]
        _max, _min, avg = StatsUtils.max_min_avg(values)

        response = {'data': dollars, 'max': _max, 'min': _min, 'avg': avg}
        response = jsonify(response)
        response.status_code = 200
        return response

    return app
