from rest_framework import serializers
from .models import User, Quiz, Question, Solution, Solved_quiz

class UserSerializer(serializers.HyperlinkedModelSerializer):
    pass