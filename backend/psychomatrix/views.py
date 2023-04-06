from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .calculator import Calculator, get_contents
from .serializers import (
    DateSerializer, PsychomatrixBaseSerializer, PsychomatrixAdditionalSerializer,
)


class SquareOfPythagorasView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = DateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        calculator = Calculator(data['date'])
        numbers = calculator.get_all_numbers()
        basic, addition = get_contents(numbers)
        return Response(
            {
                'mainInfo': [
                    {'basic': PsychomatrixBaseSerializer(basic, many=True).data},
                    {'addition': PsychomatrixAdditionalSerializer(basic, many=True).data},
                ]
            },
            status=status.HTTP_200_OK
        )
