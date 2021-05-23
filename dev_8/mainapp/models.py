from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    CHOICE = [
        ('0', 'Да'),
        ('1', 'Нет'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', default=1)
    title = models.CharField(max_length=4096, verbose_name='ответ', choices=CHOICE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.IntegerField(verbose_name='Отвечено', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-question']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
