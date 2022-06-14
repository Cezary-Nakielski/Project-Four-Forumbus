# Table of Contents

- [Table of Contents](#table-of-contents)
- [Project 4 - Full Stack Toolkit - Forumbus](#full-stack-forumbus)
- [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Agile Development Process](#agile-development-process)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


# Full Stack Forumbus

This Full Stack Web Application allows users to share their thoughts which the deem worthy of openly publicizing as well as read posts from other users.

( This is as a milestone project for the Full Toolkit module of the Full Stack Web Development Course at Code Institute. )


## Demo

To access the deployed website, click <a href="https://forumbus2022.herokuapp.com/" target="_blank"> here. </a>


# UX

## Strategy

User's expectations:
* The user may expect to be able to write a post and edit or delete the created post. The user may want to see what other people posted, comment on the post and show approval by "liking it".

Target Users:
* Anyone who wishes to share their thoughts with the world and have a look at what other people came up with.

User Stories:

* As the owner of the website, I would like to be able to approve the posts before they are presented on the site.
* As a user of the website, I would like to be able to register in order to be able to access full functionality of the application.
* As a user of the website, I would like to be able to view the posts list so that I can choose which one to read.
* As a user of the website, I would like to be able to see other people's posts.
* As a user of the website, I would like to be able to write a post.
* As a user of the website, I would like to be able to edit my posts.
* As a user of the website, I would like to be able to delete the posts that I have written.


## Scope

### Content Requirements

Admin panel where the owner of the site can approve and manage posts.
A page where user can register.
A page where user can log in.
A page where user can log out.
A page which displays a list of posts written by users.
A page where user can rad the content of a particular post.
A page where user can edit own post.
A page where user can delete own post.


### Functional Requirements

Option for the owner to approve and manage posts.
Option for the users to register at the website.
Option for the users to log in to the website.
Option for the users to log out from the website.
Option for the users to see posts and choose to read it's content.
Option for the users to rad content of selected post.
Option for the users to write a post.
Option for the users to edit the post that they have written.
Option for the users to delete the post that they have written.


## Structure

### Interaction Design

* Presentation of options available to the user in the menu in the navbar of the website.
* Buttons placed throughout the website are easy to spot and clear in their function.
* Information about changes displayed to the user immediately upon action.


### Information Architecture

* Simple design with information placed throughout the website so that the user can intuitively and with ease move around it. 
* Main page must contain information which explains that in order to access full functionality of the website, the user has to register to do that.
* User has to receive feedback on changes made by the user.
* Navigation Panel contain information which will make the user aware of current login status. 


## Skeleton

### Navigation Design

* When the user clicks on the Logo, it takes the user to the Main Page.
* When the user clicks on the Main Page button, it takes the user to the Main Page.
* When the user clicks the Join Us button, it takes the user to the Sign Up Page.
* When the user clicks on one of the posts title and is logged in, the user is taken to the paige with post details.
* When the user clicks on the Log In button, the user is taken to the login page. After logging in the page takes the user to the main page.
* When the user clicks the Log Out button, the user is take to the log out page. Then after confirmation is logged out and taken to the main page.


### Interface design

Placement of elements throughout the website needs to make it easy to access, understand, and use in order to maximise usability and user experience.


### Wireframes

Wireframes for the project can be found <a href="https://github.com/Cezary-Nakielski/Project-Four-Forumbus/tree/main/assets/wireframes" target="_blank"> here. </a>


### ER Diagram

ER diagram for the project can be found <a href="https://github.com/Cezary-Nakielski/Project-Four-Forumbus/blob/main/assets/diagrams/er_diagram.png" target="_blank"> here. </a>

### Ralational Schema

Relational schema for the project can be found <a href="https://github.com/Cezary-Nakielski/Project-Four-Forumbus/blob/main/assets/diagrams/relational_schema.png" target="_blank"> here. </a>


##  Surface

* The interface content arrangement, colouring, typography and navigation was designed with minimalist style and approach in mind.


# Agile Development Process

As part of agile development process basic kanban board within Github Projects was used along with Guthub Issues. You can find the project <a href="https://github.com/Cezary-Nakielski/Project-Four-Forumbus/projects/1" target="_blank"> here. </a>


# Features

### Existing Features

Option to register at the website
Option to log in
Option to log out
Option to see posts written by other people
Option to read content of selected post
Option to write a post
Option to edit the post written
Option to delete the post written

### Features Left to Implement

Option for users to comment on posts
Option for users to like posts
Option for users to upload photos and videos

## Technologies Used

- [HTML]
- [CSS]
- [Javascript]
- [Python]
- [Heroku]
- [PostgreSQL]
- [Django] - Python framework
- [Gunicorn] - Server used by Django to run on Heroku
- [Dj Database Url] - library used for PostgreSQL
- [Psycopg2] - PostgreSQL database adapter for the Python
- [Dj3 Cloudinary Storage] - Django package that provides Cloudinary storage


- https://balsamiq.com - to create wireframes
- https://erdplus.com/ - to crate an ER diagram and Relational Schema
- https://express.adobe.com/ - to create the logo image

## Testing

### Manual Testing:

Functionality tested according to user stories:

#### As the owner of the site:

| Achieved | Goal |
| --- | --- |
| Yes | I would like to be able to approve the posts before they are presented on the site|

#### As the user of the site:

| Achieved | Goal |
| --- | --- |
| Yes | I would like to be able to register in order to be able to access full functionality of the application. |
| Yes | I would like to be able to view the posts list so that I can choose which one to read. |
| Yes | I would like to be able to see other people's posts. |
| Yes | I would like to be able to write a post. |
| Yes | I would like to be able to edit my posts. |
| Yes | I would like to be able to delete the posts that I have written. |

Tests of messages/feedback reflected to the user caused by action performed by the user:

| Message | Action |
| --- | --- |
| Yes | User is informed that he logged out after logging out |
| Yes | User is informed that he logged in after logging in |
| Yes | User is informed that account had been created after succesfully creating an account |
| Yes | User is informed about the result of action after succesfully creating a post |
| Yes | User is informed about the result of action after succesfully updating a post |
| Yes | User is informed about the result of action before succesfully deleting a post |
| Yes | User is told that a post with the same title already exists when the user tries to create a post with already existing title |
| Yes | Whe creating a post, if the user tries to create a post with empty content or without a title, the usrer is informed that thesefields are required |

After Logging in or logging out the user the user is brought to the main page.

After creating, updating or deleting a post the user is brought to the main page.

User can only create, update or delete posts only when being logged in.

User can only update or delete owned posts.

The website design is responsive and looks decent on all screen sizes.

All buttons function as intended.


### Automatic Testing:

- https://validator.w3.org/ - used to validate HTML syntax
- https://jigsaw.w3.org/css-validator/ - used to validate CSS syntax
- https://esprima.org/demo/validate.html - used to validate Javascript syntax
- http://pep8online.com/ - used to validate Python syntax
- https://search.google.com/test/mobile-friendly - tested for mobile compatibility of the website
- https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect - tested for the websites loading speed performance


## Bugs

During development I encountered numerous minor bugs caused by mistyping code and missing characters.

One major bug was caused due to Heroku disabling automatic deployment to Github. I used the solution provided my Code Instite, which I found in Slack. - Manually setting up deployment to Heroku through terminal.

Error I encountered - Refused to apply style from static/css/style.css because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.
Solution I applied - Used {% static 'css/style.css' %} instead of href="static/css/style.css" in base.html.

No known bugs were left to correct.

## Deployment

### Initial Commit

Once I created the project, the app and installed Django and supporting libraries in Gitpod, I created the requirements.txt file with the following command, in terminal:
- pip install -r requirements.txt

Once logged into Heroku I:
- Created new Heroku App
- Added ‘Heroku Postgres’ database to App Resources
- Copied DATABASE_URL value from Config Vars, in the Settings Tab

In Gitpod, in newly created env.py file I:
- Imported os library
- Set environment variables - os.environ["DATABASE_URL"] to the url copied from Heroku
- Added in a secret key - os.environ["SECRET_KEY"] (Made up string of characters)

In Heroku I:
- Added the newly created secret key to Config Vars - SECRET_KEY

In settings.py I referenced env.py:
- import os
- import dj_database_url
- 
- if os.path.isfile("env.py"):
-   import env
Then I replaced the secure key - SECRET_KEY = os.environ.get('<new secure key>')
Then I commented out the the old database section and added the new database section

In terminal I saved all changes and made migrations with the following command:
- python3 manage.py migrate

Once logged in, from Cloudinary website I:
- Copied CLOUDINARY_URL

In env.py I:
- Added Cloudinary URL to env.py

In Heroku I:
- Added Cloudinary URL to Heroku Config Vars
- Add DISABLE_COLLECTSTATIC to Heroku Config Vars and set it to 1 (It's only until the deployment)

In settings.py I:
- Added Cloudinary Libraries to installed apps
- Inserted code which tells Django to use Cloudinary to store media and static files
- Linked file to the templates directory in Heroku - TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
- Changed the templates directory to TEMPLATES_DIR
- Added Heroku Hostname to ALLOWED_HOSTS - ALLOWED_HOSTS = ['forumbus2022.herokuapp.com', 'localhost']

In Gitpod I created 3 new folders in top level directory:
- media, static, templates

In Procfile I added the following code:
- web: gunicorn forumbus.wsgi

Due to a security issue, Heroku has disabled automated deployments from GitHub.
In the Gitpo terminal, I typed:
- heroku login -i
- heroku apps
- heroku git:remote -a forumbus2022
- git add . && git commit -m "Deploy to Heroku via CLI"
To push changes to heroku I used the following command:
- git push heroku main

Before the final deployment, I changed the DEBUG to False in settings.py and removed the DISABLE_COLLECTSTATIC from config vars in Heroku.

## Credits

### Content

- The logo image was generated using - https://express.adobe.com/ 


### Acknowledgements

I received inspiration and information necessary for this project from lessons and material provided by Code Institute, video and text tutourials found online as well as my mentor to whom I am very grateful for his patience, understanding and expertise.

 - (https://stackoverflow.com/) Probably the best place to find answers and tips on how to work out solutions for better code

- Wireframes creation tool:
    - (https://balsamiq.com)

- ER diagram and Ralational Schema creation tool:
    - (https://erdplus.com/)

- Logo creation tool:
    - (https://express.adobe.com/)

- Python validation service:
    - (http://pep8online.com/)

- HTML validation service:
    - (https://validator.w3.org/)

- CSS validation service:
    - (https://jigsaw.w3.org/css-validator/)

- Javascript validator:
    - [Esprima](https://esprima.org/demo/validate.html)

- Webite mobile screen compatibility testing service:
    - (https://search.google.com/test/mobile-friendly)

- Web application performance testing service:
    - (https://pagespeed.web.dev/)

* This website was made for educational purposes