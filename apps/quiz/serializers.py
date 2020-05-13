from __future__ import unicode_literals

from rest_framework import serializers

from apps.quiz import models as quiz_models


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.Answer
        fields = ('question', 'answer', 'is_correct')

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = quiz_models.Question
        fields = ('question', 'answers')

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.Quiz
        fields = ('name', 'question')
