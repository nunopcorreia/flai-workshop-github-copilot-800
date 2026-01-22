import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Activities component - Fetching from:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        console.log('Activities component - Response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Activities component - Processed data:', activitiesData);
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Activities component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) return <div className="container mt-4"><p>Loading activities...</p></div>;
  if (error) return <div className="container mt-4"><p className="text-danger">Error: {error}</p></div>;

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <div className="row">
        {activities.length === 0 ? (
          <p>No activities found.</p>
        ) : (
          activities.map(activity => (
            <div key={activity.id} className="col-md-6 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{activity.activity_type}</h5>
                  <p className="card-text">
                    <strong>Duration:</strong> {activity.duration} minutes<br />
                    <strong>Distance:</strong> {activity.distance || 'N/A'} km<br />
                    <strong>Calories:</strong> {activity.calories_burned}<br />
                    <strong>Date:</strong> {new Date(activity.date).toLocaleDateString()}<br />
                    {activity.user_name && <><strong>User:</strong> {activity.user_name}</>}
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

export default Activities;
