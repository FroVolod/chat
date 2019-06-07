# Chat

## Usage

1. Install Python 3.5 or newer
2. Install extra project modules buy issuing the following command from the terminal:

    ```
    cd "C:\path\to\the\project\folder"
    pip install -r requirements.txt
    ```
3. Start server:

    ```
    python manage.py runserver
    ```

4. Register a new user:

    ```
    curl -X POST http://localhost:8000/auth/users/create/ -d "username="user1"&password="user-1-pas"&email="user1@g.com""
    ```

5. Create "jwt":

    ```
    curl -X POST http://localhost:8000/auth/jwt/create/ -d "username="user1"&password="user-1-pas""
    ```
