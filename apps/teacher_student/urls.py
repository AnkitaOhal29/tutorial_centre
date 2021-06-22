from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/student/detail/',StudentDetail.as_view(), name ='student_detail'),
    path('api/update_teacher/subject/<int:pk>',UpdateTeacherSubjectAPI.as_view(), name ='update_teacher_subject'),
    path('', StudentTeacherList.as_view(),  name ='student_teacher_list'),
]