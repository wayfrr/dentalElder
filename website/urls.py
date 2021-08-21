from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html',views.contact, name="contact"),
]

##Test Comment for GitHub
## Test Cooment 2