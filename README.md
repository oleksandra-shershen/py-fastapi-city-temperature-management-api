# City Temperature Management API

This is a FastAPI application designed to manage city data and their corresponding temperature data. The application has two main components:

1. A CRUD (Create, Read, Update, Delete) API for managing city data.
2. An API that fetches current temperature data for all cities in the database and stores this data. It also provides an endpoint to retrieve the history of all temperature data.

## Features

- Create, read, update, and delete city data.
- Fetch and store current temperature data for all cities.
- Retrieve temperature history for all cities or for a specific city.

## Installation

1. *Clone the repository*
2. *Set enviroment variable:* 
- Copy and rename the .env.sample file to .env
- Open the .env file and edit the environment variables
- Save the .env file securely
- Make sure the .env file is in .gitignore

3. *Create and activate a virtual environment:*
On Windows:
```sh
python -m venv venv 
venv\Scripts\activate
```
On UNIX or macOS:
```sh
python3 -m venv venv 
source venv/bin/activate
```

4. *Install the dependencies:*
    ```sh
    pip install -r requirements.txt
    ```
5. *Run project:*
```sh
python uvicorn main:app --reload
```

Go to the site: http://localhost:8000/
