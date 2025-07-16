# pip install "fastapi[standard]"
# pip install uvicorn
# Run the fastAPI application by running command : uvicorn main:app --reload (app here is the name of the fastAPI object)

from fastapi import FastAPI
from typing import Union # Union is used when a variable, function argument, or return value can be more than one type, it is used to enable type hints that accept multiple possible types.
from pydantic import BaseModel

# We use BaseModel because it allows us to define a class that:
# - Validates input data automatically
# - Enforces type constraints
# - Provides helpful error messages if data is invalid
# - Converts data into standard Python types (e.g., str, float)
# - Works seamlessly with FastAPI to handle request bodies (JSON → Python objects)


app = FastAPI()

class Item(BaseModel):
    id : int
    name : str
    price : float
    is_offer : Union[bool, None] = None

@app.get("/")
def read_home():
    return("Home Page")

@app.get("/items/{item_id}")
def read_item(item_id : int, q : Union[str, None] = None):
    return {"item_id" : item_id, "q" : q}

# q:                      → This declares a parameter named q.
# Union[str, None]       → This means that q can be either a string (str) or None.
# = None                 → This sets the default value of q to None, making it optional.

# How to call this get endpoint? -> http://localhost:8000/items/42?q=hello -> /items/42 → Path parameter item_id = 42 | ?q=hello → Query parameter q = "hello"

# view the swagger UI by going to http://localhost:8000/docs or http://localhost:8000/redoc

@app.put("/items/{item_id}")
def update_item(item_id : int, item : Item):
    return {"item_name" : item.name, "item_id" : item.id}


# Project setup

# create a project folder
# create backend and frontend folder within the project folder
# go into the backend folder, create a virtual environment and activate it
# now within the backend folder, create a "project.toml" file and a "Dockerfile" file 
# now install the libraries required for the FastAPI backend with the below given command in the virtual environment 
#     pip install "fastapi[all]" "motor[srv]" beanie aiostream
# fastapi[all] installs fastapi as well as uvicorn server
# motor[srv] installs the asynchronous python driver for mongoDB
# beanie is a mongoDB object document mapper
# aiostream allows us to work with async functions
# once these are installed we can generate the requirements.txt file by just running pip freeze > requirements.txt
# we'll put the necessary content in the Dockerfile which is like a text file that has all the commands needed to create a docker container of the backend
# pyproject.toml is a centralized configuration file for python projects
# for the project that we are creating here, we are only putting the testing configurations for pytest

# Create your mongoDB account, create a cluster, select the driver, while selecting the driver, you'll also find your mongoDB URI which you can copy and put in your .env file (in the root directory of the project) as an environment variable
# mongodb+srv://surajsharma13395:PEqZB1LzNb4vvWDg@cluster0.r4iivza.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
# After mongodb.net/ in the URI, mention the name of the database that you want to create

# create the docker compose file by creating compose.yaml file in the root directory, docker compose is used for running multi container docker applications

# create a folder by the name nginx in the root of the project and create a file named nginx.conf in it, nginx will be used to serve the frontend and the backend, the nginx container will act as the entry container and will route requests to frontend and backend accordingly

# create the react project in the frontend directory : npx create-react-app . (dot is for creating the project in the same directory in which we are in)

# npm install axios react-icons : to install axios (HTTP client) and react-icons (this has icons as react components)

# once all the coding is complete, start docker desktop and move into the root folder of the project and then run "docker-compose up --build", run the cmd with administrator priviliges if docker desktop requires it. This command builds the images before starting the containers. Once all the images are built, docker is going to create and start the container for each service




