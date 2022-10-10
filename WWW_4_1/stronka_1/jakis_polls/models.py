from django.db import models


class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Answer(models.Model):
    def __str__(self):
        return self.answer
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)
    answer = models.TextField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
