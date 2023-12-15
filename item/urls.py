from django.urls import path
from . import views

app_name = 'item'

from .views import export_user_activity_to_excel


urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/activate/', views.activate_ad, name='activate_ad'),  # Add this line for activation
    path('<int:pk>/deactivate/', views.deactivate_ad, name='deactivate_ad'),  # Add this line for deactivation
    path('export-user-activity/', export_user_activity_to_excel, name='export_user_activity_to_excel'),
]
