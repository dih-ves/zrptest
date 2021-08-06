#!/bin/bash
app="mm.test"
docker build -t ${app} .
docker run -d -p 5003:80 \
  --name=${app} \
  -v $PWD:/app ${app}