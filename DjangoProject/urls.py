"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authenticate import views as authview
from Course import views
from Teacher import views as TeachView
from Student import views as StuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authview.LoginPage,name='login'),
    path('home/', authview.HomePage, name='home'),
    path('createTeacher/', views.create_Teacher, name='teacherCreation'),
    path('deleteTeacher/<int:id>', views.delete_teacher, name='teacherDelete'),
    path('updateTeacher/<int:id>', views.update_Teachers, name='teacherUpdate'),
    path('createStudent/', views.create_Student, name='studentCreation'),
    path('deleteStudent/<int:id>', views.delete_Student, name='studentDelete'),
    path('updateStudent/<int:id>', views.update_Student, name='studentUpdate'),
    path('createCourse/', views.create_course, name='courseCreation'),
    path('deleteCourse/<int:id>', views.delete_course, name='courseDelete'),
    path('updateCourse/<int:id>', views.update_course, name='courseUpdate'),
    path('homeTeacher/', TeachView.homeTeacher, name='teacherHome'),
    path('createProject/', TeachView.projet, name='projet'),
    path('listProject/', TeachView.liste, name='List'),
    path('homeStudent/', StuView.studentHome, name='studentHome')
]
