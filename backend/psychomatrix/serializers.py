from datetime import datetime

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import PsychomatrixBaseContent, PsychomatrixAdditionalContent, Celebrity


class CelebritySerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = Celebrity
        read_only_fields = ('__all__',)
        exclude = ('id',)


class PsychomatrixBaseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title')
    number = serializers.CharField(source='code')
    description = serializers.CharField(source='text')
    celebrities = CelebritySerializer(many=True)

    class Meta:
        model = PsychomatrixBaseContent
        fields = ('name', 'number', 'description', 'celebrities')
        read_only_fields = ('name', 'number', 'description', 'celebrities')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        if "нет" in res.get("number"):
            res["number"] = ""
        return res


class PsychomatrixAdditionalSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title')
    number = serializers.CharField(source='level')
    description = serializers.CharField(source='text')

    class Meta:
        model = PsychomatrixAdditionalContent
        fields = ('name', 'number', 'description')
        read_only_fields = ('name', 'number', 'description')
        ordering = ('number',)




class DateSerializer(serializers.Serializer):
    date = serializers.DateField()

    def validate(self, data):
        """
        Проверка, что полученная дата меньше или равна текущей
        """
        if data['date'] > datetime.now().date():
            raise serializers.ValidationError('Запрашиваемая дата больше текущей')
        return data
