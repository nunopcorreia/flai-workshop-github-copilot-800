import React, { useState, useEffect } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Users component - Fetching from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        console.log('Users component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Users component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Users component - Processed data:', usersData);
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Users component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return <div className="container mt-4"><p>Loading users...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <div className="row">
        {users.length === 0 ? (
          <p>No users found.</p>
        ) : (
          users.map(user => (
            <div key={user.id} className="col-md-6 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{user.name}</h5>
                  <p className="card-text">
                    <strong>Email:</strong> {user.email}<br />
                    {user.team_name && <><strong>Team:</strong> {user.team_name}<br /></>}
                    {user.total_points !== undefined && <><strong>Points:</strong> {user.total_points}<br /></>}
                    <strong>Joined:</strong> {new Date(user.created_at).toLocaleDateString()}
                  </p>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Users;
