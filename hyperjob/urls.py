"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from resume.views import MainMenuPage, ResumesPage, MyLoginView, NewResumesPage, HomePage, logout_view
from vacancy.views import VacancyPage, MySignupView, NewVacancyPage
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [
    path('', MainMenuPage.as_view(), name='menu'),
    path('home/', HomePage.as_view()),
    path('resumes/', ResumesPage.as_view()),
    path('vacancies/', VacancyPage.as_view()),
    path('resume/new', NewResumesPage.as_view()),
    path('vacancy/new', NewVacancyPage.as_view()),
    path('admin/', admin.site.urls),

]
urlpatterns += [
    path('login', MyLoginView.as_view()),
    path('logout', logout_view),
    path('signup', MySignupView.as_view()),
]
