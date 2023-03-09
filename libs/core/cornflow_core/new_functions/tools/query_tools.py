from sqlalchemy import tuple_


def in_list(model, **kwargs):
    """
    Filter the given fields.

    :param model: data model.
    :param kwargs: Accepted values for the given columns.
    expected format: column_name=[list_of_accepted_values]
    :return: a query
    """
    return (getattr(model, k).in_(as_list(v)) for k, v in kwargs.items())


def between(model, **kwargs):
    """
    Filter the given fields.

    :param model: data model.
    :param kwargs: Accepted values for the given columns.
    expected format: column_name=(min_value, max_value)
    :return: a query
    """
    clause = [v[0] <= getattr(model, k) for k, v in kwargs.items()] + [
        getattr(model, k) <= v[1] for k, v in kwargs.items()
    ]
    return clause


def get_combinations(model, schema, fields, combinations, max_query=2000):
    """
    Get data from a table filtering it by a combination of fields.
    For large tables, the model should define an index to increase query speed:
        __table_args__ = (db.Index("ix_combinations", "field_1", "field_2"))

    :param model: data model of the table.
    :param schema: data schema of the table.
    :param fields: fields of the combinations
    :param combinations: values of the combinations as a list of tuples
    :param max_query: max length of combinations to query at the same time (databases are limited to a few thousands).
    :return: data as a list of dict.
    """
    model_fields = [getattr(model, f) for f in fields]
    n = len(combinations)
    n_query = 1 + n // max_query
    result = []
    for i in range(n_query):
        comb = combinations[i * max_query : min((i + 1) * max_query, n)]
        # print(f"Querying combinations in model {model}: batch {i}")
        condition = tuple_(*model_fields).in_(comb)
        query = model.query.filter(condition).all()
        ri = schema().dump(query, many=True)
        result += ri
    return result


def as_list(v):
    """
    Transform single values (int, float, str) into list.
    Keep unchanged if already a list.
    Raise an error otherwise.

    :param v: a value
    :return: a list
    """
    if isinstance(v, tuple) or isinstance(v, list):
        return list(v)
    elif isinstance(v, str) or isinstance(v, int) or isinstance(v, float):
        return [v]
    else:
        raise TypeError(
            "Values passed to filter_in should be list or single value. Got {} instead".format(
                v
            )
        )
