from django.urls import path
from .views.login import LoginFormView

from django.conf.urls import handler404
from django.conf.urls import handler500

app_name = 'general'

urlpatterns = [
    path('', LoginFormView.as_view(), name='ingresar'),
]

handler404 = 'general.views.error.handler404'
handler500 = 'general.views.error.handler500'