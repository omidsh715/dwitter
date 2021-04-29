from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('', views.timeline_view, name='timeline'),
    path('form/', views.form, name='form'),


]
