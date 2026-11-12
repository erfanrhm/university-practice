# Python Backend Docker Project

## Description
A simple Python Flask backend
containerized using Docker.

## Build Docker Image

docker build -t python-backend .

## Run Container

docker run -d -p 8080:5000 --name python-container python-backend

## Check Running Container

docker ps

## Test Application

Open http://localhost:8080
