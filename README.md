
# FAST_API TodoList App

Welcome to the fast_api  Website project! This project offers the crud operations of todo list app with user authorization


## Demo

https://todo-autorization-f9i7frwh5-mulahimcoders-projects.vercel.app/docs


## Tech Stack

**Client:** fastapi, uvicorn, pymongo, PyJWT, bcrypt, python-dotenv




## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file


- `SECRET_KEY`: The secret key used for encoding JWT tokens.
- `ALGORITHM`: The algorithm used for encoding JWT tokens. 
- `MONGO_URL`: The url of your mongodb database.


## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/todo-app-api.git
    cd todo-app-api
    ```

2. **Install dependencies:**

    ```bash
    python -m venv venv
    ```
    ```bash
    . venv/Scripts/activate
    ```
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    uvicorn main:app --reload
    ```


# Api reference

## User Endpoints

### Welcome Message

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a welcome message.

    ```json
    {
        "message": "Welcome to our todo app"
    }
    ```

### Sign Up

- **URL:** `/signup`
- **Method:** `POST`
- **Tags:** `user-routes`
- **Description:** Registers a new user.

    **Request Body:**

    ```json
    {
        "name": "string",
        "email": "string",
        "password": "string"
    }
    ```

    **Response:**

    ```json
    {
        "success": true,
        "message": "Successfully Signup",
        "user": {
            "name": "string",
            "email": "string"
        }
    }
    ```

### Login

- **URL:** `/login`
- **Method:** `POST`
- **Tags:** `user-routes`
- **Description:** Logs in a user and returns a JWT token.

    **Request Body:**

    ```json
    {
        "email": "string",
        "password": "string"
    }
    ```

    **Response:**

    ```json
    {
        "access_token": "string",
        "token_type": "bearer"
    }
    ```

## Todo Endpoints

### Add Todo

- **URL:** `/add-todo`
- **Method:** `POST`
- **Tags:** `todo-routes`
- **Description:** Adds a new todo item.

    **Request Body:**

    ```json
    {
        "title": "string",
        "description": "string"
    }
    ```

    **Response:**

    ```json
    {
        "success": true,
        "message": "Todo item added successfully"
    }
    ```

### Get Todos

- **URL:** `/get_todos`
- **Method:** `GET`
- **Tags:** `todo-routes`
- **Description:** Returns all todo items for the authenticated user.

    **Response:**

    ```json
    {
        "success": true,
        "todos": [...]
    }
    ```

### Get One Todo

- **URL:** `/get_todo/{id}`
- **Method:** `GET`
- **Tags:** `todo-routes`
- **Description:** Returns a specific todo item by its ID.

    **Response:**

    ```json
    {
        "success": true,
        "todo": {...}
    }
    ```

### Update Todo

- **URL:** `/update-todo/{id}`
- **Method:** `PUT`
- **Tags:** `todo-routes`
- **Description:** Updates a specific todo item by its ID.

    **Request Body:**

    ```json
    {
        "title": "string",
        "description": "string"
    }
    ```

    **Response:**

    ```json
    {
        "success": true,
        "message": "Todo item updated successfully"
    }
    ```

### Update Complete Status

- **URL:** `/update-complete/{id}`
- **Method:** `PATCH`
- **Tags:** `todo-routes`
- **Description:** Updates the complete status of a specific todo item by its ID.

    **Request Body:**

    ```json
    {
        "complete": true/false
    }
    ```

    **Response:**

    ```json
    {
        "success": true,
        "message": "Todo item status updated successfully"
    }
    ```

### Delete Todo

- **URL:** `/delete-todo/{id}`
- **Method:** `DELETE`
- **Tags:** `todo-routes`
- **Description:** Deletes a specific todo item by its ID.

    **Response:**

    ```json
    {
        "success": true,
        "message": "Todo item deleted successfully"
    }
    ```

## Middleware

### get_current_user

- **Description:** A dependency that extracts the user from the JWT token in the request header and returns the user object.

