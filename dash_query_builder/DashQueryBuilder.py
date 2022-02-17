# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashQueryBuilder(Component):
    """A DashQueryBuilder component.
DashQueryBuilder is a Dash Component based on [`react-awesome-query-builder`](https://github.com/ukrbublik/react-awesome-query-builder).

It takes a `fields` property to generate the options for building the actual query.
The optional property `tree` is used to define the current state of the tree. It can be used to
define the starting state of the query builder.
The optional property `theme` is one of `material`, `mui`, `antd`, `bootstrap` or `basic`. This is the styling of the component.
These are the only themes supported by `react-awesome-query-builder`.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- fields (optional):
    The fields that are used to populate the options for the query
    builder. This can be a very complicated object.  See
    https://github.com/ukrbublik/react-awesome-query-builder/blob/master/CONFIG.adoc#configfields
    for more info.

- jsonLogicFormat (string; optional):
    The JSON Logic Formatted string defined by the current state of
    the tree.

- mongodbFormat (string; optional):
    The MongoDB Formatted string defined by the current state of the
    tree.

- queryBuilderStringFormat (string; optional):
    The Query Builder String Formatted string defined by the current
    state of the tree.

- queryStringFormat (string; optional):
    The Query String Formatted string defined by the current state of
    the tree.

- sqlFormat (string; optional):
    The SQL Formatted string defined by the current state of the tree.

- theme (a value equal to: 'material', "mui", 'antd', 'basic', 'bootstrap'; default 'basic'):
    Sets the theme of the query builder.

- tree (boolean | number | string | dict | list; default loadTree(emptyTree)):
    The tree that describes the state of the query builder."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, tree=Component.UNDEFINED, fields=Component.UNDEFINED, sqlFormat=Component.UNDEFINED, queryStringFormat=Component.UNDEFINED, queryBuilderStringFormat=Component.UNDEFINED, mongodbFormat=Component.UNDEFINED, jsonLogicFormat=Component.UNDEFINED, theme=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'fields', 'jsonLogicFormat', 'mongodbFormat', 'queryBuilderStringFormat', 'queryStringFormat', 'sqlFormat', 'theme', 'tree']
        self._type = 'DashQueryBuilder'
        self._namespace = 'dash_query_builder'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'fields', 'jsonLogicFormat', 'mongodbFormat', 'queryBuilderStringFormat', 'queryStringFormat', 'sqlFormat', 'theme', 'tree']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashQueryBuilder, self).__init__(**args)
