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
      <h2>Workout Suggestions</h2>
      <div className="row">
        {workouts.length === 0 ? (
          <p>No workout suggestions found.</p>
        ) : (
          workouts.map(workout => (
            <div key={workout.id} className="col-md-6 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{workout.workout_type}</h5>
                  <p className="card-text">
                    {workout.description && <>{workout.description}<br /></>}
                    <strong>Duration:</strong> {workout.duration} minutes<br />
                    <strong>Difficulty:</strong> {workout.difficulty}<br />
                    {workout.user_name && <><strong>For:</strong> {workout.user_name}<br /></>}
                    <strong>Created:</strong> {new Date(workout.created_at).toLocaleDateString()}
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

export default Workouts;
