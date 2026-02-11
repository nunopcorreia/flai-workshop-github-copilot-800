import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortColumn, setSortColumn] = useState(null);
  const [sortDirection, setSortDirection] = useState('asc');

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Fetching workouts from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts API Response:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
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

  const getSortedWorkouts = () => {
    if (!sortColumn) return workouts;

    return [...workouts].sort((a, b) => {
      let aValue = a[sortColumn];
      let bValue = b[sortColumn];

      if (sortColumn === 'duration' || sortColumn === 'calories_estimate') {
        aValue = Number(aValue) || 0;
        bValue = Number(bValue) || 0;
      } else if (sortColumn === 'difficulty') {
        const difficultyOrder = { beginner: 1, intermediate: 2, advanced: 3 };
        aValue = difficultyOrder[aValue] || 0;
        bValue = difficultyOrder[bValue] || 0;
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
          <i className="bi bi-heart-pulse-fill me-2" style={{color: '#008037'}}></i>
          Workouts
        </h1>
        <p className="text-muted mb-0">
          <i className="bi bi-clipboard-data me-1"></i>
          Total workouts: <strong>{workouts.length}</strong>
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
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('difficulty')}>
                Difficulty <SortIcon column="difficulty" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('duration')}>
                Duration (min) <SortIcon column="duration" />
              </th>
              <th style={{cursor: 'pointer'}} onClick={() => handleSort('calories_estimate')}>
                Calories/Session <SortIcon column="calories_estimate" />
              </th>
            </tr>
          </thead>
          <tbody>
            {getSortedWorkouts().map(workout => (
              <tr key={workout.id}>
                <td>{workout.id}</td>
                <td><strong>{workout.name}</strong></td>
                <td className="text-muted">{workout.description || '-'}</td>
                <td>
                  <span className={`badge bg-${
                    workout.difficulty === 'beginner' ? 'success' :
                    workout.difficulty === 'intermediate' ? 'warning' :
                    workout.difficulty === 'advanced' ? 'danger' : 'secondary'
                  }`}>
                    {workout.difficulty === 'beginner' && <i className="bi bi-star-fill me-1"></i>}
                    {workout.difficulty === 'intermediate' && <i className="bi bi-star-fill me-1"></i>}
                    {workout.difficulty === 'advanced' && <i className="bi bi-star-fill me-1"></i>}
                    {workout.difficulty}
                  </span>
                </td>
                <td>{workout.duration} min</td>
                <td><strong style={{color: '#008037'}}>{workout.calories_estimate}</strong></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
