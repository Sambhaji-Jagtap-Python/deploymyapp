from django.shortcuts import render


def welcome_page(req):
    msg = 'Welcome to my First Application deployed on PythonAnywhere...!!!'
    return render(req, 'welcome.html', context={'msg': msg})