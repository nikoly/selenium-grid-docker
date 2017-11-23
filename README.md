# Selenium Tests in Docker

UI Selenium tests can be executed using Docker tools. What does it give?

* Integrate user interface tests into your build pipeline.
    * Execute the tests on every version of your application that is not deployed yet.
    * Execute the tests before merging into the main branch which is going to deployed.
* Run your tests always in the same environment. That helps to have the tests stable.

## Getting Started

Asumption is that an application under test is managed by Git with Github, and Continuous Integration is managed by Jenkins with Pipeline. These tools are integrated with each other.

The tests are implemented using RobotFramework with Selenium Library.

The setup explained here are executed and tested on XOS.

## Install Docker

To install Docker please refer to this [link](https://docs.docker.com/engine/installation/) and read a little bit about it.

## Dockerfile for Test Project

To make a test project (any software project actually) ready for Docker a Dockerfile needs to be added

    testui/Dockerfile

The ubuntu based image built with the Dockerfile will contain a test project in a folder `frontend-integration-tests` and it's going to be a working directory.

To build the image execute

    docker build -t robottests:1

where `robottests` is image name and `1` is a tag.

## Dockerfile for App Project

See a README in `app/` to find out how to run the app. The app is there only as an example for running the Selenium tests.

## Run tests

`docker-compose` will be used to run the tests using the command

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