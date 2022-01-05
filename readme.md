### How to Build a Docker Image


Using docker build, we can now enlist Docker's help in building the image. You can combine the build command with other tags, such as the "--tag" flag, to specify the image name.

```
docker build --tag ohidurbappy/flask-docker .
```


### How to run an image as a container

Running an image inside a container is as simple as building one. But before we do so, we'd like to see what other images are available in our environment. To view images from the command line, execute the following:

```
docker images
```

If the above command finds any images, the output should look something like this:


```
REPOSITORY      TAG       IMAGE ID       CREATED             SIZE
python-docker   latest    cd52b70b361a   About an hour ago   912MB
headless-cms    latest    e8b253e230ee   43 hours ago        937MB
scrappy         latest    3e7ac0d44890   7 weeks ago         904MB
python          3.9.2     587b1bc803b3   7 months ago        885MB
```

Now we can choose which image to run. Using the docker run command, we can run an image by passing the image's name as a parameter.

```
docker run
```


While running the above command, you'll notice that on the command line it indicates that the application is running. But when you enter http://localhost:5000/ on the browser, the greeting will be:

This site can’t be reached localhost refused to connect.

Regardless of whether the container is running, it is doing so in isolation mode and cannot connect to localhost:5000.

The best solution is to run the image in detached mode. Because we need to view this application in the browser rather than the container, we'll modify our docker run and add two additional tags: "-d" to run it in detached mode and "-p" to specify the port to be exposed.

The docker run command will now be formatted as follows:

```
docker run -d -p 5000:5000 ohidurbappy/flask-docker
```


### Push it to registry


```
docker push ohidurbappy/flask-docker
```

```
docker login --username username

docker tag my-image username/my-repo

docker push username/my-repo
```