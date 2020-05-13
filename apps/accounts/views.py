from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.response import Response

from apps.accounts import models as account_models
from apps.quiz import models as quiz_models
from apps.accounts import serializers as accounts_serializers

class QuizContestViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        instance = self.get_queryset()
        serializer = accounts_serializers.QuizContestSerializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = quiz_models.Question.objects.filter(id=pk)
        return get_object_or_404(instance, pk=pk)
