# Selenium Tests in Docker

UI Selenium tests can be executed using Docker tools. What does it give?

* Integrate user interface tests into your build pipeline.
    * Execute the tests on every version of your application that is not deployed yet.
    * Execute the tests before merging into the main branch which is going to be deployed.
* Run your tests always in the same environment. That helps to have the tests stable.

## Getting Started

The tests are implemented using RobotFramework with SeleniumLibrary.

The setup explained here is executed and tested on XOS.

## Install Docker

To install Docker please refer to this [link](https://docs.docker.com/engine/installation/) and read a little bit about it.

## Dockerfile for Test Project

To make a test project (any software project actually) ready for Docker one has to add a Dockerfile to that project.

    testui/Dockerfile

The ubuntu based image built with the Dockerfile will contain a test project in the image folder `frontend-integration-tests` and it's going to be a working directory.

To build the image execute

    docker build -t robottests:1

where `robottests` is image name and `1` is a tag.

Also, there is an **entrypoint** to that image. The enry point is a `wait-for-it.sh` script that will wait for a given container to be up before executing the following command. In this case it's necessary to wait for selenium hub to be ready before executing the tests.

## Dockerfile for App Project

See a README in `app/` to find out how to run the app. The app is there only as an example for running the Selenium tests.

## Run tests

`docker-compose` will be used to run the tests using the command

    docker-compose up -d --build

also it's posible one-off command in a given container

    docker-compose run robottests robot -d reports  --variablefile variables/config.py  --variable BROWSER:chrome tests/

`docker-compose` uses `docker-compose.yaml` where images and other things are described. Amongst other things worth to mention

1. Volume

```yaml
    volumes:

      - {WORKSPACE}/reports:/frontend-integration-tests/reports
```

where `{WORKSPACE}` is a path to the directory where the reports should be stored.

When the tests are executed with the Docker, the report will be saved inside a container where they run. A volume is needed to pass the reports outside the container.

2. Network

```yaml
    networks:
        robottestsnw:
            driver: bridge
```

Network is needed to avoid various conflicts (e.g., ports). So called `user defined network` allows to run the containers in an isolated network environment.

3. Container name

It's important and recommended to have a unique container name.

```yaml
    robottests:
        container_name: robottests
        command: /bin/sleep infinity
```
