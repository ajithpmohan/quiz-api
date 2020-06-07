from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.quiz import models as quiz_models

User = get_user_model()


class QuizContestResultsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):

        user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')

        question1 = quiz_models.Question.objects.create(text='How many continents are there in the world?')
        question2 = quiz_models.Question.objects.create(text='What’s the tallest mountain in the world?')
        question3 = quiz_models.Question.objects.create(text='What sound does a dog make?')
        question4 = quiz_models.Question.objects.create(text='What sound does a cat make?')

        quiz_models.Answer.objects.bulk_create([
            quiz_models.Answer(question=question1, text='7', is_correct=True),
            quiz_models.Answer(question=question1, text='6', is_correct=False),
            quiz_models.Answer(question=question2, text='Mount K2', is_correct=False),
            quiz_models.Answer(question=question2, text='Mount Everest', is_correct=True),
            quiz_models.Answer(question=question3, text='Mooo', is_correct=False),
            quiz_models.Answer(question=question3, text='Bow', is_correct=True),
            quiz_models.Answer(question=question4, text='Bow', is_correct=False),
            quiz_models.Answer(question=question4, text='Meow', is_correct=True),
        ])

        quiz1 = quiz_models.Quiz.objects.create(name='Geography Quiz')
        quiz1.question.add(question1, question2)

        quiz2 = quiz_models.Quiz.objects.create(name='Geography Quiz')
        quiz2.question.add(question3, question4)

        quiz_models.QuizContest.objects.create(user=user1, quiz=quiz1)
        quiz_models.QuizContest.objects.create(user=user1, quiz=quiz2)

    def test_quizcontest_ids_are_not_equal(self):
        url = reverse('quiz:quizcontest-results', kwargs={'pk': 1})
        data = [
            {
                'contest': 1,
                'question': 1,
                'answer': 1
            },
            {
                'contest': 2,
                'question': 3,
                'answer': 6
            }
        ]

        response = self.client.post(url, data)

        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_quizcontest_ids_are_equal(self):
        url = reverse('quiz:quizcontest-results', kwargs={'pk': 1})
        data = [
            {
                'contest': 1,
                'question': 1,
                'answer': 2
            }
        ]

        response = self.client.post(url, data)

        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dict(response.data[0]), {'contest': 1, 'question': 1, 'answer': 2})

    def test_question_not_in_quiz(self):
        url = reverse('quiz:quizcontest-results', kwargs={'pk': 2})
        data = [
            {
                'contest': 2,
                'question': 2,
                'answer': 4
            }
        ]

        response = self.client.post(url, data)

        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_question_in_quiz(self):
        url = reverse('quiz:quizcontest-results', kwargs={'pk': 2})
        data = [
            {
                'contest': 2,
                'question': 4,
                'answer': 8
            },
            {
                'contest': 2,
                'question': 3,
                'answer': 5
            }
        ]

        response = self.client.post(url, data)

        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dict(response.data[0]), {'contest': 2, 'question': 4, 'answer': 8})
        self.assertEqual(dict(response.data[1]), {'contest': 2, 'question': 3, 'answer': 5})
