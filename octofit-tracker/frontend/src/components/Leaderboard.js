import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Leaderboard component - Fetching from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        console.log('Leaderboard component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard component - Processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return <div className="container mt-4"><p>Loading leaderboard...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Rank</th>
            <th>User</th>
            <th>Total Points</th>
            <th>Total Activities</th>
            <th>Total Calories</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.length === 0 ? (
            <tr>
              <td colSpan="5">No leaderboard data found.</td>
            </tr>
          ) : (
            leaderboard.map((entry, index) => (
              <tr key={entry.user_id || index}>
                <td>{index + 1}</td>
                <td>{entry.user_name}</td>
                <td>{entry.total_points}</td>
                <td>{entry.total_activities}</td>
                <td>{entry.total_calories}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Leaderboard;
