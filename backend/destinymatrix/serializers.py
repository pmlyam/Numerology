from datetime import datetime

from rest_framework import serializers

from .models import DestinyMatrixContent


class DestinyMatrixSerializer(serializers.ModelSerializer):

    class Meta:
        model = DestinyMatrixContent
        fields = ('title', 'meaning', 'elements', 'value', 'code')
        read_only_fields = ('__all__',)


# TODO: вынести этот сериализатор куда-нибудь
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
