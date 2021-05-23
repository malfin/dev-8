# Generated by Django 2.2 on 2021-05-17 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='title',
            field=models.CharField(max_length=4096, verbose_name='ответ'),
        ),
    ]