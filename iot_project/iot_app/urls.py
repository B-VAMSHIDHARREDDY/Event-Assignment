from django.urls import path
from .views import DeviceEventView, DeviceEventSummaryView

urlpatterns = [
    path('events/', DeviceEventView.as_view(), name='device_events'),
    path('all/events/', DeviceEventView.as_view(), name='device_all_events'),
    path('events/summary/', DeviceEventSummaryView.as_view(), name='device_events_summary'),
]
