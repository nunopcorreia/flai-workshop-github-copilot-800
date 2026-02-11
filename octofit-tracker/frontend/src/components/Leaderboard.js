import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortColumn, setSortColumn] = useState('rank');
  const [sortDirection, setSortDirection] = useState('asc');

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Fetching leaderboard from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard API Response:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  const handleSort = (column) => {
    if (sortColumn === column) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortColumn(column);
      setSortDirection('asc');
    }
  };

  const getSortedLeaderboard = () => {
    if (!sortColumn) return leaderboard;

    return [...leaderboard].sort((a, b) => {
      let aValue = a[sortColumn];
      let bValue = b[sortColumn];

      if (sortColumn === 'rank' || sortColumn === 'total_points' || sortColumn === 'total_calories' || sortColumn === 'total_activities') {
        aValue = Number(aValue) || 0;
        bValue = Number(bValue) || 0;
      } else if (sortColumn === 'updated_at') {
        aValue = new Date(aValue || 0);
        bValue = new Date(bValue || 0);
      } else {
        aValue = (aValue || '').toString().toLowerCase();
        bValue = (bValue || '').toString().toLowerCase();
      }

      if (aValue < bValue) return sortDirection === 'asc' ? -1 : 1;
      if (aValue > bValue) return sortDirection === 'asc' ? 1 : -1;
      return 0;
    });
  };

  const SortIcon = ({ column }) => {
    if (sortColumn !== column) {
      return <i className="bi bi-arrow-down-up ms-1 text-muted" style={{fontSize: '0.8rem'}}></i>;
    }
    return sortDirection === 'asc' 
      ? <i className="bi bi-arrow-up ms-1"></i>
      : <i className="bi bi-arrow-down ms-1"></i>;
  };

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="loading-container">
          <div className="spinner-border" style={{color: '#008037'}} role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger d-flex align-items-center" role="alert">
          <i className="bi bi-exclamation-triangle-fill me-2"></i>
          <div>
            <strong>Error:</strong> {error}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h1 className="display-6">
          <i className="bi bi-trophy-fill me-2" style={{color: '#FFD700'}}></i>
          Leaderboard
        </h1>
        <p className="text-muted mb-0">
          <i className="bi bi-bar-chart-fill me-1"></i>
          Total entries: <strong>{leaderboard.length}</strong>
        </p>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('rank')}>
                Rank <SortIcon column="rank" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('user')}>
                User <SortIcon column="user" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('team')}>
                Team <SortIcon column="team" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('total_points')}>
                Total Points <SortIcon column="total_points" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('total_calories')}>
                Total Calories <SortIcon column="total_calories" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('total_activities')}>
                Total Activities <SortIcon column="total_activities" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('updated_at')}>
                Last Updated <SortIcon column="updated_at" />
              </th>
            </tr>
          </thead>
          <tbody>
            {getSortedLeaderboard().map((entry, index) => (
              <tr key={entry.id || index} className={entry.rank <= 3 ? 'table-active' : ''}>
                <td>
                  {entry.rank === 1 && <i className="bi bi-trophy-fill text-warning fs-4 me-2"></i>}
                  {entry.rank === 2 && <i className="bi bi-trophy-fill text-secondary fs-5 me-2"></i>}
                  {entry.rank === 3 && <i className="bi bi-trophy-fill text-danger fs-6 me-2"></i>}
                  <span className={`badge ${
                    entry.rank === 1 ? 'bg-warning text-dark' :
                    entry.rank === 2 ? 'bg-secondary' :
                    entry.rank === 3 ? 'bg-danger' : 'bg-light text-dark'
                  }`}>
                    #{entry.rank}
                  </span>
                </td>
                <td><strong>{entry.user}</strong></td>
                <td>
                  {entry.team ? (
                    <span className="badge bg-primary">{entry.team}</span>
                  ) : (
                    <span className="text-muted">-</span>
                  )}
                </td>
                <td><strong style={{color: '#008037'}}>{entry.total_points}</strong></td>
                <td>{entry.total_calories}</td>
                <td>
                  <span className="badge bg-info text-dark">{entry.total_activities}</span>
                </td>
                <td className="text-muted">{entry.updated_at ? new Date(entry.updated_at).toLocaleDateString() : '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
