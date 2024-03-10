# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 09, 2024
"""

from rest_framework.routers import DefaultRouter
from testapi.controllers.tb_test1 import TbTest1ViewSet
from testapi.controllers.tb_test1 import TbTestApi
from django.urls import path, re_path

routes = DefaultRouter()
# routes.register(r"test", TbTest1ViewSet, basename="test")

urlpatterns = list()
urlpatterns.extend(routes.urls)
urlpatterns.append(re_path(r"dtest/", TbTestApi.as_view()))

for i in urlpatterns: print(i)
