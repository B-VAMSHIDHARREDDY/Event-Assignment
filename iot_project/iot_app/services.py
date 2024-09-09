from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base,DeviceEvent

class EventService:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def save_event(self, device_id, timestamp, temperature):
        session = self.Session()
        event = DeviceEvent(device_id=device_id, timestamp=timestamp, temperature=temperature)
        session.add(event)
        session.commit()
        session.close()

    def get_events(self, device_id, start_date, end_date):
        session = self.Session()
        events = session.query(DeviceEvent).filter(
            DeviceEvent.device_id == device_id,
            DeviceEvent.timestamp >= start_date,
            DeviceEvent.timestamp <= end_date
        ).all()
        session.close()

        # Convert events to a list of dictionaries
        return [
            {
                "device_id": event.device_id,
                "timestamp": event.timestamp.isoformat(),  # Convert datetime to ISO format string
                "temperature": event.temperature
            }
            for event in events
        ]


    def get_summary(self, device_id, start_date, end_date):
        session = self.Session()
        events = session.query(DeviceEvent).filter(
            DeviceEvent.device_id == device_id,
            DeviceEvent.timestamp >= start_date,
            DeviceEvent.timestamp <= end_date
        ).all()

        if not events:
            session.close()
            return None

        max_temp = max(event.temperature for event in events)
        min_temp = min(event.temperature for event in events)
        avg_temp = sum(event.temperature for event in events) / len(events)

        session.close()
        return {"max": max_temp, "min": min_temp, "avg": avg_temp}
