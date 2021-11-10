from django.urls import path
from django.conf.urls import include, url

from rest_framework_simplejwt import views as jwt_views
from django.views.decorators.cache import cache_page
from graphene_django.views import GraphQLView
from django.views.generic.base import TemplateView


from .views import *

urlpatterns = [
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/student/detail/',StudentDetail.as_view(), name ='student_detail'),
    path('api/update_teacher/subject/<int:pk>',UpdateTeacherSubjectAPI.as_view(), name ='update_teacher_subject'),
    path('', StudentTeacherList.as_view(),  name ='student_teacher_list'),
    path('student/detail/<pk>/', StudentDetailView.as_view(),  name ='student_detail'),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('firebase-messaging-sw.js', (TemplateView.as_view(template_name="firebase-messaging-sw.js", content_type='application/javascript', )), name='service-worker.js'),
    path('manifest.json', (TemplateView.as_view(template_name="manifest.json", content_type='application/json', )), name='manifest.json'),

    path('say_hi/<int:entry_id>',transfer, name ='say_hi'),
    path('say_hi/',hello_world, name ='say_hi'),
    path('say_hi1/',AjaxView.as_view(), name ='say_hi1'),

    path('syntaxt/highlight/',syntaxt_highlight, name ='syntaxt_highlight'),
    path('ajax/syntaxt/highlight/',ajax_syntaxt_highlight, name ='ajax_syntaxt_highlight'),
]


