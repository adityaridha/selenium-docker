# Simple Dockerize Selenium Script

Dependency
- Docker
- Remote Browser dan Webdriver (https://hub.docker.com/r/selenium/standalone-chrome)

How to setup

Setup remote browser/webdriver container

`docker run --network="test-network" -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome:3.141.59-20200525`

Create image from the script

`docker build -t test-py .`

Execute the script via created image

` docker run --name running-test --network="test-network" -e REM_DRIVER="http://172.18.0.2:4444/wd/hub" test-py `