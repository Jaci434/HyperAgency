from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .models import Resume
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from .forms import HomeForm


# Create your views here.
class MainMenuPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'MainMenuPage.html')

class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'HomePage.html')


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class ResumesPage(View):
    def get(self, request, *args, **kwargs):
        context = {'resume': Resume.objects.all()}
        return render(request, 'ViewResumes.html', context)


class NewResumesPage(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = HomeForm()
        return render(request, "NewResume.html", context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            resume = Resume.objects.create(description=request.POST.get("description"), author_id=request.user.id)
            return redirect('/home/')
        else:
            raise PermissionDenied
