from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from pyexpat.errors import messages
from django.views import generic
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Post
from django.utils import timezone
from .forms import PostForm

from users.models import Profile
def post_view(request):
    post_list = Post.objects.order_by("-id")[:5]
    return render(request, 'polls/forum.html', {'output':post_list, 'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username})
class CreateView(FormView):
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'polls/create_post.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        image = "polls/default.png"
        username = "noname"
        if (request.user.is_authenticated):
            image = Post.objects.all
            username = request.user.username
        return render(request, self.template_name, {'form': form, 'image': image, 'user_name' : username})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        p = Post(request.user, title = 'sdfsdf', content = 'sdfwefsdc', img = 'sdf', up_total = 12, down_total = 34, created = timezone.now(), updated = timezone.now())
        p.save()
        return render(request, self.template_name, {'form': form, 'image': Profile.objects.get(id = request.user.id), 'user_name' : request.user.username})




def create_post(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        p = Post(user = request.user, title = 'sdfsdf', content = 'sdfwefsdc', img = filename, up_total = 12, down_total = 34, created = timezone.now(), updated = timezone.now())
        p.save()


def post_view2(request):
    return render(request, 'polls/forum.html', {})

