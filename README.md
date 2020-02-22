[![Build Status](https://travis-ci.com/CapitainHolmes/Vinyl-E-Commerce-Project.svg?branch=master)](https://travis-ci.com/CapitainHolmes/Vinyl-E-Commerce-Project)


# VINYL E-COMMERCE APP - MILSTONE PROJECT 4
 
#### Full Stack Frameworks With Djagno Project

In this project, we were asked to build a full-stack site based around business logic used to control a centrally-owned dataset, setting 
up an authentication mechanism and providing paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

We were given three example ideas which we could choose from, which were:

- Project Example Idea 1 - Build an issue tracker
    - External user’s goal: Report and track work on bugs and other issues with a product they like.
    - Site owner's goal: Get user's feedback to guide prioritisation and get money to fund work on future features.

- Project Example Idea 2 - Build an auction place to sell historical artifacts
    - External user’s goal: Find, learn about and acquire artifacts they are interested in.
    - Site owner's goal: Earn money on selling the artifacts (the site owner is the seller).

- Project Example Idea 2 - Build a site to sell your graphic design services.
    - External user’s goal: Users are able to purchase graphical designs to address their needs.
    - Site owner's goal: Earn money for doing freelance design work.

For this project I decided to use ideas from both Example Ideas 2 and 3 and create an E-Commerce Appliation that makes money through selling new/used and rare/limited edition
vinyl records.

## UX DESIGN

### About The Application

This application will give the User the ability to browse through all avaliable Vinyls for sale, check the price for each item, see the rarity and/or check to see
whether or not they're limited edition. The User will also be able to search for a specific vinyl by name (if that item is on the app and for sale), 
show and group all avaliable rare/limited edition vinyls in a search and also search for a specific music genre. 

### Target Audience 

The Target Audience for this application would be:

- Vinyl Record Enthusaists.
- Music lovers of various Genre's.
- People looking to increase their Vinyl Collection.
- People who are unable to search Record stores to find what they're looking for.

### User Stories:

- As a User I want the ability to add a vinyl to my cart.
- As a User I want to be able to search for a specific vinyl.
- As a User I want to be able to register my login details and be able to login.
- As a User I want the application to remember my cart items.
- As a User I want to be able to purchase vinyls online from this app.

## FEATURES

### Features Used in This Project:

- a Search bar.
- The ability to search for a specific Vinyl record.
- Add multiple Vinyls to your cart.
- Sign in/out functionality.
- Able to register an account for the application.
- Checkout and purchase Vinyls that you have added to your cart.
- A dropdwon navigation bar for responsive design on smaller screens.
- The ability to view how many items you have added to your cart over the 'cart' tab in the navigation bar.
- A full form for adding in your address and card details to checkout adn purchase vinyls.


## TECHNOLOGIES

### The Technologies I Have Used:

- **[Balsamiq](https://balsamiq.com/wireframes/?gclid=EAIaIQobChMInpvOqJ3C5wIVxLHtCh0U4Qe3EAAYASAAEgItD_D_BwE)** - I have used MoqUps to create the mockup version of my website, that can be found **[Here.](https://github.com/CapitainHolmes/Vinyl-E-Commerce-Project/tree/master/Mockups)**
- **[HTML5](https://en.wikipedia.org/wiki/HTML5)** - I have used HTML5 to create the base of my project.
- **[Bootstrap](https://materializecss.com/)** - I have used Bootstrap for it's frontend frameworks for the style and layout of my project.
- **[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)** - I have used CSS3 for myy custom styles for certain things in my project.
- **[Python 3](https://www.python.org/)** - I have used Python 3 for the backend of my project along with the.
- **[Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)** - I have used Jinja2 for it's templating language so that i'm not repeating unnecessary code.
- **[Heroku](https://en.wikipedia.org/wiki/Heroku)** - I have used Heroku to deploy my application.
- **[Django](https://www.djangoproject.com/foundation/)** - as python web framework rapid development and clean, pragmatic design.
- **[Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)** - to handle version control.
- **[GitHub](https://en.wikipedia.org/wiki/GitHub)** - to store the project code remotely.
- **[PIP3](https://en.wikipedia.org/wiki/Pip_(package_manager))** - for installation of tools needed in this project.
- **[Stripe](https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450442&utm_term=stripe%20payments&utm_matchtype=e&utm_adposition=1t2&utm_device=c&gclid=EAIaIQobChMI9ubDhJ7C5wIViKztCh0DNQ3oEAAYAiAAEgIt0PD_BwE)** - 
as payment platform to validate and accept credit card payments securely.

## TESTING

I have a static directory with a folder for all tests that I conducted for this application which can be found **[here](https://github.com/CapitainHolmes/Vinyl-E-Commerce-Project/tree/master/static/tests)**

For testing I have used an IDE called Selenium, which is a free add-on for Google Chrome or Firefox. It is used for automated testing of web applications
and is really easy and simple to use.

- The First test I conducted was to open the application and to check to see if the 
Logo was there on the navigation bar, indicating that the application was live and in fully working order. 
This test can be found **[here](https://github.com/CapitainHolmes/Vinyl-E-Commerce-Project/tree/master/static/tests/selenium-tests/selenium-open-app-test.png)**

- The Second test I conducted, was to see if the ability to add a vinyl to the cart (when logged in) was fully functional.
This test can be found **[here](https://github.com/CapitainHolmes/Vinyl-E-Commerce-Project/blob/master/static/tests/selenium-tests/selenium-add-to-cart-test.png)**

- The Third test I conducted, was to see if the search functionaly was functional by searching for an Artist by name. 
This test can be found **[here](https://github.com/CapitainHolmes/Vinyl-E-Commerce-Project/blob/master/static/tests/selenium-tests/selenium-test-search-functionality.png)**

- The Fourth test I conducted, was to see whether a user is able to check their added item out by filling the details form on the checkout page.
This test can be found **[here](https://github.com/CapitainHolmes/Vinyl-E-Commerce-Project/blob/master/static/tests/selenium-tests/selenium-checking-out-test.png)**

I also conducted tests on a wide selction of browsers/devices to ensure User's can successfully use the site and it's features.

These tests included browsers/devices:

- Edge - laptop
- Mozilla - laptop
- Chrome - laptop and iPhone
- Safari - iPhone
- Internet Explorer - laptop

Here is a list of each Validator used to check my code:

- **[W3C HTML](https://validator.w3.org/)**
- **[W3C CSS3](https://jigsaw.w3.org/css-validator/)**


### Things to Add or Change in the Future

In future the things I would add:

- The ability to see whether or not a vinyl is rare/limited edition and also to search for all rare/limited vinyls.

## DEPLOYMENT

Throughout the course of this project I have been commiting every finished functionality, 
every bug fix and things I thought needed removing, to GitHub using **[Version Control.](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)**

All my commits and the full code for my project can be found on my GitHub Repository which can be found **[Here.](https://github.com/CapitainHolmes/Vinyl-E-Commerce-Project)** 

## CREDIT

The biggest thing I can credit the most, is the Code Institute course material. Being in the situation I am in, starting a new job, still reocvering from surgery, 
I cannot give enough credit to how simple and easy their videos are to follow and help me to get this project finished. I used a lot of their course material for this course,
as I was really confused and struggling for idea's. Also panicking due to my end date getting closer and closer (as I am writing this my end date is in 6 days).


## ACKNOWLEDGEMENTS

I want to thank the Code Institute Tutor System for all their help and support throughout, not just for this project but for the course as a whole. It has been
a rollercoaster, but I'm thrilled to be finally ready to submit my Fourth AND last project with Code Institute.

I recieved inspiration for this project from:

- Friends.
- My Mentor Dick.