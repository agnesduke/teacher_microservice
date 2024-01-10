

from django import forms
from django.forms import fields
from teacher_service.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

        