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

        {"email":"user1@g.com","username":"user1","id":5}
    ```

5. Create "jwt":

    ```
    curl -X POST http://localhost:8000/auth/jwt/create/ -d "username="user1"&password="user-1-pas""

        {"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTU5OTAyOTgxLCJqdGkiOiJkNWQ5MGQyMDlhNjU0NmY2YWQ2YTAwMTE5ZDkwMzMxMiIsInVzZXJfaWQiOjN9.9o3LylcS4J4VoikIwBy8X5rcO6vFL6CvuZJsx8VpzE0",
         "refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU1OTk4OTA4MSwianRpIjoiNDE2YTU5MzhlZDVkNDk1YWFlZjU5MjQ1NjY4ZGVmYTciLCJ1c2VyX2lkIjozfQ.0gTmojU5ck_gNIos91J_k0EZYoQIdeawOzhOu5oiCws"}   
    ```
