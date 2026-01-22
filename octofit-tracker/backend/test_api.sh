#!/bin/bash

echo "Testing OctoFit Tracker REST API Endpoints"
echo "=========================================="
echo ""

BASE_URL="http://localhost:8000"

echo "1. Testing API Root:"
curl -s "${BASE_URL}/api/" | python3 -m json.tool || echo "Failed to connect"
echo ""

echo "2. Testing Teams endpoint:"
curl -s "${BASE_URL}/api/teams/" | python3 -m json.tool | head -30
echo ""

echo "3. Testing Users endpoint:"
curl -s "${BASE_URL}/api/users/" | python3 -m json.tool | head -30
echo ""

echo "4. Testing Activities endpoint:"
curl -s "${BASE_URL}/api/activities/" | python3 -m json.tool | head -30
echo ""

echo "5. Testing Leaderboard endpoint:"
curl -s "${BASE_URL}/api/leaderboard/" | python3 -m json.tool
echo ""

echo "6. Testing Workouts endpoint:"
curl -s "${BASE_URL}/api/workouts/" | python3 -m json.tool | head -30
