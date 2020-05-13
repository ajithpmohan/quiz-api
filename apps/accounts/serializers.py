from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.accounts import models as accounts_models
from apps.quiz import serializers as quiz_serializers

User = get_user_model()

class QuizContestSerializer(serializers.ModelSerializer):

    questions = quiz_serializers.QuestionSerializer(many=True)

    class Meta:
        model = accounts_models.QuizContest
        fields = ('questions',)

    # def create(self, validated_data):
    #     import bpdb; bpdb.set_trace()
    #     validated_data['user'] = User.objects.get(is_superuser=True) #TODO - CHANGE LATER
    #     kwargs = validated_data.pop('quiz')
    #     instance = super().create(validated_data)
    #     return instance

    # def update(self, instance, validated_data):
    #     kwargs = validated_data.pop('stock')
    #     instance = super().update(instance, validated_data)
    #     return instance
