from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Placeholder path for dashboard home (we will build the view in views.py later)
    path('', views.dashboard_home, name='home'),
]