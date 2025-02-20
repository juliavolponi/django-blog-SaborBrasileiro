# Sabor Brasileiro - Brazilian Recipe Blog

### A Django-based web application for sharing and discovering authentic Brazilian recipes.

**Sabor Brasileiro**
  [Website](https://django-blog-saborbrasileiro-020999f88ab7.herokuapp.com/)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Design](#design)
- [User Stories](#user-stories)
- [Known Issues](#known-issues)
- [Deployment To Heroku](#deployment-to-heroku)
- [Credits](#credits)

---

## Project Overview

**Sabor Brasileiro** is a blog-style web application built using Django, designed for Brazilian food enthusiasts. Users can sign up, log in, and create, update and delete their own recipes. Visitors can explore a variety of recipes that showcase Brazilian cuisine, including ingredients and step-by-step cooking instructions.

## Features

### General Features
- **User Authentication**: Users can register, log in, and log out.
- **Create, Read, Update, Delete (CRUD)**: Authenticated users can create their own recipes, update them, and delete them.
- **Recipe Browsing**: All visitors can browse the recipe listings and view detailed recipe information, including ingredients and instructions.

### Specific Features
- **Recipe Categories**: Recipes are organized into categories for easy navigation.
- **Responsive Design**: The website is fully responsive, providing a seamless experience on all devices.
- **Slugs for SEO**: Recipes are accessible via user-friendly URLs based on the title (slugified).
  
---

## Technologies Used

- **Django**: Backend framework.
- **HTML5/CSS3**: Frontend structure and design.
- **Bootstrap**: For responsive design and UI components.
- **SQLite**: Default database for development.
- **Gunicorn**: Web server for deploying the app on Heroku.
- **PostgreSQL**: Database for production on Heroku.

---

## Design

### Wireframes and Mockups

Here is the design that represent the layout and structure of the **Sabor Brasileiro** blog:

 **Homepage/Recipe List**
   ![Homepage](static/images/design.png)

---

## User Stories

1. **As a visitor**, I want to browse available recipes so I can explore Brazilian cuisine.
2. **As a registered user**, I want to log in so I can manage my recipes.
3. **As a logged-in user**, I want to create a new recipe so I can share my favorite Brazilian dish.
4. **As a user**, I want to edit or delete my own recipes so I can manage them efficiently.

---

## Known Issues

- **Styling Tweaks**: Some minor UI elements could be improved for better user experience.
- **Pagination**: Not currently implemented for large numbers of recipes.

---

## Deployment To Heroku 

The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:

1. The first step is to log in to Heroku (or create an account if needed).

2. In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.

3. Now it's time to enter an application name that needs to be unique. When you have chose the name, choose your region and click 'Create app".

4. On the next page, click the 'Settings' tab and find the "Config Vars" section. Click "Reveal Config Vars". Now it's time to add values. In the 'WOM Record Collection' case I needed to add two values. The first one was the credentials (KEY input field = "CREDS", VALUE input field = "your credentials", click the 'Add' button. Next you need to add another key, enter "PORT" in the KEY input field and "8000" in the VALUE field), click the 'Add' button.

5. Scroll down to the buildpacks section on the settings page and click the button 'Add buildpack'.

6. Add "Python" and node.js". It is important that Python is listed above node.js.

7. Scroll to the top of the settings page and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

8. Scroll down on the deploy page and choose deployment type. Choose to enable automatic deployments if you want to and then  click 'Deploy Branch'.

## Credits

I would like to express my deepest gratitude to **Code Institute** for providing such a comprehensive and well-structured Full Stack Developer course. The modules were incredibly detailed and easy to follow, ensuring that every concept was explained thoroughly, which helped me build confidence and gain a deep understanding.

A special thank you to the **Code Institute Support Team** for their incredible support during challenging times. Their unwavering encouragement and understanding gave me the strength to keep pushing forward. The ability to lean on their support truly helped me stay on track.

I would also like to extend a huge thanks to my **mentor** for always providing invaluable guidance. From helping me brainstorm ideas for this project to breaking down how to approach each step.

This project would not have been possible without the support of everyone involved. Thank you for believing in me and for giving me the tools and confidence to succeed.


