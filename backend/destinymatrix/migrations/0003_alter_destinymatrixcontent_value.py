# Generated by Django 4.1.7 on 2023-09-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinymatrix', '0002_destinymatrixcontent_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinymatrixcontent',
            name='value',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]