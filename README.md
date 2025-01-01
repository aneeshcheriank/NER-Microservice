[![Python application test with GitHub Actions](https://github.com/aneeshcheriank/NER-Microservice/actions/workflows/makefile.yml/badge.svg)](https://github.com/aneeshcheriank/NER-Microservice/actions/workflows/makefile.yml)
# NER-Microservice
NER microservice template

## Docker commands
- `docker build . -t <tag_name>`
- `docker image ls` # list the docker ids
- `docker run -p 127.0.0.1:8080:8080 <image_id>`
- to remove a docker image `docker rmi <image_id>`

## Curl command
- curl -X 'GET' \
  'https://ideal-broccoli-5vrjvx6745624vjp-8080.app.github.dev/ner/barak%20obama' \
  -H 'accept: application/json'
- need to change the host in this curl command

## Collect the output of the process on host machine
- -v option in docker run
- `-v /path/to/host/directory:/host_data`
- Mounts a host directory (/path/to/host/directory) into the container as /host_data to store the copied file.
- `docker run -p 127.0.0.1:8080:8080 -v ./output:/output <image_id>`
### command to run
- `docker build . -t latest`
- `docker run -p 127.0.0.1:8080:8080 -v ./output:/app/output latest`