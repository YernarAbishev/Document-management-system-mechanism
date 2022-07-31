from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddQueryStudent, GenerateDocument
from .models import Student, Document

def home(request):
    return render(request, "home.html")

def addQuery(request):
    if request.method == "POST":
        form = AddQueryStudent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddQueryStudent()
    return render(request, "add-query.html", {
        'form': form
    })

def studentsList(request):
    students = Student.objects.all().order_by('-queryDate')
    return render(request, "students-list.html", {
        'students': students
    })

def documentsList(request):
    documents = Document.objects.all().order_by('-queryDate')
    return render(request, "documents-list.html", {
        'documents': documents
    })

def documentDetail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "document-detail.html", {
        'student': student,
    })

