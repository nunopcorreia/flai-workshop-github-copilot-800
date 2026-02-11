import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortColumn, setSortColumn] = useState(null);
  const [sortDirection, setSortDirection] = useState('asc');

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Fetching activities from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities API Response:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Processed activities data:', activitiesData);
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
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

  const getSortedActivities = () => {
    if (!sortColumn) return activities;

    return [...activities].sort((a, b) => {
      let aValue = a[sortColumn];
      let bValue = b[sortColumn];

      if (sortColumn === 'date') {
        aValue = new Date(aValue || 0);
        bValue = new Date(bValue || 0);
      } else if (sortColumn === 'duration' || sortColumn === 'distance' || sortColumn === 'calories_burned') {
        aValue = Number(aValue) || 0;
        bValue = Number(bValue) || 0;
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
          <i className="bi bi-activity me-2" style={{color: '#008037'}}></i>
          Activities
        </h1>
        <p className="text-muted mb-0">
          <i className="bi bi-graph-up me-1"></i>
          Total activities: <strong>{activities.length}</strong>
        </p>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('id')}>
                ID <SortIcon column="id" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('user')}>
                User <SortIcon column="user" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('activity_type')}>
                Activity Type <SortIcon column="activity_type" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('duration')}>
                Duration (min) <SortIcon column="duration" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('distance')}>
                Distance (km) <SortIcon column="distance" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('calories_burned')}>
                Calories <SortIcon column="calories_burned" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('date')}>
                Date <SortIcon column="date" />
              </th>
            </tr>
          </thead>
          <tbody>
            {getSortedActivities().map(activity => (
              <tr key={activity.id}>
                <td>{activity.id}</td>
                <td><strong>{activity.user}</strong></td>
                <td>
                  <span className={`badge ${
                    activity.activity_type === 'running' ? 'bg-danger' :
                    activity.activity_type === 'cycling' ? 'bg-primary' :
                    activity.activity_type === 'swimming' ? 'bg-info' :
                    activity.activity_type === 'walking' ? 'bg-success' :
                    activity.activity_type === 'yoga' ? 'bg-warning text-dark' :
                    activity.activity_type === 'strength' ? 'bg-dark' :
                    'bg-secondary'
                  }`}>
                    {activity.activity_type}
                  </span>
                </td>
                <td>{activity.duration} min</td>
                <td>{activity.distance ? `${activity.distance} km` : '-'}</td>
                <td><strong style={{color: '#008037'}}>{activity.calories_burned}</strong></td>
                <td className="text-muted">{activity.date ? new Date(activity.date).toLocaleDateString() : '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
