from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Log

class LogAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_log_with_parent_resource_id_in_metadata(self):
        data = {
            "level": "error",
            "message": "Failed to connect to DB",
            "resourceId": "server-1234",
            "timestamp": "2023-09-15T08:00:00Z",
            "traceId": "abc-xyz-123",
            "spanId": "span-456",
            "commit": "5e5342f",
            "metadata": {
                "parentResourceId": "server-0987"
            }
        }

        response = self.client.post('http://127.0.0.1:8000/log/ingest/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Log.objects.count(), 1)
        log = Log.objects.get()
        self.assertEqual(log.parentResourceId, "server-0987")

    def test_create_log_without_metadata(self):
        data = {
            "level": "error",
            "message": "Failed to connect to DB",
            "resourceId": "server-1234",
            "timestamp": "2023-09-15T08:00:00Z",
            "traceId": "abc-xyz-123",
            "spanId": "span-456",
            "commit": "5e5342f"
        }

        response = self.client.post('http://127.0.0.1:8000/log/ingest/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Log.objects.count(), 1)
        log = Log.objects.get()
        self.assertIsNone(log.parentResourceId)

    def test_create_log_with_empty_metadata(self):
        data = {
            "level": "error",
            "message": "Failed to connect to DB",
            "resourceId": "server-1234",
            "timestamp": "2023-09-15T08:00:00Z",
            "traceId": "abc-xyz-123",
            "spanId": "span-456",
            "commit": "5e5342f",
            "metadata": {}
        }

        response = self.client.post('http://127.0.0.1:8000/log/ingest/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Log.objects.count(), 1)
        log = Log.objects.get()
        self.assertIsNone(log.parentResourceId)

    def test_create_log_with_invalid_metadata(self):
        data = {
            "level": "error",
            "message": "Failed to connect to DB",
            "resourceId": "server-1234",
            "timestamp": "2023-09-15T08:00:00Z",
            "traceId": "abc-xyz-123",
            "spanId": "span-456",
            "commit": "5e5342f",
            "metadata": "invalid_metadata"
        }

        response = self.client.post('http://127.0.0.1:8000/log/ingest/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Log.objects.count(), 0)
