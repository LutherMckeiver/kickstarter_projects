# Kickstarter Project

## Contributors:
- Andrew Baik,
- Luther McKeiver &
- Michael Sklepowich


## Quick Start
How to launch this application from your local machine:
```py
## clone the repository
git clone https://github.com/LutherMckeiver/kickstarter_projects.git

## Create a .env file in the root of repository with following environment variables defined
ALLOWED_HOSTS
SECRET_KEY
DB_NAME
DB_HOST
DB_USER
DEBUG
DB_HOST

## Setup all config from the Docker
docker-compose up --build &

## Enter the web application bash
docker exec -it kickstarter_web bash

## Seed data crom .csv to postgres container
python3 load.db.py

## Open the web browser with one of the following URLs
http://127.0.0.1:8000/
http://0.0.0.0:8000/
http://localhost:8000/
```

