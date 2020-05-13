from __future__ import unicode_literals

from rest_framework import viewsets
from apps.quiz import models as quiz_models
from apps.quiz import serializers as quiz_serializers


class QuizViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing quiz.
    """
    queryset = quiz_models.Quiz.objects.all()
    serializer_class = quiz_serializers.QuizSerializer
    # permission_classes = [IsAccountAdminOrReadOnly] #TODO



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
