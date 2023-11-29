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
from django.views import generic

from .models import User
from .forms import LoginForm, RegisterForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Profile


from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm

# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
def model_form_upload(request):
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Profile()
    return render(request, 'core/model_form_upload.html', {
        'form': form, 'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username
    })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        p = Profile.objects.get(id=request.user.id)
        p.avatar = filename
        p.save()
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username
        })
    return render(request, 'core/simple_upload.html', {
            'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username
        })
def forum(request):
    return render(request, 'polls/forum.html', {'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username})


class DashboardView(FormView):

    template_name = "polls/register.html"
    model = User

class ChatView(generic.DetailView):
    template_name = "polls/chat_app.html"
    model = User

class ForumsView(generic.DetailView):
    template_name = "polls/forum.html"
    model = User


class RegisterView(FormView):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'polls/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        image = "polls/default.png"
        username = "noname"
        if (request.user.is_authenticated):
            image = Profile.objects.get(id = request.user.id)
            username = request.user.username


        return render(request, self.template_name, {'form': form, 'image': image, 'user_name' : username})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data.get('first_name'), form.cleaned_data.get('email'), form.cleaned_data.get('password1'))
            user.save()
        return render(request, self.template_name, {'form': form, 'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username})

def test(request):
    return render(request, 'polls/index2.html', {'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username})

class LoginView(FormView):

    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            return render(request, 'core/model_form_upload.html', content)
        content['form'] = LoginForm
        return render(request, 'polls/login.html', {'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username})

    def post(self, request):
        content = {}
        user = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=user, password=password)

            return redirect(to='polls/index2.html')
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + e
            return render_to_response('login.html', {'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username})


class LogoutView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
