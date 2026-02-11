import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortColumn, setSortColumn] = useState(null);
  const [sortDirection, setSortDirection] = useState('asc');

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Fetching teams from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams API Response:', data);
        const teamsData = data.results || data;
        console.log('Processed teams data:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
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

  const getSortedTeams = () => {
    if (!sortColumn) return teams;

    return [...teams].sort((a, b) => {
      let aValue = a[sortColumn] || '';
      let bValue = b[sortColumn] || '';

      if (sortColumn === 'created_at') {
        aValue = new Date(aValue);
        bValue = new Date(bValue);
      } else if (typeof aValue === 'string') {
        aValue = aValue.toLowerCase();
        bValue = bValue.toLowerCase();
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
          <i className="bi bi-shield-fill-check me-2" style={{color: '#008037'}}></i>
          Teams
        </h1>
        <p className="text-muted mb-0">
          <i className="bi bi-people me-1"></i>
          Total teams: <strong>{teams.length}</strong>
        </p>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('id')}>
                ID <SortIcon column="id" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('name')}>
                Name <SortIcon column="name" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('description')}>
                Description <SortIcon column="description" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('created_at')}>
                Created At <SortIcon column="created_at" />
              </th>
            </tr>
          </thead>
          <tbody>
            {getSortedTeams().map(team => (
              <tr key={team.id}>
                <td>{team.id}</td>
                <td>
                  <strong>
                    <i className="bi bi-shield-fill-check me-2" style={{color: '#008037'}}></i>
                    {team.name}
                  </strong>
                </td>
                <td className="text-muted">{team.description || <span className="fst-italic">No description</span>}</td>
                <td>
                  <span className="badge bg-info text-dark">
                    <i className="bi bi-calendar-check me-1"></i>
                    {team.created_at ? new Date(team.created_at).toLocaleDateString() : '-'}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;
