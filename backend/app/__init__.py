import sqlalchemy
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort


from backend.instance.config import app_config
from backend.app.schemas import UrlQuerySchema


# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from backend.app.models.UDIS import UDIS

    app = FlaskAPI(__name__, instance_relative_config=True)
    print("FFF-------------------->", config_name)
    app.config.from_object(app_config['development'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/UDIS/', methods=['GET'])
    def udis():
        schema = UrlQuerySchema()

        errors = schema.validate(request.args)

        if errors:
            abort(400, str(errors))

        args = request.args

        udis = UDIS.get_udis_from_range()

        response = jsonify(udis)
        response.status_code = 200
        return response

    return app
