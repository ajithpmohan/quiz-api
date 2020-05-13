from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common import models as common_models


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

class Question(common_models.BaseModel):
    question = models.CharField(_('Question'), max_length=256)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class Answer(common_models.BaseModel):
    answer = models.CharField(_('Answer'), max_length=512)
    question = models.ForeignKey(
        'quiz.Question',
        related_name='%(class)ss',
        related_query_name='answer',
        on_delete=models.CASCADE
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question} - {self.answer}'
