#!/bin/bash

# OctoFit Tracker API Testing Script for GitHub Codespaces
# This script tests all API endpoints using the codespace URL

echo "==================================="
echo "OctoFit Tracker API Testing"
echo "==================================="
echo ""

# Get codespace name from environment
CODESPACE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"

if [ -z "$CODESPACE_NAME" ]; then
    echo "Warning: CODESPACE_NAME not set, using localhost"
    CODESPACE_URL="http://localhost:8000"
fi

echo "Testing API at: $CODESPACE_URL"
echo ""

# Test API Root
echo "1. Testing API Root..."
echo "URL: ${CODESPACE_URL}/api/"
curl -s "${CODESPACE_URL}/api/" | python -m json.tool
echo ""
echo "-----------------------------------"

# Test Users endpoint
echo "2. Testing Users endpoint..."
echo "URL: ${CODESPACE_URL}/api/users/"
curl -s "${CODESPACE_URL}/api/users/" | python -m json.tool | head -40
echo ""
echo "-----------------------------------"

# Test Teams endpoint
echo "3. Testing Teams endpoint..."
echo "URL: ${CODESPACE_URL}/api/teams/"
curl -s "${CODESPACE_URL}/api/teams/" | python -m json.tool
echo ""
echo "-----------------------------------"

# Test Activities endpoint
echo "4. Testing Activities endpoint..."
echo "URL: ${CODESPACE_URL}/api/activities/"
curl -s "${CODESPACE_URL}/api/activities/" | python -m json.tool | head -40
echo ""
echo "-----------------------------------"

# Test Leaderboard endpoint
echo "5. Testing Leaderboard endpoint..."
echo "URL: ${CODESPACE_URL}/api/leaderboard/"
curl -s "${CODESPACE_URL}/api/leaderboard/" | python -m json.tool
echo ""
echo "-----------------------------------"

# Test Workouts endpoint
echo "6. Testing Workouts endpoint..."
echo "URL: ${CODESPACE_URL}/api/workouts/"
curl -s "${CODESPACE_URL}/api/workouts/" | python -m json.tool | head -40
echo ""
echo "-----------------------------------"

# Test single user endpoint
echo "7. Testing single user retrieval..."
USER_ID=$(curl -s "${CODESPACE_URL}/api/users/" | python -c "import sys, json; data=json.load(sys.stdin); print(data[0]['id'] if data else '')")
if [ ! -z "$USER_ID" ]; then
    echo "URL: ${CODESPACE_URL}/api/users/${USER_ID}/"
    curl -s "${CODESPACE_URL}/api/users/${USER_ID}/" | python -m json.tool
else
    echo "No users found"
fi
echo ""
echo "-----------------------------------"

echo ""
echo "==================================="
echo "API Testing Complete!"
echo "==================================="
echo ""
echo "All endpoints are accessible at:"
echo "  - API Root: ${CODESPACE_URL}/api/"
echo "  - Users: ${CODESPACE_URL}/api/users/"
echo "  - Teams: ${CODESPACE_URL}/api/teams/"
echo "  - Activities: ${CODESPACE_URL}/api/activities/"
echo "  - Leaderboard: ${CODESPACE_URL}/api/leaderboard/"
echo "  - Workouts: ${CODESPACE_URL}/api/workouts/"
echo ""
