# Learning Equality Trivia

This is a simple multiple-choice question app built on top of [djanvo-vue-template](https://github.com/gtalarico/django-vue-template).

## Prerequisites

Before getting started you should have the following installed and running. If you have none of these programs, you must install them in the same order as this list (e.g. Yarn, then Vue CLI 3, etc.).

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install)
- [X] Vue CLI 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Pipenv - [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

You will also need `git` to download the source code.

## Set up development environment

Download the code:

```
$ git clone https://github.com/jonboiser/le-trivia-app
$ cd le-trivia-app
```

Install JS dependencies via Yarn and Python dependencies with pipenv:

```
$ yarn install
$ pipenv install --dev && pipenv shell
```

Create the local database and load fixture data

```
$ python manage.py migrate
$ python manage.py loaddata questions
```

## Running the development server

To make things easier, open another tab or window in your terminal program and navigate to the same directory. Once you are there, enter `pipenv shell` so that both terminals are within the Python virtualenv.

Start the Django dev server in one terminal:

```
$ python manage.py runserver
```

Start the Webpack dev server in the other terminal:

```
$ yarn serve
```

If everything is set up correctly, you will see some success messages in the terminal.

In your browser, go to [`http://localhost:8080/api`](http://localhost:8080/api) to view the Django API, then go to [`http://localhost:8000`](http://localhost:8000) to view the trivia app.

## How to prepare for the coding interview

Please have your development environment ready before the interview starts, since time is limited. Aside from that, here are some other suggestions to help you be more comfortable and prepared.

1. Download whatever tooling you need to code comfortably in Vue and Django. At a minimum, make sure you have syntax highlighting for these languages. I would even recommend downloading Vue Dev Tools for your favorite web browser.
1. Make sure your webcam and microphone work and that you can share your screen over Zoom.
1. Read the code and play with the app. Even though it mostly works, there are a lot of improvements we can make. Make a list of these issues (mentally, digitally, or on paper), since we might ask you to implement some of these improvements during the interview.
1. If you are not familiar with this technology stack, I would recommend going to the documentation for [Vue](), [Django](), and [Django Rest Framework]() and getting comfortable with searching for different topics. For your own edification, you might want to read the docs for Vue Router and Axios, but the code is written in a way where you can easily infer the APIs for those libraries. The boilerplate code from the Django-Vue-Template project is also useful to read (see `messageService.js` and `models,views,urls.py`).
1. If you are an expert in other similar technologies like React, Angular, etc. (for frontend development) and/or Spring, Rails, .NET, NodeJS, etc. for (backend development), try to make conceptual connections between those technologies and Vue/Django.
