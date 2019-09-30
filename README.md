
# BT Real State Website

This project is created based on a tutorial on [Udemy](https://www.udemy.com/course/python-django-dev-to-deployment/) by Created by [Brad Traversy](https://www.udemy.com/course/python-django-dev-to-deployment/#instructor-1)

This project is about developing a backend for a real state website. The static pages (front end including html, css and javascript files) has been provided and they need to be implemented so that the pages become dynamic. 

For developing the backend Django framework is used. Also the website uses postgreSQL as database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

There should be python 3.7 installed on the machine.

### Installing

clone the project

```shell
git clone https://github.com/bornamir/BT-Real-State---Django.git
```

create and start a a virtual environment

```shell
projects/ThreeAttemptsLogin $ virtualenv venv
projects/ThreeAttemptsLogin $ source venv/bin/activate
```

Install the project dependencies:

```shell
pip install -r requirements.txt
```

then run

```shell
python manage.py migrate
```

to start the development server

```py
python manage.py runserver
```

and open localhost:8000 on your browser to view the app.

## Built With

* [Django 2.1](https://www.djangoproject.com/) - The web framework 
* [Python 3.7](https://www.python.org/downloads/release/python-370/) 

## Authors

* **Borna Mir Arabshahi**  - [github](https://github.com/bornamir)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

This project is done based on a tutorial by [Brad Traversy](https://www.udemy.com/course/python-django-dev-to-deployment/#instructor-1) on Udemy.

Many thanks to him and his great tutorial.

