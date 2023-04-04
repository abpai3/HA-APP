# HA-APP
3 tier application with LB and DataBase 

## Docker env setup
1. install docker 
2. create a custom network using command - **docker network create app-network**
3. pull python:latest, nginx, postgres images from docker hub.

## Application
**webApp** folder consist of flask webapplication codes.  
**app.py** - Flask framework & application route.
**dbConnection.py** - DataBase connection module. 
**Dockerfile** - dockerfile to containerize the image.

once repository is pulled go inside webApp folder and execute below command to create new Docker image.
1. cd <path>/webApp 
2. docker build -t application:1.0 . 

If no issues after executing above command , docker image should list when **docker images | grep application** command executed. 
  

To start the docker application container:

  
primary instance :

  
docker run -d --name app-server-1 --app-network -p 8081:8080 application:1.0

  
secondary instance : 

  
docker run -d --name app-server-2 --app-network -p 8081:8080 application:1.0

run **docker ps** to see if both instance is running fine , can be accessed with localhost:8081 , localhost:8082
  

## NGINX 
1. **nginx** - folder consist of nginx.conf file with application server details with active and passive configuration.
  
how to run:
  
docker run -d --name lb -v <path>/nginx/nginx.conf:/etc/nginx/nginx.conf:ro -p 8080:80 <nginx image id>

check container is running or not by using **docker ps**, if you see container lb as running then access nginx with **localhost:8080**

  
localhost:8080/health - return status ok 
  

localhost:8080/getUsers - returns user details from postgres db.
  
## Postgres DataBase
run postgress image using below command 

**docker run -d --name postgres --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=app@12345 -e POSTGRES_DB=UserDetails -p 9000:5432 <postgres image id>**

