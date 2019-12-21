from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "{{ cookiecutter.project_name }}_auth"

urlpatterns = [
    path('login',
          LoginView.as_view(redirect_authenticated_user=True,
                           template_name="{{ cookiecutter.project_name }}_auth/login.html"),
          name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
