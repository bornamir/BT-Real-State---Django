# Introduction

------



For better parctice with Markdown you can visit <www.markdownguide.org/> :

Cheat sheet : <https://www.markdownguide.org/cheat-sheet>

Basic Syntax : <https://www.markdownguide.org/basic-syntax>

What is this?

# Virtualenv

virtualenv is used to isolate the packages used in one project. This link is the package homepage [virtualenv](https://virtualenv.pypa.io/en/latest/) . Also read this [userguide](https://virtualenv.pypa.io/en/latest/userguide/) from the site. 

Here are some quick look at this documentation for start using it. For more options visit the site.

## Installing virtualenv

Using `pip install --user` is less hazardous but can still cause trouble within the particular user account. If a system package expects the system provided `virtualenv` and an incompatible version is installed with `--user` that package may have problems within that user account. To install within your user account with `pip` (if you have pip 1.3 or greater installed):

```
$ pip install --user virtualenv
```

## Starting it

Virtualenv has one basic command:

```
$ virtualenv ENV
```

Where `ENV` is a directory to place the new virtual environment. It has a number of usual effects (modifiable by many [Options](https://virtualenv.pypa.io/en/latest/reference/#options)):

> - `ENV/lib/` and `ENV/include/` are created, containing supporting library files for a new virtualenv python. Packages installed in this environment will live under `ENV/lib/pythonX.X/site-packages/`.
> - `ENV/bin` is created, where executables live - noticeably a new **python**. Thus running a script with `#! /path/to/ENV/bin/python` would run that script under this virtualenv’s python.
> - The crucial packages [pip](https://pypi.org/project/pip) and [setuptools](https://pypi.org/project/setuptools) are installed, which allow other packages to be easily installed to the environment. This associated pip can be run from `ENV/bin/pip`.

The python in your new virtualenv is effectively isolated from the python that was used to create it.



## Activate and deactivate script

In a newly created virtualenv there will also be a **activate** shell script. For Windows systems, activation scripts are provided for the Command Prompt and Powershell.

On Posix systems, this resides in `/ENV/bin/`, so you can run:

```
$ source /path/to/ENV/bin/activate
```

This will change your $PATH so its first entry is the virtualenv’s bin/ directory. (You have to use source because it changes your shell environment in-place.) This is all it does; it’s purely a convenience.

If you directly run a script or the python interpreter from the virtualenv’s `bin/` directory (e.g. `path/to/ENV/bin/pip` or `/path/to/ENV/bin/python-script.py`) then `sys.path` will automatically be set to use the Python libraries associated with the virtualenv. But, unlike the activation scripts, the environment variables `PATH` and `VIRTUAL_ENV` will *not* be modified. This means that if your Python script uses e.g. `subprocess` to run another Python script (e.g. via a `#!/usr/bin/env python` shebang line) the second script *may not be executed with the same Python binary as the first* nor have the same libraries available to it. To avoid this happening your first script will need to modify the environment variables in the same manner as the activation scripts, before the second script is executed.

The `activate` script will also modify your shell prompt to indicate which environment is currently active. To disable this behaviour, see [`VIRTUAL_ENV_DISABLE_PROMPT`](https://virtualenv.pypa.io/en/latest/reference/#envvar-VIRTUAL_ENV_DISABLE_PROMPT).

To undo these changes to your path (and prompt), just run:

```
$ deactivate
```

## The [`--system-site-packages`](https://virtualenv.pypa.io/en/latest/reference/#cmdoption-system-site-packages) Option

If you build with `virtualenv --system-site-packages ENV`, your virtual environment will inherit packages from `/usr/lib/python2.7/site-packages` (or wherever your global site-packages directory is).

This can be used if you have control over the global site-packages directory, and you want to depend on the packages there. If you want isolation from the global system, do not use this flag.

If you need to change this option after creating a virtual environment, you can add (to turn off) or remove (to turn on) the file `no-global-site-packages.txt` from `lib/python3.7/` or equivalent in the environments directory.

## Python venv 

Also it is note worthy that a subset of virtualvenv package is included in python since 3.3 but this is not the complete package and does not have all the features.



The python doc is [here](https://docs.python.org/3/library/venv.html). It can be used by the following command:

```
		python3 -m venv /path/to/new/virtual/environment
```



-----

# Git

Do not forget Git!!

```
git init
```

Create an `.gitignore` file. Help and guide for Django project in <www.gitignore.io> .



----

# Creating project

**Important** : Always activate the virtual enviroment when working with the project. This include the OS terminal and IDE terminal

## install django

Make sure you are in the virtual environment. Then  we need the django package from pip.

```
pip install django
```

If you run the `django-admin help` , you get all the available commands which django package provide.

## Create project

Among *django-admin help* command `django-admin startproject` will initialize a new project:

```bash
django-admin startproject <name of the project> <project dir>
django-admin startproject btre .
```

This command creates a directory which contains built-in apps such as authentication. But it also creates a file called `manage.py` which have all the abilities `django-admin` has. But we will use this file instead from now on.

Run the following command to see all the available commands within `manage.py`

```
python manage.py help
```



----

# Intro of project structure

## runserver command

to check that all the things are working fine, we can run the server :

```
python manage.py runserver
```

if 8000 is using as the port, checking the <localhost:8000> will bring the predefine django page.

More info in the lesson ***lesson23.mp4***

### db.sqlite3

Running the server will create some files. One of them is db.sqlite3 which is a small database. This database is not good for the real project and is used for testing,prototyping and really small web pages which have little data and traffic. But not good for real applicable projects.

###  \__init__.py

it is created with the `runserver` command too.It is empty at the beginning. and it maybe not be needed after version 3.3 . For more info see the video or search for it :D



### \__pycache__ directory







## Project initial files

Lets look at already existing files which were created by the `django-admin startproject` command more deeply.

### settings.py

Needs more description!

See the *lesson23.mp4* video.



### urls.py



### wsgi.py



### manage.py





# Creating app: pages

this app is responsible for showing static pages like home page or about page. 

the server is up and running while we make this changes!

## startapp command

For making a new app run the following command :

```
python manage.py startapp <name_of_the_app>
```

Running this command will create a directory named `<name_of_the_app>` in the project directory containing some files which is *pages* app in this project. 

### \__pycache__ directory

same as the main project. Running the server will create this directory.

### migrations directory

for any database migration we create. The *pages*  app does not have any migration.

but others may....

### admin.py 

For showing data in the admin page. The *pages* app does not have this setting. 

but others may...



### apps.py

It contains one class which name is the form AppnameConfig. This class should be added in the main settings.py file in the INSTALLED_APPS list. In this list, the name of the class should be addressed. For example for the *pages* app, the string 'pages.apps.PagesConfig' should be added to list. This procedure will makes the django to recognize this app.

### models.py

???

### tests.py

For running tests.

### views.py

If you want to write methods and linking urls to them.



## Adding pages

For creating a new page(url or view), 2 main things should be done. First the url should be defined and second the url link (or point) to a method which create (render) the page and sends it to the user.

### Defining url (path)

The first step is taking place in the urls.py file in the main project folder. In the *urlpatterns* list, the url pattern and the coresponding methods are defined with the *path* method. For example 

``` python

urlpatterns = [
    path('',views.index, name= 'index')

```

the url : *IP_Address.com/* will triggers the index method in the views.py file.

also we can group some urls and define them in a separate file. In this project, all the static pages such as home page or the about page are going to be in the *pages* app. So we create a local urls.py file in the *pages* app and then refrence to it in the main urls.py file as such:

``` python
# urls.py file in the main project directory
urlpatterns = [
    path('',include('pages.urls')),
    path('admin/', admin.site.urls),
]
```

Using the `incluse` methos, all the urls which defined in the urls.py in the pages directory (which is the pages app directory) will be included .

It is important that all the urls should be define in a list called `urlspattern`  . **Naming is important!**

### Defining methods for urls

In the second step, we need to define the method. All the methods which create the page related to a path and sending it to the users, are define in the views.py file ( in the views.py of every app). 

A simple view for the home page ( or the index page as called and defined before) is :

``` python
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse('<h1> Hello world. This is home page! </h1>')
```

the method `index` gets req( request) object which is the requset send form the user and then return a response ( or render a page) which is the view we want to be seen in the users browser. As you can notice, the code in the `HttpResponse` is in html format.



## Templates for pages

Instead of passing all the html codes to the `HttpResponse` , we can render it from a template html file.

### Template directory

In setting.py, there is a list called *TEMPLATES* and it has a *DIRS* which shows where the templates are.

In this project, we put all the templates in a directory called *templates* in the main folder ( hence alongside with btre and pages app directory). 

``` python
# in setting.py file
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Then all the files in the template directory are accessible and can be called in the methods, specially in the views methods.

```python
def about(req):
    return render(req,'pages/about.html')
```

note: The *about.html* file is in the *templates/pages/about.html* . Not in the pages app directory.





## Base Template

There are a lot of codes repeating in all the pages such as the title, navbar and ... . So we can prevent repeating by using templates. Also base templates allows us to change this similar setting easily by changing them only in one place instead of changing in all the pages views ( or html code).

First create the base html file and enter the custom code. Then there is a place where the variable codes ( specify by each page) is going to be placed. Enter the following jinja code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>BT Real State</title>
</head>
<body>
    {% block content %} {% endblock %} 	# Entet this where content coming from other templates
</body>
</html>
```

Then in each page that needs to extend the base template, add this:

```html
{% extends 'base.html' %}

{% block content %}

<h1> Put the page code here! </h1>

{% endblock %}
```



## Static files

In every project, there are some static files such as fonts, some pictures( backgrounds or logos), javascripts and css. 

In this project css, javascripts, webfonts and pictures are added in the static folder.

Also there are other static files which are produced by other apps. Such as admin pages file.( css, js and fonts for admin page) . It is better to put static files in the related app.

All the static files in the project can be collected and put in a directory. Then django reads and use this files for project from one place.

### Collecting static files

All the static files in the project can be collected and put in a directory. Then django reads and use this files for project.

### Defining STATIC_ROOT

For collecting static files, first we should define a path for it, so all the statics will be put in there. Hence add *STATIC_ROOT* list variable in the settings.py file:

```python

# add this
STATIC_ROOT= os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/' # already exist
```

### Collecting all static files

Then by running the following command (in the shell), django will find all the statics that are defined in the project and put it in the *STATIC_ROOT* path.

```shell
python manage.py collectstatic
```

### git_ignore notes

The main static folder (static root) is not going to be in the git. Some of them are going to be generated by the apps and others are put in other static file directory ( in this project btre/static path).

Hence add the */static* path to the .gitignore file.





### Apps static folder

All the static files should be recognized by the django so it can collect them by the `collectstatic` command. In order to do this, for the static files in an app, we add *STATICFILES_DIRS* (which is a list containing all the paths having static files) in the settings.py file:

```python
STATIC_URL = '/static/'
# define this list
STATICFILES_DIRS= [
    os.path.join(BASE_DIR, 'btre/static')
]
```

In this example, we put some images and fonts and css files in out main btre project folder ( because they are use generally in the project and it is logical to put it in the main project folder rather than any app). Now all the files in the *btre/static* path, are recognized as statics and will be collected when the command executed.

### Using Static files in html

In the previous section, we defined a static folder called `static` . Now we can access its content. For this , we need to include :

```html
{% load stataic %}
```

note that *static* is a tag and is not related to the name of the directory. For more information, visit the [django website](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#static) .

in the first line of html files. Then, for referencing a file 

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- Font Awesome -->
    <link rel="stylesheet" href=" {% static 'css/all.css' %}">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
    <!-- Custom -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <!--lightbox-->
    <link rel="stylesheet" href="{% static 'css/lightbox.min.css'%}">

    <title>BT Real State</title>
</head>
```

 note that the *static* name is not the static folder which is created by django when running the `collectstatic` command. Hence, the files which are in the btre/static directory are being read and not /static/ directory.



# useful notes/tips

In this section we are going to review some notes and techniques and methods useful in django programming. 

## os.path.join( path, *paths)

this method joins directories. The BASE_DIR variable is the project main folder directory. hence this method will return the path to a folder in the project folder.

## BASE_DIR

It is a String variable containing the project path. To point to a folder in the project directory it is better to use this variable with the `os.path.join` method. For example to generate the static folder in btre folder :

```python
    os.path.join(BASE_DIR, 'btre/static')
```

## jinja syntax

used by django and can be read in the html files.

## Tags in django

Refer to [this](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#static) page for complete information.

django ships with lots of useful tags such as if statements, cycles and ... .

  