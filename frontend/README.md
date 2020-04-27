## <div align="center">Frontend<br /><br /></div>


Frontend in our project is a Flask application. [Flask]((https://flask.palletsprojects.com/en/1.1.x/)) is a lightweight web application framework. Flask uses Jinjga, a templating engine in python, for creating templates and managing pages in the frontend.

Broadly, our frontend has following Components:
- Flask: for managing routes and APIs
- SQLite: for database
- SQL-Alchemy: ORM for accessing database in Flask.
- Templates: written in HTML and Bootstrap CSS, using Jinja template engine for writing templates.

### How to run:
- To run flask app, export the following variables before calling "flask run" command. Port and other details can be changed as needed.
 ```$export FLASK_APP=frontend
 $export FLASK_RUN_PORT=5000
 $export FLASK_DEBUG=1
 $flask run
 ```

### Each component is detailed in the following section.
#### 1. Flask
  - Used here primarily to manage the routes and routing within the application.
  - Managing login of users using flask-login package, with SQLite database
  - Consists of following files
    - [__init__.py](__init__.py): for initial confiuration of flask app, linking login manager, database
    - [main.py](main.py): for handling routes to home page of the web application.
    - [auth.py](auth.py): for handling authentication realted routes (login, logout) for the application.
    - [services.py](services.py): for handling routes for each individual services, API calls, and service webpage calls.

#### 2. SQLite and SQL-Alchemy
  - SQLite is used as the datbase for storing user details for authentication purposes
  - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper, enabliing SQL functionality within python.
  - [models_db.py](models_db.py) is used for defining class for each database table that we intend to use in the application.
  - models_db.py implements classes for User schema and Service Schema. Users schema is used to store the user relaed data for login and authentication purposes. Service schema is used for storing details reagarding services. These details are used for storng data about services like API details, route detils. These are used for populating content in webpages. This ensures that we don't have to change individual HTMLs every time a new service is added.
  - Flask-migrate package is used for handling the changes in the database schemas. This packages handles changes easily while keeping the data from older schemas intact and usable in new schema. This keeps application open for extension and easy to implement changes.

#### 3. Templates:
  - Flask plugins are used for genarting forms for login and register pages in the application.
  - Flask support Jinja template engine which allows inheritence from a particular layout. For ex: all service pages will inherit from the service.html layout and change the body as needed for that service.
  - HTML and Bootstrap CSS is used to generating the static pages. Links and some other contents in hese pages are populated by using Jinjga syntax, by sending data from python API/function calls.
  - [templates](templates) is used for storing HTMLs of all pages within the application, which in turn use the contents of [static](static) as resources like CSS stylesheets, images etc.


### How to add services to the page
Pleaes refer this [document](/Adding_a_service_Readme.md) for adding new service to this page.


### Futher improvements:
1. Dockerizing the application, so that user of the forntend do not have to go through the excercise of installing all dependencies.
2. Changng SQLite to a more scalable database.
3. A more thorogh automatic updation of individual HTMLs and service pages. 
