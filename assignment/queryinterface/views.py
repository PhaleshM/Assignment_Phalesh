# views.py
from rest_framework import generics
from logingestor.models import Log
from queryinterface.serializers import LogSerializer
from django.db.models import Q
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from asgiref.sync import async_to_sync

class LogListView(generics.ListAPIView):
    serializer_class = LogSerializer

    def get_queryset(self):
        queryset = Log.objects.all()

        # Filter by level
        level = self.request.query_params.get('level', None)
        if level:
            queryset = queryset.filter(level=level)

        # Filter by message
        message = self.request.query_params.get('message', None)
        if message:
            queryset = queryset.filter(message__icontains=message)

        # Filter by resourceId
        resource_id = self.request.query_params.get('resourceId', None)
        if resource_id:
            queryset = queryset.filter(resourceId=resource_id)

        # Filter by timestamp range
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%SZ')
            end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%SZ')
            queryset = queryset.filter(timestamp__range=[start_date, end_date])

        # Filter by metadata.parentResourceId
        parent_resource_id = self.request.query_params.get('parentResourceId', None)
        if parent_resource_id:
            queryset = queryset.filter(Q(parentResourceId=parent_resource_id) | Q(metadata__parentResourceId=parent_resource_id))

        return queryset

class HomeView(TemplateView):
    template_name = 'search.html'

class IndexView(TemplateView):
    template_name = 'index.html'

# from django.http import HttpResponse
# from django.views import View
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# import json
# from channels.layers import get_channel_layer


# @receiver(post_save, sender=Log)
# def log_post_save(sender, instance, **kwargs):
#     channel_layer = get_channel_layer()
#     logs = {
#         'level': instance.level,
#         'message': instance.message,
#         'resourceId': instance.resourceId,
#         'timestamp': instance.timestamp.isoformat(),
#         'traceId': instance.traceId,
#         'spanId': instance.spanId,
#         'commit': instance.commit,
#         'parentResourceId': instance.parentResourceId,
#     }
#     async_to_sync(channel_layer.group_send)(
#         'logs_group', {'type': 'send_logs', 'logs': logs}
#     )