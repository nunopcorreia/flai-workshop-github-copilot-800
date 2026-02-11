import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortColumn, setSortColumn] = useState(null);
  const [sortDirection, setSortDirection] = useState('asc');

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    console.log('Fetching users from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Users API Response:', data);
        const usersData = data.results || data;
        console.log('Processed users data:', usersData);
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
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

  const getSortedUsers = () => {
    if (!sortColumn) return users;

    return [...users].sort((a, b) => {
      let aValue = a[sortColumn] || '';
      let bValue = b[sortColumn] || '';

      if (typeof aValue === 'string') aValue = aValue.toLowerCase();
      if (typeof bValue === 'string') bValue = bValue.toLowerCase();

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
          <i className="bi bi-people-fill me-2" style={{color: '#008037'}}></i>
          Users
        </h1>
        <p className="text-muted mb-0">
          <i className="bi bi-person-badge me-1"></i>
          Total users: <strong>{users.length}</strong>
        </p>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('id')}>
                ID <SortIcon column="id" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('username')}>
                Username <SortIcon column="username" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('email')}>
                Email <SortIcon column="email" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('first_name')}>
                First Name <SortIcon column="first_name" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('last_name')}>
                Last Name <SortIcon column="last_name" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('team')}>
                Team <SortIcon column="team" />
              </th>
            </tr>
          </thead>
          <tbody>
            {getSortedUsers().map(user => (
              <tr key={user.id}>
                <td>
                  <span className="badge bg-secondary">
                    #{user.id}
                  </span>
                </td>
                <td>
                  <div className="d-flex align-items-center">
                    <i className="bi bi-person-circle me-2" style={{fontSize: '1.25rem', color: '#008037'}}></i>
                    <strong>{user.username}</strong>
                  </div>
                </td>
                <td>
                  <a href={`mailto:${user.email}`} className="text-decoration-none">
                    <i className="bi bi-envelope me-1"></i>
                    {user.email}
                  </a>
                </td>
                <td>
                  {user.first_name ? (
                    <span>
                      <i className="bi bi-person-badge me-1 text-info"></i>
                      {user.first_name}
                    </span>
                  ) : (
                    <span className="text-muted fst-italic">Not set</span>
                  )}
                </td>
                <td>
                  {user.last_name ? (
                    <span>
                      <i className="bi bi-person-badge me-1 text-info"></i>
                      {user.last_name}
                    </span>
                  ) : (
                    <span className="text-muted fst-italic">Not set</span>
                  )}
                </td>
                <td>
                  {user.team ? (
                    <span className="badge bg-primary">
                      <i className="bi bi-shield-fill me-1"></i>
                      {user.team}
                    </span>
                  ) : (
                    <span className="text-muted">No Team</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;
