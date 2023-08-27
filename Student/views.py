from django.shortcuts import render

# Create your views here.
def studentHome(request):

    return render(request, 'homeStudent.html')

def soumission(request):
    return True