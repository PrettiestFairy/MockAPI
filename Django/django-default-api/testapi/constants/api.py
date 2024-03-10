# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 10, 2024
"""


class Api:

    @classmethod
    def get_default_results(cls):
        return {"status": 500, "message": "Internal failure.", "data": None}


class DefaultHTTPStatusCode:
    GetData = 200
    CreateData = 201
    UpdateData = 202
    DeleteData = 204
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    InternalServerError = 500
    ServiceUnavailable = 503
    GatewayTimeout = 504
    HTTPVersionNotSupported = 505
