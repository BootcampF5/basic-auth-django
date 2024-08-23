from django.urls import path, include
from rest_framework import routers
from .views import CourseView, MyCoursesView

router = routers.DefaultRouter()
router.register('courses', CourseView, 'courses')

urlpatterns = [
    path('', include(router.urls)),
    path('my_courses/', MyCoursesView.as_view(), name='my_courses')
]
