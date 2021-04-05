![Logo Text](https://user-images.githubusercontent.com/64138643/108905833-17788880-7618-11eb-85e6-b6c7e066fe7c.PNG)

### [Heroku App](https://wrottesley-golf-club.herokuapp.com/)
### [GitHub](https://github.com/CarterStefan/wrottesley_golf_club)

Wrottesley Golf Club is a golf course located in the west midlands. There are a number of users that the website will target and each of these user types will have a different need when using the website. This is my fourth milestone project as part of my Full Stack Web Development Course with [Code Institute](https://codeinstitute.net/). This project focuses on "Full stack Frameworks With Django" and will put into practice what I have learned over the last year on the course.

## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
  - [**User Stories**](#user-stories)
  - [**Design**](#design)
    - [**Libraries**](#third-party-libraries)
    - [**Color Scheme**](#color-scheme)
    - [**Typography**](#typography)
  - [**Wireframes**](#wireframes)
3. [**Features**](#features)
  - [**Existing Features**](#existing-features)
  - [**Features Left to Implement**](#features-left-to-implemement)
4. [**Technologies Used**](#technologies-used)
5. [**Databases Used**](#databases-used)
6. [**Deployment**](#Deployment)
7. [**Testing**](#Testing)
8. [**Acknowledgments**](#Acknowledgments)
---

## Project overview
The project was built using [Django](https://www.djangoproject.com/) - web framework.
 
 
## UX

### User Stories

The three targetted users of the site will be:
- Existing members of the club
- Potential Members of the club
- Casual golfers wishing to play a round or purchase products from the store

Using the website, all users will be able to:

#### Viewing & Navigation
- View informatiion about the club
- View contact information about the club
- See a list of all the products that I can purchase through the club

#### Registration & User Accounts
- Register for an account
- Login and Logout of the account
- Recover my password easily
- Recieve email confirmations once I have registered for an account
- Have an area of the user profile dedicated to my purchase history
- Have an area of the user profile dedicated to my personal information

#### The Store
- View and sort all products in the store
- Sort within a chosen category
- Search for an item
- See what the search criteria was
- Select the quantity of an item to purchase
- Select the size of an item (if applicable)
- View my items that I have added to my bag
- Delete an item and reduce the size selected
- Easily fill out delivery and payment information
- View an order summary once a purchase is made
- Recieve an email confirmation

#### Subscribtions
- See the benefits of a pro membership
- Be able to purchase a pro membership
- Be able to downgrade to beginner membership at any time

#### Blog
- Read the latest news about the course
- Comment on a blog post
- Upload new blog posts (Admin Only)
- Edit blog posts (Admin Only)
- Delete blog posts (Admin Only)

#### Administration
- Upload new products to the store (Admin Only)
- Edit the existing products in the store (Admin Only)
- Delete a product from the store (Admin Only)
- Approve comments which have been made on blog posts (Admin Only)


## UI

#### Color Scheme
[uiuxcenter](https://www.instagram.com/uiuxcenter/?hl=en) - Used for inspiration on my color scheme, to create a bold web experience.

#### Typography
[GoogleFonts](https://fonts.google.com/)
- [Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville?query=Libre+Baskerville) - Used for the logo and headings around the site
- [Roboto](https://fonts.google.com/specimen/Roboto?query=Roboto) - Used for the main body text

#### Third party Libraries
 - [Bootstrap](https://getbootstrap.com/) - A modern responsive front-end framework. Used for the layout of the site, responsiveness to screen sizes and various features around the site (forms, cards, buttons, search selctions etc)
 - [jQuery](https://jquery.com/) - jQuery is a fast, small, and feature-rich JavaScript library. Used for some interactive elements with the Bootstrap features.
 - [Fontawesome](https://fontawesome.com/) - Font Awesome is a font and icon toolkit based on CSS and Less. Used for all the icons around the site.

#### Desktop Wireframes
##### Homepage
![Homepage](https://user-images.githubusercontent.com/64138643/109057030-24a97c00-76d9-11eb-970e-a57d0d017f35.png)

##### Products
![Products](https://user-images.githubusercontent.com/64138643/109057014-2115f500-76d9-11eb-8e23-21a0433e092e.png)

##### Product Details
![Product Details](https://user-images.githubusercontent.com/64138643/109057032-24a97c00-76d9-11eb-9ce6-50de431d0e4f.png)

##### Basket
![Basket](https://user-images.githubusercontent.com/64138643/109057019-22dfb880-76d9-11eb-924b-7ee89c4d09c8.png)

##### Checkout
![Checkout](https://user-images.githubusercontent.com/64138643/109057025-23784f00-76d9-11eb-9b63-e9324238e2d7.png)

##### Blog
![Blog](https://user-images.githubusercontent.com/64138643/109057021-22dfb880-76d9-11eb-944b-87542884a8e7.png)

##### Tournaments
![Tournaments](https://user-images.githubusercontent.com/64138643/109057017-21ae8b80-76d9-11eb-8faa-fc96ce54c6c2.png)

### Features

The Wrottesley Golf Club website has 9 apps:
- Basket
- Blog
- Checkout
- Home
- Memberships
- Products
- Profiles
- Tournaments
- Account
