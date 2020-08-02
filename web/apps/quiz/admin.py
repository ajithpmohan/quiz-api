from django.contrib import admin

from apps.quiz import models as quiz_models


@admin.register(quiz_models.Question)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(quiz_models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(quiz_models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


class QuizContestResultInAdmin(admin.TabularInline):
    model = quiz_models.QuizContestResult


@admin.register(quiz_models.QuizContest)
class QuizContestAdmin(admin.ModelAdmin):
    inlines = [
        QuizContestResultInAdmin,
    ]
