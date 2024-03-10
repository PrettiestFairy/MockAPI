# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 09, 2024
"""

import json

from rest_framework import viewsets
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http.response import JsonResponse

from testapi.models.tb_test1 import TbTest1
from testapi.serializers.tb_test1 import TbTest1Serializer
from testapi.constants.api import Api, DefaultHTTPStatusCode
from testapi.constants.simulation import ClientData


class TbTest1ViewSet(viewsets.ModelViewSet):
    queryset = TbTest1.objects.all()
    serializer_class = TbTest1Serializer


class TbTestApi(View):

    # 序列化 - 获取数据
    # def get(self, request: HttpRequest) -> HttpResponse:
    #     __results = Api.get_default_results()
    #     serializer = TbTest1Serializer(instance=TbTest1.objects.all(), many=True)
    #     __results.update({"status": 200, "message": "Success", "data": serializer.data})
    #     return JsonResponse(data=__results, status=200)

    # 序列化 - 数据验证
    # def get(self, request: HttpRequest) -> HttpResponse:
    #     # __data = json.dumps(request.body)
    #     __data = ClientData.get_test_api()
    #     __results = Api.get_default_results()
    #     serializer = TbTest1Serializer(data=__data)
    #     if serializer.is_valid():
    #         __results.update({"status": 200, "message": "Success", "data": "OK"})
    #     else:
    #         __results.update({"status": 500, "message": "Failure", "data": serializer.errors})
    #     return JsonResponse(data=__results, status=DefaultHTTPStatusCode.GetData)

    # 序列化 - 添加数据
    # def get(self, request: HttpRequest) -> HttpResponse:
    #     __data = ClientData.get_test_api()
    #     __results = Api.get_default_results()
    #     serializer = TbTest1Serializer(data=__data)
    #     if serializer.is_valid():    
    #         serializer.save()
    #         __results.update({"status": 201, "message": "Success", "data": serializer.data})
    #     return JsonResponse(data=__results, status=__results.get("status"))

    # 序列化 - 更新数据
    def get(self, request: HttpRequest) -> HttpResponse:
        __results = Api.get_default_results()
        # 获取数据
        try:
            tb_test1_data = TbTest1.objects.get(pk=2)
        except TbTest1.DoesNotExist:
            __results.update({"status": "400"})
            return JsonResponse(data=__results, status=DefaultHTTPStatusCode.BadRequest)

        __data = ClientData.get_test_api()
        serializer = TbTest1Serializer(instance=tb_test1_data, data=__data)
        serializer.is_valid()
        serializer.save()
        __results.update({"status": 200, "message": "Success", "data": serializer.data})
        return JsonResponse(data=__results, status=__results.get("status"))
