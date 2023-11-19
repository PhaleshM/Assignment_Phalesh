from rest_framework import generics
from .models import Log
from .serializers import LogSerializer

class LogCreateView(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
