import csv

from django.core.management.base import BaseCommand
from drf_extra_fields.fields import Base64ImageField

from psychomatrix.models import Celebrity

CSV_PATH = 'data/'
DICT = {
    Celebrity: 'celebrity.csv',
}


def csv_import(csv_data, model):
    objs = []
    for row in csv_data:
        objs.append(model(**row))
    # objs = [model(**row) for row in csv_data]
    model.objects.bulk_create(objs)


class Command(BaseCommand):
    help = 'import data from csv files'

    def handle(self, *args, **kwargs):
        for model in DICT:
            with open(
                    CSV_PATH + DICT[model],
                    newline='',
                    encoding='utf8'
            ) as csv_file:
                csv_import(csv.DictReader(csv_file), model)
