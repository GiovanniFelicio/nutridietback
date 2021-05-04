from rest_framework.exceptions import APIException

STATUS_CODE = 422

class UnprocessableForm(APIException):
    status_code = STATUS_CODE
    default_detail = 'Form is not valid'
    default_code = 'form_not_valid'

class UnprocessablePatternDate(APIException):
    status_code = STATUS_CODE
    default_detail = 'Invalid date pattern, please use the pattern: DD/MM/YYYY'
    default_code = 'date_pattern_not_valid'

class UnprocessableDatePeriod(APIException):
    status_code = STATUS_CODE
    default_detail = 'Invalid date period, please make sure the date period is valid'
    default_code = 'date_period_not_valid'

class UnprocessableCPF(APIException):
    status_code = STATUS_CODE
    default_detail = 'Invalid CPF, check if it is correct '
    default_code = 'cpf_not_valid'


