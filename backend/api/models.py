from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Question(models.Model):
    ANSWER_CHOICES = (
        (1, 'a'),
        (2, 'b'),
        (3, 'c'),
        (4, 'd'),
    )
    prompt = models.CharField(max_length=200)
    choice_a = models.CharField(max_length=200)
    choice_b = models.CharField(max_length=200)
    choice_c = models.CharField(max_length=200)
    choice_d = models.CharField(max_length=200)
    answer = models.IntegerField(choices=ANSWER_CHOICES)

    def __str__(self):
        return self.prompt


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    # TODO randomize choices on the backend
    class Meta:
        model = Question
        fields = (
            'id',
            'prompt',
            'choice_a',
            'choice_b',
            'choice_c',
            'choice_d',
            'answer'
        )


class Score(models.Model):
    correct = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    name = models.CharField(max_length=200)


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = (
            'id',
            'correct',
            'total',
            'name',
        )
