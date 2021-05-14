from rest_framework.exceptions import APIException

STATUS_CODE = 400


class BadRequestCRUD(APIException):
    status_code = STATUS_CODE
    default_detail = 'Falha na comunicação com o banco de dados'
    default_code = 'failed_commn_database'
