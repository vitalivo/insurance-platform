
from django.urls import path
from .views import ApplicationCreateView, ApplicationDetailView, AdminApplicationListView, AdminApplicationUpdateView

app_name = 'applications'

urlpatterns = [
    path('create/', ApplicationCreateView.as_view(), name='application-create'),
    path('<str:application_number>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('', AdminApplicationListView.as_view(), name='application-list'),
    path('<int:pk>/', AdminApplicationUpdateView.as_view(), name='application-update'),
]
