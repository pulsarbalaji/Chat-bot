# Quiz bot
This is a basic version of an interactive quiz bot that engages users in quizzes, evaluates their responses, and provides a final score based on their answers. In this we use Django channels websocket communication, redis as message broker, and Django sessions for temporary data storage.


Steps to run the project with Docker

1. Install Docker and Docker Compose (https://docs.docker.com/compose/install/)
2. Docker should be running
3. In the project root run `docker-compose build` and `docker-compose up`
4. Go to `localhost` to view the chatbot


Steps to run the project without Docker

1. Install required packages by running `pip install -r requirements.txt`
2. Install and run postgresql, and change the `DATABASES` config in `settings.py`, if required.
3. Install and run redis, and update the `CHANNEL_LAYERS` config in `settings.py`, if required.
4. In the project root run `python manage.py runserver`
4. Go to `127.0.0.1:8000` to view the chatbot



#vijay balaji Arumugam 
#setup of project
1. clone repo
https://github.com/pulsarbalaji/Chat-bot.git

cd Chat-bot

2. Create Venv(Virtual Environment)

python -m venv venv

activate - venv\script\activate

3. Install Dependencies

pip install -r requirements.txt

4. DB setup and create .env

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

put in bash python manage.py migrate

5. start and run local 

python manage.py runserver

6. Visit:

http://127.0.0.1:8000/quiz?msg=
 → first request shows welcome + Q1

http://127.0.0.1:8000/quiz?msg=7
 → example response



