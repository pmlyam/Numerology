# Generated by Django 4.1.7 on 2023-09-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinymatrix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinymatrixcontent',
            name='code',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
