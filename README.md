# python-web-app-0001 - A Web Application Lab Environment

This project contains the necessary files to set up a lab environment for a web application using Docker and Docker Compose.

Specifically the environment is for building and deploying a Python web application with NGINX and PostgreSQL.

## Files

|File|Description|
|--|--|
|`Dockerfile.loadbalancer`|Dockerfile for the load balancer using NGINX.|
|`Dockerfile.appserver`|Dockerfile for the web application using Python FastAPI.|
|`Dockerfile.database`|Dockerfile for the database using PostgreSQL.|
|`docker-compose.yml`|Docker Compose file that creates a network and deploys each service as a container.|
|`nginx.conf`|NGINX configuration file for the load balancer.|
|`requirements.txt`|Requirements file for the Python web application.|
|`init.sql`|Initialization script for the database.|
|`Makefile`| Makefile to build each image and manage the Docker Compose stack.|
|`main.py`|FastAPI web application that serves the specified routes.|

## Usage

1. Build the Docker images using the provided Makefile:

        make build

2. Start the stack with Docker Compose:

        make start

3. Access the web application at http://localhost:9001.

4. Stop the stack with Docker Compose:

        make stop

Feel free to modify and customize the files as needed for your specific web application.