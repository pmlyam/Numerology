# Generated by Django 4.1.7 on 2023-08-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinyMatrixContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=55, null=True)),
                ('elements', models.CharField(blank=True, max_length=55, null=True)),
                ('value', models.CharField(blank=True, max_length=55, null=True)),
                ('meaning', models.CharField(blank=True, max_length=10240, null=True)),
                ('advice', models.CharField(blank=True, max_length=4096, null=True)),
                ('recommendation', models.CharField(blank=True, max_length=4096, null=True)),
            ],
            options={
                'db_table': 'destinymatrix_basic_contents',
            },
        ),
    ]