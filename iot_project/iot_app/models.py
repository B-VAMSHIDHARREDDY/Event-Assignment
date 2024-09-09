from django.db import models

# Create your models here.
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeviceEvent(Base):
    __tablename__ = 'device_events'

    id = Column(Integer, primary_key=True)
    device_id = Column(String, index=True)
    timestamp = Column(DateTime, index=True)
    temperature = Column(Float)

    def __repr__(self):
        return f"<DeviceEvent(device_id={self.device_id}, timestamp={self.timestamp}, temperature={self.temperature})>"
    
    def __str__(self):
        return f"{self.device_id} at {self.timestamp}: {self.temperature}°C"