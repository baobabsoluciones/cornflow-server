from marshmallow import fields, Schema


class HealthResponse(Schema):

    cornflow_status = fields.Str()
    backend_status = fields.Str()
