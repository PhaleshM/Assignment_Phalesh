from django.urls import path
from .views import LogListView

urlpatterns = [
    path('interface/', LogListView.as_view(), name='log-list'),
]
