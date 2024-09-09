import React, { useState } from 'react';
import axios from 'axios';

interface Summary {
  total_events: number;
  average_temperature: number;
}

const SummaryReport: React.FC = () => {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [loading, setLoading] = useState(false);

  const fetchSummary = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://127.0.0.1:8000/v1/api/events/summary/', {
        params: {
          device_id: 'device123',
          start_date: '2023-08-08',
          end_date: '2024-09-08'
        }
      });
      console.log(response.data)
      setSummary(response.data);
    } catch (error) {
      console.error("Error fetching summary", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={fetchSummary}>Get Summary</button>
      {loading && <p>Loading...</p>}
      {summary && (
        <div>
          <p>Total Events: {summary.total_events}</p>
          <p>Average Temperature: {summary.average_temperature}°C</p>
        </div>
      )}
    </div>
  );
};

export default SummaryReport;
