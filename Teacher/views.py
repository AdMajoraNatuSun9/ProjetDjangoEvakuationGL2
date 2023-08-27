from django.shortcuts import render

# Create your views here.
def homeTeacher(request):

    return render(request, 'homeTeacher.html')