# Selenium Tests with Docker Compose

UI Selenium tests can be executed using Docker tools and one of the benefits to do so are:

* Integrate user interface tests into your build pipeline.

  * Execute the tests on every version of your application that is not deployed yet.
  * Execute selenium tests before merging the code into the main branch.
* Run your tests always in the same environment locally or remotely.
* Remove an overhead of dependencies installation for running the selenium tests on your local or remote machines.

## Getting Started

The tests are implemented using [RobotFramework with SeleniumLibrary](http://robotframework.org/SeleniumLibrary/).

This setup is created from the perspective and a need to execute the Selenium tests using [Jenkins Pipeline](https://jenkins.io/doc/book/pipeline/).

The explained here setup was executed and tested on XOS.

### Install Docker

To install Docker please refer to this [link](https://docs.docker.com/engine/installation/) and read a little bit about it.

### Create A Dockerfile For The Project With Tests

To make a test project (any software project actually) ready for Docker one has to add a Dockerfile to that project.

    testui/Dockerfile

The Ubuntu based image built with the Dockerfile will contain Selenium tests in a folder `frontend-integration-tests` of the image, and the folder is going to be a work directory.

To build the image execute

    docker build -t robottests:1 .

where `robottests` is an image name and `1` is a tag. "." means that the Dockerfile is in a current directory.

Also, there is an **entrypoint** to that image. The entry point is a `wait-for-it.sh` that will wait for a given container to be up before executing the following command. In this case, it's necessary to wait for selenium hub to be ready before executing the tests.

Usage:

    wait-for-it.sh -t 15 chromenode:5555

### Create The Dockerfile For The Demo App

See a README in `app/` to find out how to run the app. The app is there only to test it with Selenium tests.

## Run Selenium Tests

Use `docker-compose` command to run the setup.

    docker-compose -p my_unique_project up -d --build

The command will build, create and run Docker containers as specified in the docker-compose file.

To run the tests, please, execute one-off command in `robottests` container:

    docker-compose -p my_unique_project exec robottests ./wait-for-it.sh -t 15 selenium_hub:4444 -- robot -d reports  --variablefile variables/config.py  --variable BROWSER:chrome tests/

Clean the environment

    docker-compose -p my_unique_project down

`docker-compose` uses `docker-compose.yaml` that contains a description of images and other things. Amongst other things worth to mention

1. Volume

    ```yaml
        volumes:

        - ./reports:/frontend-integration-tests/reports
    ```

    `./reports` is in a current directory where you run docker-compose.

    When the tests are executed with docker-compose, the report will be saved inside a container where they run. A volume is needed to pass the reports outside the container, for example to your local machine.

2. Network

    ```yaml
        networks:
            robottestsnw:
                driver: bridge
    ```

    The network is needed to avoid various conflicts (e.g., ports). So called `user defined network` allows to run the containers in an isolated network environment.

3. Container name

    That is important and recommended to have a unique container name for managing convenience.

    ```yaml
        robottests:
            container_name: this_robottests
            command: /bin/sleep infinity
    ```

4. Project name

    Specify an alternate project name.

        docker-compose -p **my_project** up

    If the project name is specified, it's possible to run several the same docker-compose setups on the same environment. You can imagine when a few pull requests to the same projects are made at the same time.

5. Wait not only that Selenium Grid is up but also that it's ready.

    Before executing the Selenium tests, it's necessary to make sure that the test runner can create a Selenium Grid Session with a given webdriver. It means that Selenium Grid or Selenium Chrome Node should be **up** and **ready**.

    `wait-for-it.sh` script provides you with an opportunity to wait for the service to be up but not ready. To find out if the service is ready, please, check [this](wait-for-it.sh) out.
