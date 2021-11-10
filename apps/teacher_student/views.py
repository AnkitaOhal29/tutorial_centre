from rest_framework import generics
from rest_framework import status
from django.core.cache import cache
from rest_framework.response import Response
from django.views.generic import TemplateView

from rest_framework.permissions import IsAuthenticated
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render


from teacher_student.models import Student
from .serializers import *
from ._decorator import *
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


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

    
    def get_queryset(self):
        if cache.get('objects'):
            return cache.get('objects')
        else:
            data = self.queryset
            cache.set('objects', data)
            return data


class StudentDetailView(DetailView):
    # specify the model to use
    model = Student



class AjaxView(TemplateView):
  template_name = ''

  def get_context_data(self, **kwargs):
    return context

  @method_decorator(require_ajax)
  def dispatch(self, *args, **kwargs):
      return super(AjaxView, self).dispatch(*args, **kwargs)


def uppercase_decorator(function):
    def inner():
        import pdb;pdb.set_trace()
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return inner

@uppercase_decorator
def say_hi():
    return 'hello there'

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

def hello_decorator(func):
    def inner1(request):
         
        print("before Execution")
         
        # getting the returned value
        returned_value = func(request)
        print("after Execution")
         
        # returning the value to the original frame
        return returned_value
         
    return inner1


@hello_decorator
def sum_two_numbers(request):
    # import pdb;pdb.set_trace()
    print("Inside the function")

    return redirect('/')



def mydecorator():
    def wrap(view):
        def wrapper(request):
            print('Hello User')
            return view()
        return wrapper
    return wrap



@mydecorator()
def hello_world():
    print('hello world')
    return redirect('/')



a, b = 1, 2
# print("Sum =", sum_two_numbers(a, b))
print("-----------------------------------------------------")

say_whee()
print("-----------------------------------------------------")


@user_is_entry_author
def transfer(request, entry_id):
    print('test')
    return redirect('/')



def syntaxt_highlight(request):
    code = 'print("Hello World")'
    print(highlight(code, PythonLexer(), HtmlFormatter()))
    return render(request,'syntext_hightlight.html',{'data':highlight(code, PythonLexer(), HtmlFormatter()), 'style':HtmlFormatter().get_style_defs('.highlight')})

import re
from django.http import JsonResponse

def ajax_syntaxt_highlight(request):
    # import pdb;pdb.set_trace()
    data = request.GET.get('data')
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', data)
    code = cleantext
    # print(highlight(code, PythonLexer(), HtmlFormatter()))
    return JsonResponse({'data':highlight(code, PythonLexer(), HtmlFormatter()), 'style':HtmlFormatter().get_style_defs('.highlight')})