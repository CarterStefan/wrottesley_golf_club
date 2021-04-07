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
![Homepage](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/homepage.png)


![Products](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/products.png)


![Product Details](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/product_details.png)


![Basket](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/Basket.png)


![Checkout](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/checkout.png)


![Blog](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/blog.png)


![Blog Post](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/blog_post.png)


![Tournaments](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static//UX/Wireframes/Desktop/tournaments.png)


![Memberships](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/memberships.png)


![Profile](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/profile.png)


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
