import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Teams from './components/Teams';
import Activities from './components/Activities';
import Workouts from './components/Workouts';
import Leaderboard from './components/Leaderboard';

function Home() {
  return (
    <div className="container mt-5">
      {/* Sporting Championship Banner */}
      <div className="alert alert-success border-3 mb-4" style={{
        background: 'linear-gradient(135deg, #006633 0%, #008037 50%, #006633 100%)',
        color: 'white',
        borderColor: '#FFD700',
        boxShadow: '0 4px 15px rgba(255, 215, 0, 0.3)'
      }}>
        <div className="text-center py-3">
          <h2 className="display-5 fw-bold mb-3">
            <i className="bi bi-trophy-fill me-2" style={{color: '#FFD700', fontSize: '2.5rem'}}></i>
            🦁 SPORTING CLUBE DE PORTUGAL 🦁
            <i className="bi bi-trophy-fill ms-2" style={{color: '#FFD700', fontSize: '2.5rem'}}></i>
          </h2>
          <h3 className="fw-bold mb-3" style={{color: '#FFD700', textShadow: '2px 2px 4px rgba(0,0,0,0.3)'}}>
            CAMPEÃO NACIONAL 2024 & 2025
          </h3>
          <div className="d-flex justify-content-center align-items-center gap-4 mb-2">
            <div className="text-center">
              <i className="bi bi-star-fill" style={{color: '#FFD700', fontSize: '2rem'}}></i>
              <div className="fw-bold fs-4">2023-2024</div>
            </div>
            <div className="text-center">
              <i className="bi bi-plus-lg" style={{fontSize: '2rem', color: '#FFD700'}}></i>
            </div>
            <div className="text-center">
              <i className="bi bi-star-fill" style={{color: '#FFD700', fontSize: '2rem'}}></i>
              <div className="fw-bold fs-4">2024-2025</div>
            </div>
          </div>
          <p className="mt-3 mb-2 fs-5 fw-bold" style={{letterSpacing: '1px'}}>
            🏆 BICAMPEÃO CONSECUTIVO 🏆
          </p>
          <p className="mb-0 fst-italic">
            "Train like a champion, win like Sporting!"
          </p>
        </div>
      </div>

      <div className="jumbotron p-5 rounded-3 mb-5">
        <h1 className="display-4 fw-bold">
          <i className="bi bi-trophy-fill me-2" style={{color: '#FFD700'}}></i>
          OctoFit Tracker
        </h1>
        <p className="lead fs-4">Track your fitness journey with the spirit of champions!</p>
        <hr className="my-4" style={{borderColor: 'rgba(255,215,0,0.4)'}} />
        <p className="fs-5">
          <i className="bi bi-lightning-charge-fill me-2"></i>
          Train like a champion. Compete with passion. Achieve greatness.
        </p>
      </div>

      <div className="row g-4">
        <div className="col-md-6 col-lg-4">
          <Link to="/users" className="text-decoration-none">
            <div className="card h-100">
              <div className="card-body text-center">
                <i className="bi bi-people-fill" style={{fontSize: '3rem', color: '#008037'}}></i>
                <h5 className="card-title mt-3 fw-bold">Users</h5>
                <p className="card-text text-muted">View and manage user profiles</p>
                <span className="btn btn-primary btn-sm mt-2">
                  <i className="bi bi-arrow-right-circle me-1"></i>
                  Explore Users
                </span>
              </div>
            </div>
          </Link>
        </div>

        <div className="col-md-6 col-lg-4">
          <Link to="/teams" className="text-decoration-none">
            <div className="card h-100">
              <div className="card-body text-center">
                <i className="bi bi-shield-fill-check" style={{fontSize: '3rem', color: '#008037'}}></i>
                <h5 className="card-title mt-3 fw-bold">Teams</h5>
                <p className="card-text text-muted">Browse competitive teams</p>
                <span className="btn btn-success btn-sm mt-2">
                  <i className="bi bi-arrow-right-circle me-1"></i>
                  View Teams
                </span>
              </div>
            </div>
          </Link>
        </div>

        <div className="col-md-6 col-lg-4">
          <Link to="/activities" className="text-decoration-none">
            <div className="card h-100">
              <div className="card-body text-center">
                <i className="bi bi-activity" style={{fontSize: '3rem', color: '#008037'}}></i>
                <h5 className="card-title mt-3 fw-bold">Activities</h5>
                <p className="card-text text-muted">Track fitness activities</p>
                <span className="btn btn-primary btn-sm mt-2">
                  <i className="bi bi-arrow-right-circle me-1"></i>
                  See Activities
                </span>
              </div>
            </div>
          </Link>
        </div>

        <div className="col-md-6 col-lg-4">
          <Link to="/workouts" className="text-decoration-none">
            <div className="card h-100">
              <div className="card-body text-center">
                <i className="bi bi-heart-pulse-fill" style={{fontSize: '3rem', color: '#008037'}}></i>
                <h5 className="card-title mt-3 fw-bold">Workouts</h5>
                <p className="card-text text-muted">Discover workout plans</p>
                <span className="btn btn-success btn-sm mt-2">
                  <i className="bi bi-arrow-right-circle me-1"></i>
                  Browse Workouts
                </span>
              </div>
            </div>
          </Link>
        </div>

        <div className="col-md-6 col-lg-4">
          <Link to="/leaderboard" className="text-decoration-none">
            <div className="card h-100" style={{borderTopColor: '#FFD700'}}>
              <div className="card-body text-center">
                <i className="bi bi-trophy-fill" style={{fontSize: '3rem', color: '#FFD700'}}></i>
                <h5 className="card-title mt-3 fw-bold">Leaderboard</h5>
                <p className="card-text text-muted">Check top performers</p>
                <span className="btn btn-warning btn-sm mt-2">
                  <i className="bi bi-arrow-right-circle me-1"></i>
                  View Rankings
                </span>
              </div>
            </div>
          </Link>
        </div>

        <div className="col-md-6 col-lg-4">
          <div className="card h-100 bg-light" style={{borderTopColor: '#6c757d'}}>
            <div className="card-body text-center">
              <i className="bi bi-gear-fill text-secondary" style={{fontSize: '3rem'}}></i>
              <h5 className="card-title mt-3 fw-bold">More Coming Soon</h5>
              <p className="card-text text-muted">Additional features in development</p>
              <span className="btn btn-secondary btn-sm disabled mt-2">
                <i className="bi bi-hourglass-split me-1"></i>
                Stay Tuned
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <i className="bi bi-shield-fill-check me-2"></i>
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
