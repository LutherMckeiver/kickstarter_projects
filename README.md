# Kickstarter Project
Contributors:
Andrew
Luther
Micheal


# Setup all config from the Docker
docker-compose up --build &

# Enter the web application bash
docker exec -it kickstarter_web bash

# Seed data crom .csv to postgres container
python3 load.db.py