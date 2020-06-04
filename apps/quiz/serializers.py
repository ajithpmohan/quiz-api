from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers

from apps.quiz import models as quiz_models
from apps.quiz import relations as quiz_relations

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


class QuizContestResultSerializer(serializers.ModelSerializer):
    contest = quiz_relations.CustomPrimaryKeyField(queryset=quiz_models.QuizContest.objects.all(), required=True)
    question = quiz_relations.CustomPrimaryKeyField(queryset=quiz_models.Question.objects.all(), required=True)
    answer = quiz_relations.CustomPrimaryKeyField(
        allow_null=True, queryset=quiz_models.Answer.objects.all(), required=False
    )

    class Meta:
        model = quiz_models.QuizContestResult
        fields = ('contest', 'question', 'answer')

    def validate_contest(self, value):
        contest = self.context.get("contest")
        if value.id != contest.id:
            raise serializers.ValidationError("Invalid Contest")
        return value

    def validate_question(self, value):
        contest = self.context.get("contest")
        questions = contest.get_questions
        if value.id not in questions.values_list('id', flat=True):
            raise serializers.ValidationError(_("Invalid Question"))
        return value
