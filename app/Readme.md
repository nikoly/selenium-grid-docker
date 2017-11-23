# Example App

Based on Flask. Sample application to run in a Docker Container.

## Getting Started

Install Docker and build an image

    docker build -t app:1 .

where `app` is an image name and `1` is a tag.

If you run a command

    docker images

    REPOSITORY    TAG   IMAGE ID            CREATED             SIZE
    app           1     5d757b6c31b9        5 seconds ago       700MB

you can see that the image with the app was created.

This command will run the image in a Docker Container and start the app

    docker run -d -p 9000:80 app:1

    docker ps

    CONTAINER ID    IMAGE    COMMAND         CREATED        STATUS         PORTS                  NAMES
    345f085032cc    app:1    "python app.py" 46 seconds ago Up 44 seconds  0.0.0.0:9000->80/tcp   hypo

Now it's possible to reach the app at `http://localhost:9000`.
