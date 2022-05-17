# Pitches
This' is Pitches website where user can sign in and put comments on pitch


## Built By [Kipkemoi Elvis](https://github.com/DynastyElvis)


You can view the site at: [ My PITCHES Live Link](https://pitches-posts.herokuapp.com/)


## Screenshots
<img src="https://github.com/DynastyElvis/Posts/blob/main/post/static/img/Screenshot%20from%202022-05-16%2009-17-33.png" width="800px" height="400px">
<img src="https://github.com/DynastyElvis/Posts/blob/main/post/static/img/Screenshot%20from%202022-05-16%2009-17-39.png" width="800px" height="400px">
<img src="https://github.com/DynastyElvis/Posts/blob/main/post/static/img/Screenshot%20from%202022-05-16%2009-17-52.png" width="800px" height="400px">
<img src="https://github.com/DynastyElvis/Posts/blob/main/post/static/img/Screenshot%20from%202022-05-16%2009-17-55.png" width="800px" height="400px">

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

[Go Back to the top](#Pitches)

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select login|
| Select login |  **Email**,**Password** |Redirect to Home page|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with all pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Select comment button | **Add Comment** | Form that you input your comment|
| Select comment button | **View Comment** | Redirect to all comments|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

---
[Go Back to the top](#Pitches)

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv

[Go Back to the top](#Pitches)

### Cloning
* In your terminal:

        $ git clone https://github.com/DynastyElvis/Pitches
        $ cd Pitches

[Go Back to the top](#Pitches)

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.8 -m pip install Flask
        $ python3.8 -m pip install Flask-Bootstrap
        $ python3.8 -m pip install Flask-Script

To get the code..
Cloning the repository:
  ```bash
https://github.com/DynastyElvis/Pitches  ```
Move to the folder and install requirements
  ```bash
  cd Wise_Pitches
  pip install -r requirements.txt
  ```
Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
Running the application
  ```bash
  python3.8 manage.py server
  ```
Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser 
```bash
127.0.0.1:5000
```
---


* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

[Go Back to the top](#Pitches)

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py tests

[Go Back to the top](#Pitches)

## Technologies Used
* Python3.8
* Flask

[Go Back to the top](#Pitches)

## License

[MIT LICENCE](https://github.com/DynastyElvis/Pitches/blob/main/LICENSE)


Copyright (c) 2022 K. E. Rono


[Go Back to the top](#Pitches)

## Known Bugs

No Known Bugs.

[Go Back to the top](#Pitches)

## Authors Info
LinkedIn - [KIPKEMOI ELVIS RONO](https://www.linkedin.com/in/elvis-rono-aa3548209/)

[Go Back to the top](#Pitches)


