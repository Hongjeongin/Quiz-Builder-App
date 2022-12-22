from django.db import models

class User(models.Model):
    email = models.EmailField(max_length = 128, verbose_name = 'E-mail')
    password = models.CharField(max_length = 50, verbose_name = 'Password')
    registered_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Registered_Date')
    validation = models.BooleanField(default = False, verbose_name = 'Validation')

    class Meta:
        ordering = ['-registered_date']

class Quiz(models.Model):
    title = models.CharField(max_length = 200, blank = True, verbose_name = 'Title')
    count_of_visitor = models.IntegerField(default = 0, verbose_name = 'Visitor')
    published = models.BooleanField(default = False, verbose_name = 'Published')
    owner = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Owner')
    
class Question(models.Model):
    question_text = models.CharField(max_length = 200, verbose_name = 'Text')
    possible_answer_first = models.CharField(max_length = 100, verbose_name = 'first_answer')
    possible_answer_second = models.CharField(max_length = 100, verbose_name = 'second_answer')
    possible_answer_third = models.CharField(max_length = 100, verbose_name = 'third_answer')
    possible_answer_fourth = models.CharField(max_length = 100, verbose_name = 'fourth_answer')
    possible_answer_fifth = models.CharField(max_length = 100, verbose_name = 'fifth_answer')
    correct_answer_first = models.BooleanField(default = False, verbose_name = 'first_correct')
    correct_answer_second = models.BooleanField(default = False, verbose_name = 'second_correct')
    correct_answer_third = models.BooleanField(default = False, verbose_name = 'third_correct')
    correct_answer_fourth = models.BooleanField(default = False, verbose_name = 'fourth_correct')
    correct_answer_fifth = models.BooleanField(default = False, verbose_name = 'fifth_correct')
    
class Solution(models.Model):
    soultion_text = models.CharField(max_length = 500, verbose_name = 'Text')
    quiz_id = models.ForeignKey('Quiz', on_delete = models.CASCADE, verbose_name = 'Quiz_id')
    writer = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Writer')
    
class Solved_quiz(models.Model):
    question0_score = models.FloatField(default = 0, verbose_name = 'Score1')
    question1_score = models.FloatField(default = 0, verbose_name = 'Score2')
    question2_score = models.FloatField(default = 0, verbose_name = 'Score3')
    question3_score = models.FloatField(default = 0, verbose_name = 'Score4')
    question4_score = models.FloatField(default = 0, verbose_name = 'Score5')
    question5_score = models.FloatField(default = 0, verbose_name = 'Score6')
    question6_score = models.FloatField(default = 0, verbose_name = 'Score7')
    question7_score = models.FloatField(default = 0, verbose_name = 'Score8')
    question8_score = models.FloatField(default = 0, verbose_name = 'Score9')
    question9_score = models.FloatField(default = 0, verbose_name = 'Score10')
    quiz_id = models.ForeignKey('Quiz', on_delete = models.CASCADE, verbose_name = 'Quiz_id')
    solved_user = models.ForeignKey('User', on_delete = models.CASCADE, verbose_name = 'Solved_user')