from django.urls import path
from mainapp.views import index, contact

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact')
]
