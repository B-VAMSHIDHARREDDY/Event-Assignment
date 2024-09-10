from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import EventService
from datetime import datetime
from iot_project.settings import DB_SERVICE

class DeviceEventView(APIView):
    service = EventService(DB_SERVICE)

    def post(self, request):
        device_id = request.data.get('device_id')
        timestamp = request.data.get('timestamp')
        temperature = request.data.get('temperature')

        if not all([device_id, timestamp, temperature]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        timestamp = datetime.fromisoformat(timestamp)
        self.service.save_event(device_id, timestamp, temperature)

        return Response({"status": "Event recorded"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        device_id = request.query_params.get('device_id')
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')
        if not all([device_id, start_date_str, end_date_str]):
            events = self.service.get_all_events()
            return Response(events, status=status.HTTP_200_OK)
        start_date_str = start_date_str.strip()
        end_date_str = end_date_str.strip()
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            end_date = end_date.replace(hour=23, minute=59, second=59) 
        except ValueError as e:
            return Response({"error": f"Invalid date format: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        events = self.service.get_events(device_id, start_date, end_date)

        return Response(events, status=status.HTTP_200_OK)

class DeviceEventSummaryView(APIView):
    service = EventService(DB_SERVICE)

    def get(self, request):
        device_id = request.query_params.get('device_id')
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not all([device_id, start_date_str, end_date_str]):
            return Response({"error": "Missing required query parameters"}, status=status.HTTP_400_BAD_REQUEST)
        
    
        start_date_str = start_date_str.strip()
        end_date_str = end_date_str.strip()

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            end_date = end_date.replace(hour=23, minute=59, second=59)  
        except ValueError as e:
            return Response({"error": f"Invalid date format: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        summary = self.service.get_summary(device_id, start_date, end_date)

        if summary is None:
            return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(summary, status=status.HTTP_200_OK)

# class AllDeviceEventView(APIView):
#     def get(self,request):
#         return ""

