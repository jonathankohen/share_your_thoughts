<div align="center" margin-bottom="20px">
    <img src="../main/social_network/static/images/wacky.png" alt="Logo" width="200" />
</div>

# Share Your Thoughts

Share Your Thoughts is a social network web application with which users can... share their toughts with each other! The project is a work in progress built using Python, Django, SQLite, and Bootstrap with CSS overrides.

## Demo
![Demo Animation](../media/social_network/static/images/sytGif.gif)

## Getting Started

You will need `python`, `django`, and a `virtual environment` installed.

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/jonathankohen/share_your_thoughts.git
    $ cd portfolio_project
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

## Description

Much like the social networks it was modelled after, Share Your Thoughts allows users to create and like posts. User's liked posts are sectioned into a "favorites" section, with the rest in a timeline. Users can see who created each post, and choose to like or unlike them. In the case that the user created the post, they have the option to delete it as well. Users may also select individual posts to navigate to a new page that displays how many people have liked the post, and their names.

As it is a work in progress, I plan to add more features including API integrations, and OAuth.
