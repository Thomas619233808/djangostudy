from  django.urls import path

from . import views

urlpatterns = [
    path('others/', views.listorders)
]