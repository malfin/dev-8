# Generated by Django 2.2 on 2021-05-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210517_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='title',
            field=models.CharField(choices=[('0', 'Да'), ('1', 'Нет')], max_length=4096, verbose_name='ответ'),
        ),
    ]
