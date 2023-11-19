from django.db import models

class Log(models.Model):
    level = models.CharField(max_length=255)
    message = models.TextField()
    resourceId = models.CharField(max_length=255)
    timestamp = models.DateTimeField(db_index=True)  # Adding db_index for indexing    
    traceId = models.CharField(max_length=255)
    spanId = models.CharField(max_length=255)
    commit = models.CharField(max_length=255)
    parentResourceId = models.CharField(max_length=255, null=True, blank=True)
