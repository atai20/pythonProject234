from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from pyexpat.errors import messages

from .models import User
from polls.models import Question
from .forms import LoginForm, RegisterForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Profile


def model_form_upload(request):
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Profile()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


class DashboardView(FormView):

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            ques_obj = Question.objects
            content['question_text'] = ques_obj
            return render(request, 'core/dashboard.html', content)
        else:
            return redirect(reverse('login-view'))


class RegisterView(FormView):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class LoginView(FormView):

    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('dashboard-view'))
        content['form'] = LoginForm
        return render(request, 'core/login.html', content)

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.first().username, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + e
            return render_to_response('login.html', content)


class LogoutView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
