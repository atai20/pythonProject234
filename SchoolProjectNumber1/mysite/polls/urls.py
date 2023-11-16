from django.urls import include, path

from . import views
app_name  = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:pk>/results2/", views.TestView.as_view(), name="test"),
    path("<int:pk>/results3", views.ChatView.as_view(), name="chat"),
    path("<int:pk>/results4", views.RegisterView.as_view(), name="register"),
    path("<int:pk>/results5", views.ForumsView.as_view(), name="forum"),
    path("__debug__/", include("debug_toolbar.urls")),
]


