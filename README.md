# chaos-toolkit-for-webapp
using chaos toolkit for flask based web app

#### Clone the repo

#### Create the virtual environment

```sh
virtualenv env --python=python3
```

#### Run the app

To run the Flask app use the following commands from a terminal

```sh
source env/bin/activate
python app.py
```
To run the Chaos experiments use the following commands from a terminal

```sh
chaos run experiment.json
chaos --verbose run experiment.json # In verbose mode
```

#### Generating requirements.txt file

To generate requirements.txt use below command from within the virtual environment

```sh
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2
```

For example:

```sh
(env) admin@Karans-MacBook-Pro chaos-toolkit-for-webapp % pip3 freeze > requirements.txt
```
#### Docker commands

List of Docker commands to use

```sh
## Build the image
docker build -t chaos-toolkit-for-webapp
## Run the docker image
docker run -p 5002:5002 --name chaos-toolkit-for-webapp -d chaos-toolkit-for-webapp
```

```sh
## View all running containers
docker ps -a
## Docker stop the container
docker stop <container-id>
## Docker remove the image
docker rm <container-id>
## View logs
docker logs <container-id>
```


#### Reference links

* https://medium.com/proofdock/introduce-a-chaos-middleware-for-python-flask-simulate-disruptions-to-improve-resiliency-aa3aad25ecd2
* https://stackoverflow.com/questions/21070369/importerror-no-module-named-virtualenv
* https://joachim8675309.medium.com/jenkins-ci-pipeline-with-python-8bf1a0234ec3
* https://stackoverflow.com/questions/50916740/docker-command-not-found-in-local-jenkins-multi-branch-pipeline
* https://stackoverflow.com/questions/50916740/docker-command-not-found-in-local-jenkins-multi-branch-pipeline
* https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
* https://www.javacodemonk.com/flask-in-production-part-3-6f14a256
* https://www.youtube.com/watch?v=nfLO5ONVI6E&ab_channel=CloudBeesTV
