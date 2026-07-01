from django.shortcuts import render

def dashboard_home(request):
    # This will render a basic template or just a placeholder message later
    return render(request, 'dashboard/dashboard.html', {
        'title': 'Admin Dashboard - Green Core Factory Systems'
    })