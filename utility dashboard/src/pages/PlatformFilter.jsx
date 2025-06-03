import React from 'react';
import { useState } from 'react';
import axios from 'axios';

function PlatformFilter() {
  const [platform, setPlatform] = useState('');
  const [reports, setReports] = useState([]);

  const handleFilter = () => {
    axios.get(`http://localhost:8000/machines/filter?platform=${platform}`)
      .then(res => setReports(res.data))
      .catch(err => console.error(err));
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Filter by Platform</h1>
      <input
        type="text"
        value={platform}
        onChange={e => setPlatform(e.target.value)}
        placeholder="e.g., Windows"
        className="border p-2 mr-2"
      />
      <button onClick={handleFilter} className="bg-blue-600 text-white px-4 py-2 rounded">Filter</button>
      {reports.length > 0 && (
        <table className="mt-4 min-w-full table-auto bg-white border border-gray-300">
          <thead>
            <tr>
              <th className="border p-2">Machine ID</th>
              <th className="border p-2">Platform</th>
              <th className="border p-2">Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {reports.map((r, idx) => (
              <tr key={idx}>
                <td className="border p-2">{r.machine_id}</td>
                <td className="border p-2">{r.platform}</td>
                <td className="border p-2">{r.timestamp}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default PlatformFilter;