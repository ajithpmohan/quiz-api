from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.quiz import models as quiz_models

User = get_user_model()


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.Answer
        fields = ('id', 'question', 'text', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = quiz_models.Question
        fields = ('id', 'text', 'answers')


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.Quiz
        fields = ('id', 'name', 'question')


class QuizNestedSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = quiz_models.Quiz
        fields = ('id', 'name', 'question')


class QuizContestSerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.QuizContest
        fields = ('id', 'quiz')

    def create(self, validated_data):
        validated_data['user'] = User.objects.first()  # TODO
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        validated_data['user'] = User.objects.first()  # TODO
        instance = super().update(instance, validated_data)
        return instance
