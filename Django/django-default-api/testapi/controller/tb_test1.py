# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 09, 2024
"""

from testapi.models.tb_test1 import TbTest1
from rest_framework import viewsets

class TbTest1ViewSet(viewsets.ModelViewSet):
    queryset = TbTest1.objects.all()
    serializer_class = TbTest1Serializer

