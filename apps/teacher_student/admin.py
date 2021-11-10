from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django import forms
from .models import *


class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('user_type',)

class CustomUserChangeFrom(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserChangeFrom
    model = User
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('username', 'password','user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'user_type')}
        ),
    )

    search_fields = ('username',)
    ordering = ('username',)




class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','user']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','user']


admin.site.register(User, UserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(assignment)