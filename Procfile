web: gunicorn --bind 0.0.0.0:$PORT Estimator:app
heroku ps:scale web=1
manage.py migrate