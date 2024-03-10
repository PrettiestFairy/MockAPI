# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 10, 2024
"""

from collections import OrderedDict

from rest_framework import serializers

from testapi.models.tb_test1 import TbTest1


# # 数据校验(方式三)
class CheckData:

    @classmethod
    def check_name(cls, value: str):
        if value.lower() in ("python", "django"):
            raise serializers.ValidationError(detail="姓名不能是Python或Django", code="validate_name")
        return value


class TbTest1Serializer(serializers.Serializer):
    # 字段类型, 简单的数校验
    id = serializers.IntegerField(label="ID", read_only=True)
    name = serializers.CharField(label="姓名", required=True, validators=(CheckData.check_name,))
    age = serializers.IntegerField(label="年龄", min_value=0, max_value=100)

    # 数据校验(方式一) 定义一个 validate_<字段名> 的方法, 在使用 is_valid() 方法时会自动调用
    def validate_name(self, value: str):
        if value.lower() in ("python", "django"):
            raise serializers.ValidationError(detail="姓名不能是Python或Django", code="validate_name")
        return value

    # 数据校验(方式二) 定义一个 validate 方法, 校验多个字段
    def validate(self, attrs: OrderedDict) -> OrderedDict:
        name: str = attrs.get("name")
        if name.lower() in ("python", "django"):
            raise serializers.ValidationError(detail="姓名不能是Python或Django", code="name")
        return attrs

    # 数据插入
    def create(self, validated_data: OrderedDict):
        return TbTest1.objects.create(**validated_data)

    # 数据更新
    def update(self, instance: TbTest1, validated_data: OrderedDict) -> TbTest1:
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        return instance
