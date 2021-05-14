from rest_framework.exceptions import APIException

STATUS_CODE = 409


class CustomConflict(APIException):
    status_code = STATUS_CODE
    detail = None

    def __init__(self, message):
        CustomConflict.detail = message
