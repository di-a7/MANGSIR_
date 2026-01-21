from django.urls import path
from .views import *

urlpatterns = [
   path('home/',home),
   path('about_us/',about_us),
   path('todolist/',todolist),
]
