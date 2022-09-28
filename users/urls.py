from django.urls import path
from users.views import Login

app_name = 'usuarios'

urlpatterns = [
    path('ingresar/', Login.as_view(), name='ingresar'),
]