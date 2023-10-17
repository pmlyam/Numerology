from django.db import models


# class MatrixElement(models.Model):
#     # TODO: так вроде красивее, но это доп запросы в БД => оверинжиниринг?
#     elements = models.CharField(
#         max_length=55,
#         null=True,
#         blank=True
#     )
#     title = models.CharField(
#         max_length=55,
#         null=True,
#         blank=True
#     )


class DestinyMatrixContent(models.Model):
    """
    title - название раздела
    meaning - расшифровка матрицы в контексте раздела
    advice - совет, как относиться к получившимся расчетам
    recommendation - совет, как работать над собой в этой сфере жизни
    matrix_elements - элементы матрицы, которые относятся к текущему разделу, и их значения
    """
    title = models.CharField(
        max_length=55,
        null=True,
        blank=True
    )
    elements = models.CharField(
        max_length=55,
        null=True,
        blank=True
    )
    value = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    code = models.CharField(
        max_length=55,
        null=True,
        blank=True
    )
    meaning = models.CharField(
        max_length=10240,
        null=True,
        blank=True
    )
    advice = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )
    recommendation = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'destinymatrix_basic_contents'
