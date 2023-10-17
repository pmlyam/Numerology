from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from destinymatrix.serializers import (DateSerializer,
                                       DestinyMatrixSerializer)
from .calculator import DestinyMatrix, get_contents


class MatrixOfDestinyView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        # проверка корректности даты рождения
        serializer = DateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # расчет элементов матрицы судьбы
        calculator = DestinyMatrix(data['date'])
        calculator.get_matrix_points()
        # расшифровка полученных значений
        matrix_codes = calculator.get_matrix_points_w_titles()
        meaning = get_contents(matrix_codes)
        matrix_description = DestinyMatrixSerializer(meaning, many=True).data

        return Response(
            data=matrix_description,
            status=status.HTTP_200_OK
        )
