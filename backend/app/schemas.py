from marshmallow import Schema, fields


class UrlQuerySchema(Schema):
    start_date = fields.Date('%Y-%m-%d')
    end_date = fields.Date('%Y-%m-%d')
