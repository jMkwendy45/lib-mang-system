from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.playGround),
    path('hello/',views.helloWorld)

]
