from django import forms
from .models import Student, Document

class AddQueryStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstName', 'lastName', 'group', 'course', 'email']

class GenerateDocument(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'student']
