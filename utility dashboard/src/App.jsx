import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Reports from './pages/Reports';
import PlatformFilter from './pages/PlatformFilter';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-gray-800 text-white p-4 flex justify-between">
          <div className="space-x-4">
            <Link to="/" className="hover:underline">Dashboard</Link>
            <Link to="/reports" className="hover:underline">Reports</Link>
            <Link to="/filter" className="hover:underline">Filter</Link>
          </div>
          <a href="http://localhost:8000/export/csv" className="hover:underline">Export CSV</a>
        </nav>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/filter" element={<PlatformFilter />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;