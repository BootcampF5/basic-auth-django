from rest_framework import serializers
from .models import Course, MyCourses


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class MyCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourses
        fields = ['course']
