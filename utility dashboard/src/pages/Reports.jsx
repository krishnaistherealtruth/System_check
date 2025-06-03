import React from 'react';
import { useEffect, useState } from 'react';
import axios from 'axios';

function Reports() {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/machines')
      .then(response => setReports(response.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">All Reports</h1>
      <table className="min-w-full table-auto bg-white border border-gray-300">
        <thead>
          <tr>
            <th className="border p-2">Machine ID</th>
            <th className="border p-2">Platform</th>
            <th className="border p-2">Disk Encryption</th>
            <th className="border p-2">OS Update</th>
            <th className="border p-2">Antivirus</th>
            <th className="border p-2">Sleep Setting</th>
            <th className="border p-2">Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {reports.map((report, idx) => (
            <tr key={idx} className="text-sm text-gray-700">
              <td className="border p-2">{report.machine_id}</td>
              <td className="border p-2">{report.platform}</td>
              <td className="border p-2">{report.disk_encryption}</td>
              <td className="border p-2">{report.os_update_status}</td>
              <td className="border p-2">{report.antivirus_status}</td>
              <td className="border p-2">{report.sleep_setting_status}</td>
              <td className="border p-2">{report.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Reports;