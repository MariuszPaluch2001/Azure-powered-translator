# Azure powered translator

Simple google translator copy powered by Azure.

## Setup flask

Poopulate .env variables:
1. SECRET_KEY = ...
2. AZURE_KEY = ...
3. ENDPOINT = ...
4. LOCATION = ...
5. PATH_ENDPOINT = ...
6. IS_DEBUG = ...

## Run localy

Type following commends:

```console
virtualenv venv
```

```console
source venv/bin/activate
```

```console
pip install -r requirements.txt
```

```console
flask run
```

## Docker image run

Type following commends:

```console
docker build --tag flask-demo .
```

```console
docker run --detach --publish 5000:50505 flask-demo
```

## Deploy on azure

Tutorial for deploying flask app on azure is [here](https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app-for-app-service?tabs=web-app-flask)