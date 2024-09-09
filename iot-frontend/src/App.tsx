import React from 'react';
import GetEvents from './components/GetEvents';
import SummaryReport from './components/SummaryReport';
import CreateEvent from './components/CreateEvent';

const App: React.FC = () => {
  return (
    <div>
      <h1>IoT Device Event Manager</h1>
      <GetEvents />
      <SummaryReport />
      <CreateEvent />
    </div>
  );
};

export default App;
