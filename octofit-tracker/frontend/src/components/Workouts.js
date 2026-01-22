import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts component - Fetching from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        console.log('Workouts component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts component - Processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return <div className="container mt-4"><p>Loading workouts...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">💪 Workout Suggestions</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Workout Type</th>
              <th>Description</th>
              <th>Duration (min)</th>
              <th>Difficulty</th>
              <th>For User</th>
              <th>Created</th>
            </tr>
          </thead>
          <tbody>
            {workouts.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center">No workout suggestions found.</td>
              </tr>
            ) : (
              workouts.map(workout => (
                <tr key={workout.id}>
                  <td><strong>{workout.workout_type}</strong></td>
                  <td>{workout.description || 'N/A'}</td>
                  <td>{workout.duration}</td>
                  <td>
                    <span className={`badge ${workout.difficulty === 'Easy' ? 'bg-success' : workout.difficulty === 'Medium' ? 'bg-warning' : 'bg-danger'}`}>
                      {workout.difficulty}
                    </span>
                  </td>
                  <td>{workout.user_name || 'N/A'}</td>
                  <td>{new Date(workout.created_at).toLocaleDateString()}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
