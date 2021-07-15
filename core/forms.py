from django import forms
from .models import HomeWorks, HomeWorkUpload


class TeacherFile(forms.ModelForm):
    class Meta:
        model = HomeWorks
        fields = ('file', 'title',)


class StudentFile(forms.ModelForm):
    class Meta:
        model = HomeWorkUpload
        fields = ('file',)