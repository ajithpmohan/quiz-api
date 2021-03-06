# Generated by Django 2.2.12 on 2020-06-04 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=256, verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name of Quiz')),
                ('question', models.ManyToManyField(related_name='Questions', to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quiz',
            },
        ),
        migrations.CreateModel(
            name='QuizContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Completed')], default='P', max_length=16)),
                ('score', models.PositiveSmallIntegerField(default=0)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizcontests', related_query_name='quizcontest', to='quiz.Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizcontests', related_query_name='quizcontest', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'QuizContest',
                'verbose_name_plural': 'QuizContests',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=512, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', related_query_name='answer', to='quiz.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuizContestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Answer')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_results', related_query_name='contest_result', to='quiz.QuizContest')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_results', related_query_name='contest_result', to='quiz.Question')),
            ],
            options={
                'verbose_name': 'QuizContestResult',
                'verbose_name_plural': 'QuizContestResults',
                'unique_together': {('contest', 'question')},
            },
        ),
    ]
