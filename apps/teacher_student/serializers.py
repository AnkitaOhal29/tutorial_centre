from rest_framework import serializers
from .models import *




class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    def get_subjects(self,obj):
        return obj.subjects.all().values_list('name',flat=True)
    
    class Meta:
        model = Teacher
        fields = ['id','name','subjects']
        
class UpdateTeacherSerializer(serializers.ModelSerializer):
    subject = serializers.ListField()
    class Meta:
        model = Teacher
        fields = ['subject']



class StudentDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    username = serializers.SerializerMethodField()
    
    def get_username(self,obj):
        return obj.user.username
    class Meta:
        model = Student
        fields = ['id','student_name', 'username','teachers']


        