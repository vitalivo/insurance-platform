
from django.urls import path
from .views import ApplicationCreateView, ApplicationDetailView

app_name = 'applications'

urlpatterns = [
    path('create/', ApplicationCreateView.as_view(), name='application-create'),
    path('<str:application_number>/', ApplicationDetailView.as_view(), name='application-detail'),
]
