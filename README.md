api_stub
========

Files to get started with a basic REST API wrapped up into a Docker container.
THe Dockerfile creates a container running Ubuntu 14.04 with `python-dev`,
`pip`, and a few other things installed. Python dependencies are specified
in the `requirements.txt` file and installed into the container using `pip`.
The default behavior is to deploy the API on port 5000. 

The main portion to modify is lines 33-36 in `app.py` and perhaps the code for
the arguments in the `__init__` method.

**A note on filepaths:** If you need to access data files within the app, the
path should be something like `/src/datafile.dat`.

Docker
------

To build and run the Docker image:

```
docker build -t APP_NAME .
# Forward to port 5010. Pick any open port.
docker run -p "5000:5010" APP_NAME
```

