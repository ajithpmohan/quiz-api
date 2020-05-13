from django.db import models
# from django.contrib.auth import models as auth_models
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# class User(AbstractBaseUser, auth_models.PermissionsMixin):
#     # TODO
#     pass

from django.contrib.auth import get_user_model

from apps.common import models as common_models
from apps.quiz import models as quiz_models

User = get_user_model()


class QuizContest(common_models.BaseModel):
    user = models.ForeignKey(
        User,
        related_name='%(class)ss',
        related_query_name='quizcontest',
        on_delete=models.CASCADE
    )

    quiz = models.ForeignKey(
        quiz_models.Quiz,
        related_name='%(class)ss', #
        related_query_name='quizcontest',
        on_delete=models.CASCADE
    )

    score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'QuizContest'
        verbose_name_plural = 'QuizContests'

    def __str__(self):
        return f'{self.user} - {self.quiz} - {self.score}'
