from django.shortcuts import render, redirect
from .models import Vacancy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import HomeForm

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

# Create your views here.
class VacancyPage(View):
    def get(self, request, *args, **kwargs):
        context = {'vacancy': Vacancy.objects.all()}
        return render(request, 'ViewVacancy.html', context)


class NewVacancyPage(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = HomeForm()
        return render(request, "NewResume.html", context)

    def post(self, request):
        user = request.user.is_staff
        if user:
            vacancy = Vacancy.objects.create(description=request.POST.get("description"), author_id=request.user.id)
            return redirect('/home/')
        else:
            return HttpResponse(status=403)


