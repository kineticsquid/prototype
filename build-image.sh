#!/bin/bash
echo "Tagging and pushing docker image. Be sure to start docker.app first"
echo "To examine contents: 'docker run -it sudoku-main sh'"
echo "Need to be logged on first with 'bx login --sso'. "

docker rmi kineticsquid/prototype:latest
docker build --rm --no-cache --pull -t kineticsquid/prototype:latest -f Dockerfile .
docker push kineticsquid/prototype:latest

# list the current images
echo "Docker Images..."
docker images
