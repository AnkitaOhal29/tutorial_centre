from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.generic.list import ListView

from .models import Student
from .serializers import *


# Create your views here.


class StudentDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    def get(self, *args, **kwargs):
        try:
            if self.request.user.user_type == 'student':
                qs = Student.objects.get(user=self.request.user)
                data = self.serializer_class(qs).data
            else:
                data = {'meesage' : 'You are not student!'}
            return Response(data) 
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST) 


class UpdateTeacherSubjectAPI(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Teacher.objects.all()
    lookup_field = 'pk'


class UpdateTeacherSubjectAPI(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = UpdateTeacherSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():

            subjects = request.data.get('subject')
            subjects = [Subject.objects.get_or_create(name = subject)[0] for subject in subjects]
            instance.subjects.clear()
            instance.subjects.set(subjects)
            return Response({"message": "Teacher's subject successfully updated!"})

        else:
            return Response({"error": "failed", "details": serializer.errors})


class StudentTeacherList(ListView):
    model = Student
    queryset = Student.objects.all().order_by('id')
    template_name = "student_list.html"
    context_object_name = 'objects'