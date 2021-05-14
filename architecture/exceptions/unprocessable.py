from rest_framework.exceptions import APIException

STATUS_CODE = 422


class UnprocessableForm(APIException):
    status_code = STATUS_CODE
    default_detail = 'Formulário não é válido'
    default_code = 'form_not_valid'


class UnprocessablePatternDate(APIException):
    status_code = STATUS_CODE
    default_detail = 'Padrão de data inválida, use por padrão: DD/MM/YYYY'
    default_code = 'date_pattern_not_valid'


class UnprocessableDatePeriod(APIException):
    status_code = STATUS_CODE
    default_detail = 'Período de data inválido'
    default_code = 'date_period_not_valid'


class UnprocessableCPF(APIException):
    status_code = STATUS_CODE
    default_detail = 'CPF inválido'
    default_code = 'cpf_not_valid'


class CustomUnprocessable(APIException):
    status_code = STATUS_CODE
    detail = None

    def __init__(self, message):
        CustomUnprocessable.detail = message
