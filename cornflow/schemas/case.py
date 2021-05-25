from marshmallow import fields, Schema

from .common import QueryFilters as QueryFiltersCase


class CaseBase(Schema):
    """ """

    id = fields.Int()
    path = fields.Str()
    name = fields.Str()
    description = fields.Str()
    data = fields.Raw()
    data_hash = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
    solution = fields.Raw()
    solution_hash = fields.String()
    schema = fields.String()


class CaseRawData(Schema):

    name = fields.Str(required=True)
    description = fields.Str()
    schema = fields.String(required=True)
    path = fields.Str(required=True)
    data = fields.Raw(required=True)
    solution = fields.Raw()


class CaseListResponse(Schema):
    id = fields.Int()
    path = fields.Str()
    name = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
    schema = fields.String()
    dependents = fields.List(fields.Int())


class CaseEditRequest(Schema):
    path = fields.Str()
    name = fields.Str()
    description = fields.Str()
    schema = fields.String()


class CaseSchema(Schema):
    """ """

    id = fields.Int(required=True)


class CaseRequest(Schema):
    """ """

    pass


class CaseFromInstanceExecution(Schema):
    """ """

    instance_id = fields.Str()
    execution_id = fields.Str()
    name = fields.Str(required=True)
    description = fields.Str()
    path = fields.Str(required=True)


class CaseToLive(Schema):
    """ """

    instance_id = fields.Str(required=True)
    execution_id = fields.Str()
    schema = fields.Str(required=True)
