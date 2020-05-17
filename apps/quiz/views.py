from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.quiz import models as quiz_models
from apps.quiz import serializers as quiz_serializers


class QuestionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing question.
    """
    queryset = quiz_models.Question.objects.all()
    serializer_class = quiz_serializers.QuestionSerializer
    # permission_classes = [IsAccountAdminOrReadOnly] #TODO


class AnswerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing answer.
    """
    queryset = quiz_models.Answer.objects.all()
    serializer_class = quiz_serializers.AnswerSerializer
    # permission_classes = [IsAccountAdminOrReadOnly] #TODO


class QuizViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing quiz.
    """
    queryset = quiz_models.Quiz.objects.all()
    serializer_class = quiz_serializers.QuizSerializer
    # permission_classes = [IsAccountAdminOrReadOnly] #TODO


class QuizContestViewset(viewsets.ModelViewSet):

    queryset = quiz_models.QuizContest.objects.all()

    def get_serializer_class(self):
        if self.action == 'quiz':
            return quiz_serializers.QuizNestedSerializer
        else:
            return quiz_serializers.QuizContestSerializer

    @action(detail=True, methods=['get'])
    def quiz(self, request, pk=None):
        serializer = self.get_serializer_class()(self.get_object().quiz)
        return Response(serializer.data)
