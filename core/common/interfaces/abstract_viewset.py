from rest_framework.viewsets import ViewSet
from rest_framework import status


class AbstractViewSet(ViewSet):

    def get_status(self):
        return status
