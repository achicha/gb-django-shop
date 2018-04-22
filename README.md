
[![Build Status](https://travis-ci.org/achicha/gbdjangoshop.svg?branch=master)](https://travis-ci.org/achicha/gbdjangoshop)

run:

    # local  django server
    python manage.py runserver

    # gunicorn
    gunicorn --bind 0.0.0.0:8000 gbdjangoshop.wsgi:application