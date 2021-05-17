from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.question
