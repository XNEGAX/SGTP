from django.shortcuts import render
from django.template import RequestContext

def handler404(request, exception = None):
    """ Redirige el error 404 al template personalizado """
    return render(request,'error/404.html', status=404)

def handler500(request, exception = None):
    """ Redirige el error 500 al template personalizado """
    return render(request,'error/500.html', status=500)