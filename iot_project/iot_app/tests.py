import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from iot_app.services import EventService 
from iot_app.models import DeviceEvent  
from iot_project.settings import DB_SERVICE

class TestEventService(unittest.TestCase):

    def setUp(self):
        # Setup for the tests
        # self.db_url = DB_SERVICE 
        self.service = EventService(DB_SERVICE)

    @patch('iot_app.services.sessionmaker')
    def test_save_event(self, mock_sessionmaker):
        # Mock the session and engine
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session

        # Call the method to test
        self.service.save_event('device123', datetime(2023, 8, 8, 12, 0, 0), 25.5)

        # Assert that the session methods were called correctly
        self.assertTrue(mock_session().add.called)
        self.assertTrue(mock_session().commit.called)
        self.assertTrue(mock_session().close.called)

    @patch('iot_app.services.sessionmaker')
    def test_get_events(self, mock_sessionmaker):
        # Setup mock data
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session
        mock_session().query().filter().all.return_value = [
            DeviceEvent(device_id='device123', timestamp=datetime(2023, 8, 8, 12, 0, 0), temperature=25.5)
        ]

        # Call the method to test
        events = self.service.get_events('device123', datetime(2023, 8, 8), datetime(2023, 8, 9))

        # Assert the returned events are correct
        expected_events = [{
            "device_id": 'device123',
            "timestamp": '2023-08-08T12:00:00',
            "temperature": 25.5
        }]
        self.assertEqual(events, expected_events)

        # Assert session methods were called
        self.assertTrue(mock_session().query().filter().all.called)
        self.assertTrue(mock_session().close.called)

    @patch('iot_app.services.sessionmaker')
    def test_get_summary(self, mock_sessionmaker):
        # Setup mock data
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session
        mock_session().query().filter().all.return_value = [
            DeviceEvent(device_id='device123', timestamp=datetime(2023, 8, 8, 12, 0, 0), temperature=25.5),
            DeviceEvent(device_id='device123', timestamp=datetime(2023, 8, 8, 13, 0, 0), temperature=30.5),
            DeviceEvent(device_id='device123', timestamp=datetime(2023, 8, 8, 14, 0, 0), temperature=20.0)
        ]

        # Call the method to test
        summary = self.service.get_summary('device123', datetime(2023, 8, 8), datetime(2023, 8, 9))

        # Assert the returned summary is correct
        expected_summary = {"max": 30.5, "min": 20.0, "avg": 25.33}
        self.assertEqual(summary["max"], expected_summary["max"])
        self.assertEqual(summary["min"], expected_summary["min"])
        self.assertAlmostEqual(summary["avg"], expected_summary["avg"], places=2)

        # Assert session methods were called
        self.assertTrue(mock_session().query().filter().all.called)
        self.assertTrue(mock_session().close.called)

    @patch('iot_app.services.sessionmaker')
    def test_get_summary_no_events(self, mock_sessionmaker):
        # Setup mock data
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session
        mock_session().query().filter().all.return_value = []

        # Call the method to test
        summary = self.service.get_summary('device123', datetime(2023, 8, 8), datetime(2023, 8, 9))

        # Assert the returned summary is None for no events
        self.assertIsNone(summary)

        # Assert session methods were called
        self.assertTrue(mock_session().query().filter().all.called)
        self.assertTrue(mock_session().close.called)

if __name__ == '__main__':
    unittest.main()
