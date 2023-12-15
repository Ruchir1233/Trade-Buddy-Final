from django.contrib.auth import views as auth_views
# from django.urls import handler404, handler500
from core.views import custom_404_view # Import your custom error handling views

handler404 = custom_404_view
from django.urls import path
from django.conf.urls import handler404, handler500
from core import views
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('otp-verification/', views.otp_verification, name='otp_verification'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('export-user-activity/', views.export_user_activity_to_excel, name='export_user_activity_to_excel'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html'),)
]
# handler404 = 'core.views.handler404'