from rest_framework import viewsets, permissions, generics
from .models import Course, MyCourses
from .serializers import CourseSerializer, MyCoursesSerializer


# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(CourseView, self).get_permissions()


class MyCoursesView(generics.ListCreateAPIView):
    serializer_class = MyCoursesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MyCourses.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)