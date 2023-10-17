from datetime import datetime

from rest_framework import serializers

from .models import DestinyMatrixContent


# class MatrixElementSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MatrixElement
#         read_only_fields = ('__all__',)
#         exclude = ('id',)


class DestinyMatrixSerializer(serializers.ModelSerializer):
    # elements = MatrixElementSerializer(many=True)

    class Meta:
        model = DestinyMatrixContent
        fields = ('title', 'meaning', 'elements', 'value', 'code')
        read_only_fields = ('__all__',)

    # def to_representation(self, instance):
    #     res = super().to_representation(instance)
    #     if "нет" in res.get("number"):
    #         res["number"] = ""
    #     return res


# TODO: вынести этот сериализатор куда-нибудь, т.к. он используется в двух местах
class DateSerializer(serializers.Serializer):
    date = serializers.DateField()

    def validate(self, data):
        """
        Проверка, что полученная дата меньше или равна текущей
        """
        if data['date'] > datetime.now().date():
            raise serializers.ValidationError(
                'Запрашиваемая дата больше текущей'
            )
        return data
