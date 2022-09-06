from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('account/<int:pk>/', views.account, name='account'),
    path('logout/', views.logout_user, name='logout_user'),
]
