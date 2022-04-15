# Memgraph Console Query Application

## Description

This is simple Console Query Application that allows you to execute Cypher queries from your browser and the
results will be returned and displayed in a readable format.

## Running the application

### Prerequisites

[Docker](https://docs.docker.com/get-docker/)

[Docker Compose](https://docs.docker.com/compose/install/)

### Build and Run

Docker Compose will start both Console Query Application and Memgraph Platform which includes Memgraph DB.

1. Run `docker-compose build`
2. Run `docker-compose up -d`
3. Go to `http://localhost:3001` for console query application

Database is loaded with small intial dataset. You can test application with following query that will return all persons in database with restaurants at which they like to eat.
```
MATCH (r:Restaurant)<-[:ATE_AT]-(p:Person)
RETURN p.name AS person, r.name AS restaurant;
```
If you want to load additional datasets you can load sample datasets on [Memgraph Lab](https://memgraph.com/lab) at `http://localhost:3000/`.

### Testing backend

To run backend tests run `docker-compose exec backend python -m pytest "src/tests"` while application is running.
