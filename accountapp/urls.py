from django.urls.conf import path
from . import views

app_name ='accountapp'

urlpatterns = [
    path('hello_world/', views.hello_world)
]