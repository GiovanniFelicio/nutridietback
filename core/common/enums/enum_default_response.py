from rest_framework import status


class EnumDefaultResponse():
    # Authentication #
    SUCCESSFULLY_LOGGED_IN = {'status': status.HTTP_200_OK, 'message': 'Login efetuado com sucesso'}

    # SAVE #
    SUCCESSFULLY_CREATED = {'status': status.HTTP_201_CREATED, 'message': 'Criado com Sucesso'}