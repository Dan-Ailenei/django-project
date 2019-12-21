from django.shortcuts import render


def index(request):
    return render(request, '{{cookiecutter.app_name}}/index.html', {})
