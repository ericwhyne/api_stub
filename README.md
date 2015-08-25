api_stub
========

Files to get started with a basic REST API wrapped up into a Docker container.
THe Dockerfile creates a container running Ubuntu 14.04 with `python-dev`,
`pip`, and a few other things installed. Python dependencies are specified
in the `requirements.txt` file and installed into the container using `pip`.
The default behavior is to deploy the API on port 5000. 

The main portion to modify is lines 33-36 in `app.py` and perhaps the code for
the arguments in the `__init__` method.
