from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common import models as common_models

User = get_user_model()


class Question(common_models.BaseModel):
    text = models.CharField(_('Question'), max_length=256)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.text


class Answer(common_models.BaseModel):
    text = models.CharField(_('Answer'), max_length=512)
    question = models.ForeignKey(
        'quiz.Question',
        related_name='%(class)ss',
        related_query_name='answer',
        on_delete=models.CASCADE
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question} - {self.text}'


class Quiz(common_models.BaseModel):
    name = models.CharField(_('Name of Quiz'), max_length=128)
    question = models.ManyToManyField(
        'quiz.Question',
        _('Questions'),
    )

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quiz'

    def __str__(self):
        return self.name


class QuizContest(common_models.BaseModel):

    PENDING, COMPLETED = 'P', 'C'

    STATUS_CHOICES = (
        (PENDING, _('Pending')),
        (COMPLETED, _('Completed')),
    )

    user = models.ForeignKey(
        User,
        related_name='%(class)ss',
        related_query_name='quizcontest',
        on_delete=models.CASCADE
    )

    quiz = models.ForeignKey(
        'quiz.Quiz',
        related_name='%(class)ss',
        related_query_name='quizcontest',
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=16, default=PENDING, choices=STATUS_CHOICES)
    score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'QuizContest'
        verbose_name_plural = 'QuizContests'

    def __str__(self):
        return f'{self.user} - {self.quiz} - {self.score}'
