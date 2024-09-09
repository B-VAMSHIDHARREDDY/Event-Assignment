import React, { useState } from 'react';
import axios from 'axios';
import './CreateEvent.css'; // Import the CSS file

const CreateEvent: React.FC = () => {
  const [deviceId, setDeviceId] = useState('');
  const [timestamp, setTimestamp] = useState('');
  const [temperature, setTemperature] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      await axios.post('http://127.0.0.1:8000/v1/api/events/', {
        device_id: deviceId,
        timestamp: timestamp,
        temperature: temperature
      });
      alert("Event created successfully!");
    } catch (error) {
      console.error("Error creating event", error);
      alert("Failed to create event");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={() => document.getElementById('popup')?.classList.add('show')}>Create Event</button>
      <div id="popup" className="popup">
        <h2>Create New Event</h2>
        <label>
          Device ID:
          <input type="text" value={deviceId} onChange={e => setDeviceId(e.target.value)} />
        </label>
        <label>
          Timestamp:
          <input type="datetime-local" value={timestamp} onChange={e => setTimestamp(e.target.value)} />
        </label>
        <label>
          Temperature:
          <input type="number" value={temperature || ''} onChange={e => setTemperature(Number(e.target.value))} />
        </label>
        <button onClick={handleSubmit} disabled={loading}>Submit</button>
        <button onClick={() => document.getElementById('popup')?.classList.remove('show')}>Close</button>
      </div>
    </div>
  );
};

export default CreateEvent;
