import { useState } from 'react';

function ScheduleScanForm({ onSubmit }) {
  const [scanName, setScanName] = useState('');
  const [scanDescription, setScanDescription] = useState('');
  const [scanFrequency, setScanFrequency] = useState('');
  const [scanDuration, setScanDuration] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit({ scanName, scanDescription, scanFrequency, scanDuration });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Scan Name:
        <input
          type="text"
          value={scanName}
          onChange={(event) => setScanName(event.target.value)}
        />
      </label>
      <label>
        Scan Description:
        <textarea
          value={scanDescription}
          onChange={(event) => setScanDescription(event.target.value)}
        />
      </label>
      <label>
        Scan Frequency:
        <select value={scanFrequency} onChange={(event) => setScanFrequency(event.target.value)}>
          <option value="daily">Daily</option>
          <option value="weekly">Weekly</option>
          <option value="monthly">Monthly</option>
        </select>
      </label>
      <label>
        Scan Duration (in minutes):
        <input
          type="number"
          value={scanDuration}
          onChange={(event) => setScanDuration(event.target.value)}
        />
      </label>
      <button type="submit">Schedule Scan</button>
    </form>
  );
}
