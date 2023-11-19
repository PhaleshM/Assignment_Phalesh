from django.urls import path
from .views import LogCreateView

urlpatterns = [
    path('ingest/', LogCreateView.as_view(), name='log-ingest'),
]
