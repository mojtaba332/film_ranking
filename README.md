# Project jaar 1


## Installation
- Make sure you have docker AND docker compose installed (easiest way to do this is to install docker desktop - [Download Docker Desktop](https://www.docker.com/products/docker-desktop) )
- The docker folder of the installation contains the file: example.env.docker. Rename this file to **.env.docker** (filename starts with a dot!) and start your editor 
- Open .env.docker and edit the variable lines like "SERVER_ROOT_FOLDER" and "CLIENT_ROOT_FOLDER" to represent the paths of the folders of the server and client respectively. Make sure both folders exist and use the full path on your device (make sure there are quotes around the path) and use forward (/) slashes for folders. In this file you can also change ports for the services. 
- Start Docker Desktop app (if not already running!)
- Run the following command in the folder where your docker-compose.yml file is located: `docker compose --env-file=.env.docker up -d`
- Let the process finish setting up your environment
- Start coding!
-- your client is available on localhost (if you changed the variable "CLIENT_PORT_HTTP" make sure you put this after localhost - localhost:YOUR_PORT)

## Services
- Python flask server - python_server
- Nginx Webserver - client

Your client is accessed through [http://localhost](http://localhost) (unless you changed ports in the .env.docker file)
Your server is accessed through [http://localhost:5000](http://localhost:5000) (unless you changed ports in the .env.docker file)

## Important!
For docker to work you need to have enabled Virtualization in your BIOS (Windows users only). Find out how to do that [here](https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html)

This installation uses the following ports for it's services. these ports cannot be used by any other program. If you are experiencing troubles setting this up, you should check if these ports are unused. 

| Portnumber | used by? |
|---|---|
| 80 | Nginx (HTTP) |
| 443 | Nginx (HTTPS) |
| 5000 | Python/Flask |


## Useful commands for setting up or managing your docker environment
Make sure to run these commands in the folder where you cloned this repo!!!

|  Title | Description  | When to run?  |  Command |
|---|---|---|---|
| Up Command  | Run this command to pull & setup and run/start the containers/services/networks mentioned in the docker-compose.yml. | Run this when you want to start using this environment (you need to have docker & docker compose installed - install docker desktop for the easiest setup. | docker compose --env-file=.env.docker up -d |
| Down command | Stops and removes the containers started with the "up" command (previous command). | Run this when you want to stop using the containers and services (your data will be persisted still) OR when you want to setup a new/different environment. | docker compose --env-file=.env.docker down |
| Cleanup command | Removes stopped containers, unused networks, dangling images, and dangling build cache. && also removes all images not used by a container. | Run this when you have recently used a down command and you want to prevent docker from using stored cache to build new images. | docker image prune -a |
| Attach command | Attaches your current terminal to a container running in docker. This allows you to run commands in the container. | Run this when you want to run commands in a container. For example composer commands in the php container, node commands in the node container or mysqlcommands in the mysql container. {container_name} Should be changed to the name of the container you are trying to run the command in. 'sh' means shell command, you can also use 'bash' to use bash (bash might not work in all containers) | docker exec -it {container_name} sh |


## Example requests
More info and example requests: use Postman and import collection file from repo.

| Method | Endpoint | Description       |
|--------|--|-------------------|
| GET    | /init | (re)set database  |
| GET    | /films | get all films     |
| GET    | /film/<film_id> | get film by id    |
| DELETE | /film/delete/<film_id> | delete film by id |
| PUT    | /film/create | create film       |
| PUT    | /ranking/rank | create ranking |
| PUT    | /user/create | create user      |

