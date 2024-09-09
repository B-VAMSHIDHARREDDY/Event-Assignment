import React, { useState } from 'react';
import axios from 'axios';

interface Event {
  device_id: string;
  timestamp: string;
  temperature: number;
}

const GetEvents: React.FC = () => {
  const [events, setEvents] = useState<Event[]>([]);
  const [loading, setLoading] = useState(false);
  
  const fetchEvents = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://127.0.0.1:8000/v1/api/events/', {
        params: {
          device_id: 'device123',
          start_date: '2023-08-08',
          end_date: '2024-09-08'
        }
      });
      setEvents(response.data);
    } catch (error) {
      console.error("Error fetching events", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={fetchEvents}>Get Events</button>
      {loading && <p>Loading...</p>}
      <ul>
        {events.map((event, index) => (
          <li key={index}>
            Device: {event.device_id} | Timestamp: {event.timestamp} | Temperature: {event.temperature}°C
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GetEvents;
