![Logo Text](https://user-images.githubusercontent.com/64138643/108905833-17788880-7618-11eb-85e6-b6c7e066fe7c.PNG)

### [Heroku App](https://wrottesley-golf-club.herokuapp.com/)
### [GitHub](https://github.com/CarterStefan/wrottesley_golf_club)

Wrottesley Golf Club is a golf course located in the west midlands. There are a number of users that the website will target and each of these user types will have a different need when using the website. This is my fourth milestone project as part of my Full Stack Web Development Course with [Code Institute](https://codeinstitute.net/). This project focuses on "Full stack Frameworks With Django" and will put into practice what I have learned over the last year on the course.

## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
  - [**User Stories**](#user-stories)
3. [**UI**](#ui)
  - [**Color Scheme**](#color-scheme)
  - [**Typography**](#typography)
  - [**Wireframes**](#wireframes)
4. [**Features**](#features)
  - [**Existing Features**](#existing-features)
  - [**Features Left to Implement**](#features-left-to-implemement)
5. [**Databases**](#databases)
6. [**Technologies Used**](#technologies-used)
7. [**Deployment**](#Deployment)
8. [**Testing**](#Testing)
9. [**Acknowledgments**](#Acknowledgments)
---

## Project overview
The project was built using [Django](https://www.djangoproject.com/) - web framework. 

For the testing of the store and subscriptions, a test credit card can be used by inputting the following details:
- Card Number: 4242 4242 4242 4242
- Exp date: 04/24
- CVC: 424
- ZIP: 42424
 
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
- Easily navigate to the Tournaments page
- Easily navigate to the Blog page
- Easily navigate to the Store page
- Easily navigate to the Memberships page
- Always be able to see the total count of the basket

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
- Recieve an email confirmation when a purchase is made

#### Subscribtions
- See the benefits of a pro membership
- Be able to purchase a pro membership
- Be able to downgrade to beginner membership at any time

#### Blog
- Read the latest news about the course through individual blog posts
- Comment on a blog post
- Upload new blog posts (Admin Only)
- Edit blog posts (Admin Only)
- Delete blog posts (Admin Only)
- Approve comments which have been posted on a blog
- Only allow approved comments to be visible to members

#### Tournaments
- See a list of all the upcoming tournaments
- See the dates and times of the tournaments
- See the location of the tournaments
- See the prices of the tournaments

#### Administration
- Upload new tournaments to the Tournaments page (Admin Only)
- Edit tournaments on the Tournaments page (Admin Only)
- Delete tournaments (Admin only)
- Upload new products to the store (Admin Only)
- Edit the existing products in the store (Admin Only)
- Delete a product from the store (Admin Only)
- Approve comments which have been made on blog posts (Admin Only)

## UI
#### Color Scheme
[uiuxcenter](https://www.instagram.com/uiuxcenter/?hl=en) - Used for inspiration on my color scheme, to create a bold web experience.
![ColorScheme](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/color_scheme.PNG)

#### Typography
[GoogleFonts](https://fonts.google.com/)
- [Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville?query=Libre+Baskerville) - Used for the logo and headings around the site
- [Roboto](https://fonts.google.com/specimen/Roboto?query=Roboto) - Used for the main body text

#### Desktop Wireframes
<details><summary>Homepage</summary>
<p>

![Homepage](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/homepage.png)

</p>
</details>

<details><summary>Products</summary>
<p>

![Products](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/products.png)

</p>
</details>

<details><summary>Product Details</summary>
<p>

![Product Details](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/product_details.png)

</p>
</details>

<details><summary>Basket</summary>
<p>

![Basket](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/Basket.png)

</p>
</details>

<details><summary>Checkout</summary>
<p>

![Checkout](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/checkout.png)

</p>
</details>

<details><summary>Blog</summary>
<p>

![Blog](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/blog.png)

</p>
</details>

<details><summary>Blog Post</summary>
<p>

![Blog Post](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/blog_post.png)

</p>
</details>

<details><summary>Tournaments</summary>
<p>

![Tournaments](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static//UX/Wireframes/Desktop/tournaments.png)

</p>
</details>

<details><summary>Memberships</summary>
<p>

![Memberships](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/memberships.png)

</p>
</details>

<details><summary>Profile</summary>
<p>

![Profile](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Desktop/profile.png)

</p>
</details>

#### Tablet Wireframes
<details><summary>Homepage</summary>
<p>

![Homepage](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_homepage.png)

</p>
</details>

<details><summary>Products</summary>
<p>

![Products](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_store.png)

</p>
</details>

<details><summary>Product Details</summary>
<p>

![Product Details](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_store_product.png)

</p>
</details>

<details><summary>Basket</summary>
<p>

![Basket](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_basket.png)

</p>
</details>

<details><summary>Checkout</summary>
<p>

![Checkout](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_checkout.png)

</p>
</details>

<details><summary>Blog</summary>
<p>

![Blog](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_blog.png)

</p>
</details>

<details><summary>Blog Post</summary>
<p>

![Blog Post](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_blog_post.png)

</p>
</details>

<details><summary>Tournaments</summary>
<p>

![Tournaments](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static//UX/Wireframes/Tablet/tablet_tournaments.png)

</p>
</details>

<details><summary>Memberships</summary>
<p>

![Memberships](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_memberships.png)

</p>
</details>

<details><summary>Profile</summary>
<p>

![Profile](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Tablet/tablet_profile.png)

</p>
</details>

#### Mobile Wireframes
<details><summary>Homepage</summary>
<p>

![Homepage](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_homepage.png)

</p>
</details>

<details><summary>Products</summary>
<p>

![Products](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_store.png)

</p>
</details>

<details><summary>Product Details</summary>
<p>

![Product Details](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_store_item.png)

</p>
</details>

<details><summary>Basket</summary>
<p>

![Basket](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_basket.png)

</p>
</details>

<details><summary>Checkout</summary>
<p>

![Checkout](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_checkout.png)

</p>
</details>

<details><summary>Blog</summary>
<p>

![Blog](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_blog.png)

</p>
</details>

<details><summary>Blog Post</summary>
<p>

![Blog Post](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_blog_post.png)

</p>
</details>

<details><summary>Tournaments</summary>
<p>

![Tournaments](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static//UX/Wireframes/Mobile/mobile_tournaments.png)

</p>
</details>

<details><summary>Memberships</summary>
<p>

![Memberships](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_memberships.png)

</p>
</details>

<details><summary>Profile</summary>
<p>

![Profile](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Wireframes/Mobile/mobile_profile.png)

</p>
</details>


## Features
### Existing Features & Pages

#### Navbar
The nav bar serves as the main navigation for the site. It is always visible at the top of the page accross all pages of the site. The navbar shows the Wrottesley Golf Club logo, which links to the homepage, an account button which shows a dropdown with options to go to the profile page or logout, and a basket which is the link to the basket page and also to keep track of the ammount of the current basket. 

The secondary part of the navbar has four links, which go to the tournaments page, the blog page, the store page and the memberships page.

#### Footer
The footer serves as secondary navigation. It has the same links as the nav bar but also features the golf club address and some external links to facebook, twitter and instagram. 

#### The homepage
This serves as the landing page upon sign-up and login and the main hub for the site. The main feature on the site is the hero image and a statement to say the store is now live with a CTA to the store page. Beneath this there is a banner for information about memberships as well as some extra navigation to the blog, memberships and store pages.

![Homepage_one](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/homepage_one.PNG)
![Homepage_two](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/homepage_two.PNG)

#### Tournaments
The tournaments page is a simple table which lists all of the items on the tournaments database. The table shows five columns - Name, Date, Time, Location and Price. The price will show either the ammount or 'Free' depending on your membership level.

#### Blog
The blog page serves as a place listing all of the blog posts in one page. The items are stacked in a single column vertically down the page on all screen sizes. Each blog post is summarised in a card and shows the main image, the title, the author, the first 200 characters, the time the post was last updated and a button to go to the blog post itself. As a superuser, you can also add, edit and delete a post from this page. 

![Blog_one](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/blog_one.PNG)

As a superuser, as well as being able to do so on the admin panel, there is also a form to edit or add a new blog to the list of blogs on the website. There will be links to the forms visible on the blog page if you are a superuser.

#### Blog Post
The blog post page shows the full details of the individual blog post you have just clicked on. This shows the full hero image at the top of the page, the title, the author and the full blog post. At the top of the page you can see a count of how many comments there have been on the post. 

![Blog_two](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/blog_two.PNG)

Underneath the post, there is the option to leave a comment on the post, up to a maximum of 200 characters. You won't go over this count, as there is a count to warn you when you are close and also the button to submit the comment will not be clickable if you go over. You will only be able to leave a comment if you are logged in. Underneath the form the list of comments are listed in a vertical column. The comments will only be visible if a superuser has deemed the comment as safe and approved it on the database.

![Blog_three](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/blog_three.PNG)

#### Store
The store page lists all the products which are listed on the product database and some tools to help you navigate these products so you can find exactly what you want when there are a lot more items in the store. 

The first is a search bar which filters the results down by taking the search criteria and matching it to the product title, the product description or the categories. if nothing is entered into the search box when the user presses submits a search query, the page will show all products and a message will appear to let the user know they need to enter search criteria to search the store.

Above the search bar, there is a total count of the number of items currently listed on the page. If no filtering has been done, it will just show the count followed by the word products e.g "12 Products". If a category has been chosen, the count will show the category selected and the total number of ptoducts e.g "Accessories | 4 products". If the user has used the search box, the count will show the number of products and te search term that was entered e.g "1 products found for "tees""

Above the products is a sort dropdown which lets the user sort by four different criteria - Price (high - low), price (low - high), name (a - z), name (z - a). 

All the products are listed in individual cards which show the product category, image, title and price. Clicking the image will take the user to the product detail page. 

![Products_one](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/products_one.PNG)

#### Product Detail
The prduct detail page shows more information about a particular product. This has some of the same information seen on the product detail card in the store page, with some extra details. On the product detail page the user can see the product image, title, price, catgeory and full description. On top of this, the user can update the quantity and select the size of the item to purchse, if the product has sizes. There is also a primary button here to add the product to the basket, and a secondary button to go back to the store. Clicking the category will take the user back to the store, but the products will be filtered by that category.

![Products_two](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/products_two.PNG)

Underneath the product details, there is a banner which shows other products the user may be insterested in. This will show other products from the same category, which when clicked, will take the user to that product.

![Products_three](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/products_three.PNG)

#### Memberships
The memberships page serves as the page to manage your subscription with the club. The display on the page is dependent on the current membership level of the user. If the user is a new member, and has never had a subscription before, they will be classed as a 'beginner' member for use around the site but will technically have no membership status. When coming to the memberships page in this scenario, the user would see details of the pro membership and a primary button to subscribe. Clicking this would take them to the stripe checkout page where they would add their card details and become a plus member. When navigating back to the membership page, they would see scenario two. 

If coming to the page as a 'pro' member, the user would see a page which highlights the benefits of being a plus member, but will now give them the option to downgrade their membership level from 'pro' to 'beginner'. Clicking this button will not require the user to fill out any other details, but will switch the customers membership level instantly. When navigating back to the memberships page, they would see scenario three. 

When coming to this page as a 'beginner' member, the user would see a page highlighting the benefits of pro membership with the option to upgrade again to this level. This would be easier this time around, and will not require the user to fill out the credit card details, but would switch the membership level to 'pro' on both the user profile and the stripe system, using the original card details.

![Memberships_one](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/memberships_one.PNG)

#### Basket
The basket page shows a summary of the products in the basket and the amount that the current basket equates to. Here, the user has the ability to update the quantity of each product or delete it entirely from the basket. The amounts show a breakdown of the prices and a total amount with a button which takes the user to the checkout page.

![Basket_one](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/basket_one.PNG)

#### Checkout
The checkout page has two sections, the delivery and personal information details and the total of the order. The details is a form when, if logged in, lets the user save their information to their profile for a quicker checkout next time. The total is similar to the basket page, and shows the breakdown of the amounts with the option ot edit the basket and a final summary of how much will be charged. The final feature on the page is the payment information which uses Stripe to handle the payments. A successfull payment will take the users to the order success page showing the order summary.

![Checkout_one](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/checkout_one.PNG)

#### Profile
The profile page is split into two sections, delivery details and order history. The delivery details is a simple form and has an 'update information' button below to update their details on their profile, which would also reflect on the delivery details on the checkout page.

![Profile_one](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/basket_one.PNG)

The order history shows a summary of the users previous orders. It is in the layout of a table and shows the order number, date, items and the grand total. Clicking the order number would take the user to the order summary where they would see a more detailed breakdown of the order. Underneath the order history is a button to go to the store. 

![Profile_two](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/Features/basket_two.PNG)

#### Future Features

## Databases
For my development environment, I was using SQLite, as this is the default with Django. Once my code was deployed to Heroku, I switched to a PostgreSQL database.

### models and apps
My site consists of 9 models and 8 apps

#### Home App
- The home app is used to display index.html, which serves as the root page of the site. This app contains no models.

#### Basket App
- The basket app is used for basic CRUD operations for managing products in the shopping basket. This app contains no models.

#### Blog App
- The blog app is used to show blog posts which have been added by an admin. Users can read and also comment on blog.

##### Blog model
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_posts')
    slug = models.SlugField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=300, unique=True, null=False, blank=False,)
    sub_title_one = models.CharField(max_length=300, unique=True, null=False, blank=False,)
    blog_content_one = models.TextField(null=False, blank=False,)
    sub_title_two = models.CharField(max_length=300, default='', blank=True,)
    blog_content_two = models.TextField(default='', blank=True,)
    last_updated = models.DateTimeField(auto_now=True)

##### Comment model
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.OneToOneField(to=User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

#### Checkout App
- The checkout app is used to handle the chekout process of the store and enabled users purchase their products through the Stripe payments system.

##### Order model
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, default='', blank=True)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=30, default='', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

##### OrderLineItem model
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, default='', blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models. DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

#### Memberships App
- The memberships app is used to allow users to upgrade their membership to 'pro' or downgrade to 'beginner' if they have signed up but no longer which to be a 'pro'memnber.

##### StripeCustomer model
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

#### Products App
- The products app is used to store the details of an individual product and associate it with a particular category.

##### Category model
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='', blank=True)

##### Product model
    sku = models.CharField(max_length=254, default='', blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    material = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, default='', blank=True)
    image = models.ImageField(default='', blank=True)

#### Profiles App
- The profiles app is used to store information about the registered users of the site, this can be used for faster checkout and handles the membership level for discounts and access around the site.

##### UserProfile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=20, default='', blank=True)
    default_phone_number = models.CharField(max_length=20, default='', blank=True)
    default_street_address = models.CharField(max_length=80, default='', blank=True)
    default_town_or_city = models.CharField(max_length=40, default='', blank=True)
    default_county = models.CharField(max_length=30, default='', blank=True)
    default_postcode = models.CharField(max_length=20, default='', blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)

#### Tournaments App
- The tournaments app is used to store information about upcoming tournaments at the golf club.

##### Tournament model
    name = models.CharField(max_length=254, default='', blank=True)
    start_date = models.CharField(max_length=254, default='', blank=True)
    start_time = models.CharField(max_length=254, default='', blank=True)
    location = models.CharField(max_length=254, default='', blank=True)
    entry_fee = models.CharField(max_length=254, default='', blank=True)

### Database Schema
![DatabaseSchema](https://github.com/CarterStefan/wrottesley_golf_club/blob/master/static/UX/database_schema.png)

## Technologies Used
1. [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- HTML is the standard markup language for Web pages.

2. [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.

3. [JAVASCRIPT](https://www.javascript.com/)
- JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. The vast majority of websites use it for client-side page behavior,[11] and all major web browsers have a dedicated JavaScript engine to execute it.

5. [PYTHON](https://www.python.org/)
- Python is a programming language that lets you work quickly and integrate systems more effectively.

4. [JQUERY](https://jquery.com/)
- jQuery is a fast, small, and feature-rich JavaScript library.

5. [BOOTSTRAP](https://getbootstrap.com/)
- A modern responsive front-end framework based on Material Design.

6. [FONTAWESOME](https://fontawesome.com/)
- Font Awesome is a font and icon toolkit based on CSS and Less.

7. [GOOGLE FONTS](https://fonts.google.com/)
- Google Fonts is a library of more than a thousand free and open source font families, an interactive web directory for browsing the library, and APIs for using the fonts via CSS and Android.

8. [DJANGO](https://www.djangoproject.com/)
- Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

9. [BOTO3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3).

10. [GUNICORN](https://gunicorn.org/)
- Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

11. [PILLOW](https://pillow.readthedocs.io/en/stable/)
- Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

12. [POSTGRES](https://www.postgresql.org/)
- PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. 

13. [PSYCOPG2](https://pypi.org/project/psycopg2/)
- Psycopg is the most popular PostgreSQL database adapter for the Python programming language.

14. [STRIPE](https://stripe.com/en-gb)
- Stripe is an Irish-American financial services and software as a service company. The company primarily offers payment processing software and application programming interfaces for e-commerce websites and mobile applications.

15. [SQLITE3](https://www.sqlite.org/index.html)
- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

16. [GITPOD](https://www.gitpod.io/)
- Gitpod streamlines developer workflows by providing prebuilt, collaborative development environments in your browser - powered by VS Code.

17. [GITHUB](https://github.com/)
- Hosting for software development and version control using Git.

18. [HEROKU](https://www.heroku.com/home)
- Heroku is a cloud platform as a service supporting several programming languages.

19. [ADOBEXD](https://www.adobe.com/products/xd.html)
- Adobe XD is a vector-based user experience design tool for web apps and mobile apps, developed and published by Adobe Inc.

20. [Imgur](https://imgur.com/)
- Free image hosting website used for embedding links to images into websites.

## Deployment
### Local deployment
All code on this project was created in [Gitpod](https://www.gitpod.io/) for development. When development was nearing completion it was deployed to Heroku for hosting the webpage and AWS S3 for hosting the static files and all images.

If someone wishes to run this project locally, they should install the Gitpod chrome browser extension. Then:
- Go to https://github.com/CarterStefan/wrottesley_golf_club and click the green button titled 'Gitpod'

- In the gitpod settings click 'variables' and then 'add new variable' and add the following variables
    - STRIPE_SECRET_KEY = {Your stripe secret key}
    - DEVELOPMENT = {True}
    - STRIPE_BEGINNER_PRICE_ID = {Your stripe beginner price ID}
    - DOMAIN_URL = {Your domain url}
    - STRIPE_PRO_PRICE_ID = {Your stripe pro price ID}
    - STRIPE_WH_SECRET = {Your stripe webhook secret key}
    - STRIPE_PUBLIC_KEY = {Your stripe public key}
    - SECRET_KEY = {Your stripe secret key}
    - STRIPE_MEMBERSHIP_WH_SECRET = {your stripe membership webhook secret key}

    - Any stripe secret keys will need to be set up in the stripe interface once registered for an account

- In the command line type 'pip install -r requirements.txt'

- Migrate the models to the database by going to the command line and typing:
    - python3 manage.py makemigrations
    - python3 manage.py migrate

- Create a super user by going to the command line and typing:
    - python3 manage.py createsuperuser
    
    - Enter a email, username and password

- Load the data for the categories and the products by going to the command line and typing:
    - python3 manage.py loaddata categories
    - python3 manage.py loaddata Products

- Start the web app by going to the command line and typing:
    - python3 manage.py runserver
    
- Go to the admin page, by tacking /admin to the end of the url
    - Login with the credentials of the superuser you just created
    - Go to the blog option, and add a new blog using the form
    - Go to the Tournaments option, and add a new tournament using the form

### Heroku deployment
If someone wishes to deploy this project on Heroku, they should follow these steps:

- Within Stripe, create a new account and set up webhook endpoints for checkout/wh and memberships/webhooks
- Within Stripe, create two products for 'Pro' and 'Beginner' membership products

- Setup up an AWS account with the following:
    - AWS S3 Bucket
    - Bucket Policy
    - Group
    - Access Policy
    - User

- Setup a gmail account
    - Turn on 2-step verification
    - Create an app password by selecting 'mail' as the app and 'other' as the device type - set this as 'Django'

- Create a requirements.txt file by going to the CLI and typing 'pip freeze > requirements.txt'
- Create a procfile with the line 'web: gunicorn {the_name_of_your_heroku_app_here}.wsgi:application
- Save and push the code to github
- Create a Heroku account
- In Heroku, create a new app for the project with a unique name
- In Heroku, on the'resources page' search and select 'Heroku Postgress'
- In Heroku, set your config variables:
    - AWS_ACCESS_KEY_ID = {Your AWS_ACCESS_KEY_ID}
    - AWS_SECRET_ACCESS_KEY = {Your AWS_SECRET_ACCESS_KEY}
    - DATABASE_URL = {Your DATABASE_URL}
    - DOMAIN_URL = {Your DOMAIN_URL}
    - EMAIL_HOST_PASS = {Your EMAIL_HOST_PASSWORD}
    - EMAIL_HOST_PASS = {Your EMAIL_HOST_USER}
    - SECRET_KEY = {Your SECRET_KEY}
    - STRIPE_BEGINNER_PRICE_ID = Your STRIPE_BEGINNER_PRICE_ID}
    - STRIPE_MEMBERSHIP_WH_SECRET = {Your STRIPE_MEMBERSHIP_WH_SECRET}
    - STRIPE_PRO_PRICE_ID = {Your STRIPE_PRO_PRICE_ID}
    - STRIPE_PUBLIC_KEY = {Your STRIPE_PUBLIC_KEY}
    - STRIPE_SECRET_KEY = {Your STRIPE_SECRET_KEY}
    - STRIPE_WH_SECRET = {Your STRIPE_WH_SECRET}
    - USE_AWS = True
- Change the allowed hosts in settings.py to match your new heroku app
- In the CLI, type 'python3 manage.py makemigrations' then 'python3 manage.py migrate' to migrate your models to the new database
- In the CLI, import the products and categories by typing 'python3 manage.py loaddata categories' then 'python3 manage.py loaddata products'
- In the CLI, create a super user for your deployed site by typing 'python3 manage.py createsuperuser' and entering the required details
- Set Heroku to get changes from github automatically
- Save and push the code to github

## Testing

<details><summary>Navbar</summary>
<p>

- Nav bar is permanently visible at the top of the page for ease of access across the site.

##### Desktop
- The top part of the nav bar always shows three options - logo / my account / basket.
- Clicking the logo in the top left takes the user to the homepage.
- If a user clicks on the 'my account' button they will be shown a dropdown.
    - When logged out this dropdown shows the options - signup / login.
        - Clicking on signup takes the user to the sign up form.
        - Clicking on login takes the user to the login screen.
    - When logged in this dropdown displays the options - my profile / logout.
        - Clicking on my profile takes the user to the profile page.
        - Clicking logout takes the user to the confirm logout page.
    - When logged in as a superuser this dropdown displays the options - admin / my profile / logout.
        - Clicking admin takes the user to the Django admin page.
- The basket icon will always display the amount currently in the basket, or £0.00 if there is nothing.
    - Clicking on basket takes the user to the basket page.
- The bottom part of the nav bar shows four more navigation links to the site - tournaments / blog / store / memberships.
    - Clicking tournaments takes the user to the tournamnets page.
    - Clicking blog takes the user to the blog page.
    - Clicking store takes the user to the store page.
    - Clicking memberships takes the user to the memberships page.

##### Tablet / Mobile
- The top part of the nav bar always shows four options - hamburger menu / home / my account / basket.
- Clicking the hamburger option in the top left shows a fullscreen submenu.
- The fullscreen submenu displays the options - tournaments / blog / store / memberships.
    - Clicking tournaments takes the user to the tournamnets page.
    - Clicking blog takes the user to the blog page.
    - Clicking store takes the user to the store page.
    - Clicking memberships takes the user to the memberships page.    
- Clicking the home button takes the user to the homepage.
- If a user clicks on the 'my account' button they will be shown a dropdown.
    - When logged out this dropdown shows the options - signup / login.
        - Clicking on signup takes the user to the sign up form.
        - Clicking on login takes the user to the login screen.
    - When logged in this dropdown displays the options - my profile / logout.
        - Clicking on my profile takes the user to the profile page.
        - Clicking logout takes the user to the confirm logout page.
    - When logged in as a superuser this dropdown displays the options - admin / my profile / logout.
        - Clicking admin takes the user to the Django admin page.
- The basket icon will always display the amount currently in the basket, or £0.00 if there is nothing.
    - Clicking on basket takes the user to the basket page.
- Clicking the hamburger menu when the menu is oen closes the hamburger menu.

</p>
</details>

<details><summary>Footer</summary>
<p>

- Footer is located by scrolling to the bottom of any page across the site.
- In scenarios where the content of the page does not fill the entire viewport height, the footer will still remain at the bottom of the page-.
- The adress is permanently in the first column of the footer.
- The second column consists of two states depending on if you are logged in or logged out.
    - When logged out the footer links show the options - signup / login.
        - Clicking on signup takes the user to the sign up form.
        - Clicking on login takes the user to the login screen.
    - When logged in the footer links show the options - tournaments / blog / store / memberships.
    - Clicking tournaments takes the user to the tournamnets page.
    - Clicking blog takes the user to the blog page.
    - Clicking store takes the user to the store page.
    - Clicking memberships takes the user to the memberships page.
- The third column shows 3 social links - Facebook / Twitter / Instagram.
    - Clicking facbook takes the user to the WGC facebook page in an external tab.
    - Clicking twitter takes the user to the WGC twitter page in an external tab.
    - Clicking instagram takes the user to an instagram page, showing all pictures with the 'wrottesley golf club' location, in an external tab.
- The cloumns stack when the page becomes too thin for them to be alligned horizontaly.

</p>
</details>

<details><summary>Homepage</summary>
<p>

- Home page loads as intended as is responsive to all screen sizes.
- Hero image is the first feature you see, with a card giving the user the option to go to the store.
    - Clicking on 'visit store' takes the user to the store.
- The second feature is a banner advertising the pro membership.
    - Clicking 'see more' takes the user to the memberships page.
- The third feature is three cards with some navigation around the site to the pages - blog / memberships / store
    - Clicking on blog takes the user to the blog page.
    - Clicking on memberships takes the user to the memberships page.
    - Clicking on store takes the user to the store page.

</p>
</details>

<details><summary>Blog</summary>
<p>

- The blog page loads as intended as is responsive to all screen sizes.
- Each blog is displayed in a card.
    - The card header features the blog image.
    - The card body features:
        - The blog title is displayed as the card title.
        - The blog author is displayed underneath the title preceeded by the words 'A blog post by'.
        - The first 200 characters of the blog content one followed by...
        - A read more button.
        - The date when the blog was last updated preceeded by the words 'Last updated'.
        - If logged in as super user an 'add' button appears in the bottom right of the page which takes the super user to the add blog page.
        - If logged in as super user an 'edit' and 'delete' options are available in the card footer.
            - The edit button takes the super user to the edit page for that individual blog post.
            - The delete button deletes the blog and reloads the page. The deleted blog is no longer visible.
    - Clicking on the 'read more' button will take you to the correct blog post.

</p>
</details>

<details><summary>Blog Post</summary>
<p>

- The blog post page loads as intended as is responsive to all screen sizes.
- The top of the page features the correct main image full width.
- The page title shows the correct blog title.
- The blog author shows the correct author underneath the title preceeded by the words 'A blog post by'.
- A count of the number of comments on the individual blog post shows the correct number.
- The blog subtitles show the correct blog subtitles in a large, bold font.
- Blog content show the correct blog contents in body font.
- The bottom of the blog post shows the correct last updated date preceeded by 'Last updated on'.
- If logged in as super user an 'edit' and 'delete' options are available at the bottom of the blog.
            - The edit button takes the super user to the edit page for that individual blog post.
            - The delete button deletes the blog and goes to the main blog page. The deleted blog is no longer visible.
- The comment section appears below the blog and has 2 states:

#### A logged out user
- The number of comments count.
    - If there is one comment, the count correctly says '1 comment'.
    - If there is not one comment, the count correctly says '{{ number }} comments'.
- The line 'Login to leave a comment' is correctly displayed i
- Clicking the login word, the user is taken to the login screen.
- If there are comments for that blog, the correct comments for that blog post are displayed underneath.
- Only approved comments are shown.
- If there are no comments for that blog, the sentence 'No comments yet. Be the first to comment' is displayed.

#### A logged in user
- The number of comments count.
    - If there is one comment, the count correctly says '1 comment'.
    - If there is not one comment, the count correctly says '{{ number }} comments'.
- The text field to leave a comment is correctly displayed.
- There is a character count beneath which updates the left number as you type.
- When you go past 140 characters, the word count changes color to warn users they are approaching the limit.
- When you go past the 200 character limit, the 'post comment' button is disabled.
- Removing characters to make the character count below the 200 limit re-enables the 'post comment' button.
- Removing characters to make the character count below 140 characters, the text will go back to green.
- If there are comments for that blog, the correct comments for that blog post are displayed underneath.
    - Only approved comments are shown.
- If there are no comments for that blog, the sentence 'No comments yet. Be the first to comment' is displayed.
- Writing a comment and clicking 'post comment' will display a toast message and reload the page.
- The commentis then created as unapproved on the database for the superuser to approve.

</p>
</details>

<details><summary>Blog Edit</summary>
<p>

- The edit blog page loads as intended as is responsive to all screen sizes.
- All fields from the Django form are displayed.
- All fields have the current content for the correct blog post pre-filled.
- Selecting a new image will show the chosen image in a message underneath the current image.
- A toast message displays to say which blog post you are editing.
- Fields which are required have an asterisk next to them.
- Trying to confirm the form with a required field missing will not proceed and show the validation 'please fill in this field'.
- Removing content from none required fields and clicking confirm lets you proceed as expected.
- Clicking confirm after editing a field updates the blog correctly.
- Clicking confirrm will take the super user back to the blog post page, with the updated changes now showing.
- A toast message appears to confirm the change was successful.
- Clicking cancel will take the user back to the blog post with no edits made.

</p>
</details>

<details><summary>Blog Delete</summary>
<p>

- Clicking delete will reload the page with the deleted blog no longer visible.
- A toast message appears to confirm the deletion was successful.

</p>
</details>

<details><summary>Store</summary>
<p>

- The store page loads as intended as is responsive to all screen sizes.
- When the page is initially loaded, all products are displayed.
- The number of products correctly shows the correct number shown on the page.
- When a user searches for a product the results are filtered correctly based on the input. Showing results compared against the title, category and description.
- When a user searches for a product and results are found the product count reads "1 products found for 'search query here' " with the search query in bold.
- If the search returns no results, there are no products found and the product count reads "0 products found for 'search query here' " with the search query in bold.
- If a user tries to search with nothing entered into the box all products are shown with an error message to say 'Please enter something to search the store!'
- Clicking on each of the individual categories correctly filters the result by that category.
    - The product count is updated to show you have filtered by category and correctly says 'Accessories | 4 products', with the category in bold.
- The sort by is located above the products and has 4 options:
    - price (low to high)
    - price (high to low)
    - name (a - z)
    - name (z - a)
- Clicking each of the sort orders correctly sorts the products by the chosen sort order.
- This also works when sorting while filtering by a specific category.
- Each product is displayed in a card and correctly displays:
    - The product category.
    - The product image.
    - The product title.
    - The product price.
- Clicking the product image takes the user to the correct product detail page.

</p>
</details>

<details><summary>Product Details</summary>
<p>

- The product detail page loads as intended as is responsive to all screen sizes.
- The page consists of the product:
    - Image
    - SKU 
    - Title 
    - Price 
    - Category
    - Quantity selector
    - Size selector (if applicable)
    - Description 
    - Back to products button
    - 'You may also like' specification
- All of the above are correctly displayed for the product that was just clicked on the store page.
- Clicking the category takes the user to the store page with only products from that category showing.
- Clicking the plus button makes the quantity count increase by one.
- If the number is 99, the plus is disabled.
- Clicking the minus button makes the quantity count decrease by one.
- If the number is 1, the minus button is disabled.
- The minus button is disabled when the page first loads as the number is one by default.
- If a user types a number which is less 1 or greater than 99 and tries to add to basket, a validation message appears.
- If the product has sizes, the size selector is visible.
- The size selection is on medium by default.
- Clicking the dropdown shows the other size options available.
- Selecting a different size changes the option in the dropdown.
- Clicking the 'add to basket' button add the correct item to the basket with the correct size and quantity selected.
- A toast message appears with the correct item, sizes (if applicable) and quantity that the user has just added.
- Clicking the 'back to products' button, the user is taken to the store page showing all products.
- The 'you may also like section is displayed underneath the product details. 
- Only items from the category of the product you are on are displayed.
- Clicking one of these products takes you to the correct product details page.

</p>
</details>

<details><summary>Basket</summary>
<p>

- When an item is added to the basket, the price in the nav bar is updated and a toast message appears with details of:
    - The item which was just added to the basket.
    - The current count of the items in the basket.
    - A list of all the items showing:
        - Product title
        - Product price
        - Size (will show as N/A if product has no sizes)
        - Quantity of that item with that size (if applicable) in the basket
    - The basket total
    - A view basket button
- Clicking 'view basket' will take the user to the main basket page.
- The basket page is also accessed by clicking the basket icon in the nav bar.
- The basket page loads as intended as is responsive to all screen sizes.
- If the user has no items in their basket the page shows a message informing the user they have no items in their basket with a button to go to the store.
    - Clicking the 'go to store' button takes the user to the store page with all products visible.
- If the user does have items in their basket.
    - The page shows a list view of all the products in the basket.
    - For each item in the basket the user can see:
        - Product price
        - Product title
        - Size (will show as N/A if product has no sizes)
        - Quantity displayed in a quantity picker
    - While testing that the user can not enter an amount larger than 99 I discovered a flaw where a user can enter more than the max 99. 
        - This was fixed by disabling typing on the quantity fields, so a user will now select the item quantity using the plus and minus buttons.
    - When a user updates the quantity and clicks 'update' the page relaods and correctly shows the new amount.
    - When a user clicks the delete icon, the page is reloaded and correctly shows the basket with the deleted item no longer showing.
    - A toast message shows for each of these actions.
    - The second part of the page is a summary of the total amount of the basket.
    - This shows:
        - Basket total
        - Membership discount
            - If the member is a pro member, the membership discount shows at 10% of the basket total
            - If the member is a beginner member (or not signed up for membership) the membership discount shows as 0.00
        - Delivery
            - If the member is a pro member, the delivery shows at 0.00
            - If the member is a beginner member (or not signed up for membership) the delivery shows as 10% of the basket total
        - total
            - This is a calculation of basket total + delivery - membership discount
    - Clicking 'checkout' takes the user to the checkout page where they payment will be processed.

</p>
</details>

<details><summary>Checkout</summary>
<p>

- The checkout page loads as intended as is responsive to all screen sizes.
- The page shows customer details, delivery details, and a summary of the order amounts.
- The details form consists of three fields:
    - Full name
    - Email adress 
    - phone number

    - All three fields load correctly.
    - All three fields are mandatory and validation works correctly on all three fields.
    - If the user is logged in and has profile information saved, these fields will be pre populated.
    - If the user is logged in and has not saved profile information, the email field will be pre populated.

- The delivery form consists of five fields:
    - Street address 
    - Town or city 
    - Postcode 
    - County or state 
    - Country

    - All five fields load correctly.
    - Three fields are mandatory, street address / town or city / country, and validation works correctly on all three fields.
    - If the user is logged in and has profile information saved, these fields will be pre populated.
    - If the user is logged in and has not saved profile information the fields appear with their placeholders

- The option to save profile information appears when a user is logged in only.
- The prompt to login or create account appears when a user is logged out.
    - Clicking 'create account' takes the user to the sign up page.
    - Clicking 'login' takes the user to the login page.
- Clicking save information and submitting the form correctly saves the information to the profile page.

- Filling the card information field with invalid information will prompt a validation error from stripe.
- Submitting the form with invalid information will prompt a validation error from stripe.

- The second part of the page is a summary of the total amount of the basket.
    - This shows:
        - Basket total
        - Membership discount
            - If the member is a pro member, the membership discount shows at 10% of the basket total
            - If the member is a beginner member (or not signed up for membership) the membership discount shows as 0.00
        - Delivery
            - If the member is a pro member, the delivery shows at 0.00
            - If the member is a beginner member (or not signed up for membership) the delivery shows as 10% of the basket total
        - total
            - This is a calculation of basket total + delivery - membership discount
    - Clicking 'edit basket' takes the user to the basket page where they can ammend their order.
    - The final summary confirms the amount the card will be charged and is the same amount at the total.

- Clicking 'complete order' will start the stripe payment process.
- The form become completely hidden behind the button, which has now become disabled and turned into a 'spinny' while the payment processes.
- Once confirmation from stripe has come through, the user is taken to a success page which will show a summary of the order.

</p>
</details>

<details><summary>Memberships</summary>
<p>

- The profile page loads as intended as is responsive to all screen sizes.
- If a user goes to the memberships page while they are logged out, they are redirected to the login page.
- If a user has not previously subscribed to the plus membership, they have no membership status, but are regarded as a beginner.
- A user going to the page with no membership status will see the page encouraging them to sign up to plus membership.
    - Clicking the 'subscribe' takes the user to the stripe checkout page, where they need to provide.
        - Email
        - Card information
        - Country
        - Postcode
    - When the checkout session is completed a new customer is created on the Stripe customer on the stripe dashbaord with the 'pro' subscription.
    - When the checkout session is completed a new entry is created on the StripeCustomer model with the correct member.
    - When the checkout session is completed the correct users profile membership status is updated to 'pro'.
- A user going to the page with 'pro' membership status will see the page giving them the option to downgrade.
    - Clicking the 'downgrade' button takes the user to the homepage and show a toast message confirming the account has been downgraded.
    - Clicking the 'downgrade' button updates the membership status on the Stripe customer on the stripe dashbaord with the 'beginner' subscription.
    - Clicking the 'downgrade' button updates the correct users profile membership status to 'beginner'.
- A user going to the page with 'beginner' membership status will see the page giving them the option to subscribe again (as they have already been a 'pro' member previosuly).
    - Clicking the 'subscribe' button takes the user to the homepage and show a toast message confirming the account has been upgraded.
    - Clicking the 'subscribe' button updates the membership status on the Stripe customer on the stripe dashbaord with the 'pro' subscription.
    - Clicking the 'subscribe' button updates the correct users profile membership status to 'pro'.    

</p>
</details>

<details><summary>Profile</summary>
<p>

- The profile page loads as intended as is responsive to all screen sizes.
- The page shows user delivery details, and a summary of the users previous orders
- The details form consists of three fields:
    - phone number
    - Street address 
    - Town or city 
    - County or state
    - Postcode 
    - Country

    - All six fields load correctly.
    - If the user is logged in and has profile information saved, these fields will be pre populated.
    - If the user is logged in and has not saved profile information previously, the fields appear with their placeholders.
    - None of these fields are mandatory.
- Clicking 'update information' will save the users information and relaod the page with the new information pre populated.

- The second part of the page is a summary of the users previous orders.
    - This is shown in the form of a table with the following fields:
        - Order number 
        - Date 
        - Items 
        - Grand total
- Clicking on the order number takes the user to the previous order page with the correct information shown similar to the checkout success page.

</p>
</details>

<details><summary>Tournaments</summary>
<p>

- The tournaments page loads as intended as is responsive to all screen sizes with the exception compared to other pages where the table will have a horizontal scroll on mobile.
- The page shows all the tournaments currently in the tournaments database with the following fields:
    - Tournament name
    - Start date
    - Start time
    - location
    - Fee 
- All information is shown correctly, and when adding a new entry into the database the new entry appears on the page.
- The fee column changes depending on the users membership status.
    - If a user is a beginner (or not signed up for membership), the entry fee is shown as is on the database entry.
    - If a user is a pro member, the membership fee shows as Free, with the original price striked out.

</p>
</details>

### Validation
#### Pages
- I used [W3C](https://validator.w3.org/#validate_by_uri) validator the all pages accross my site.

All pages passed the validator with no errors or warnings.


#### CSS
- I used [W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) validator the three CSS files in my project:
    - base.css
    - memberships.css
    - blog.css

All three files passed the validator with no errors or warnings.

#### Pep8
- All python files (excluding those which come as built in with django) pass the [PEP8](http://pep8online.com/) online code check.

## Acknowledgments
#### Code
- The store section of the website was largely created by following the tutorials from the Boutique Ado project from [CodeInstitute](https://codeinstitute.net/). The code was adapted to suit the needs of my store and fit with the branding of my project. This code included the bag, store products and checkout process.

- The blog application was created by following along with the [DjangoCentral](https://djangocentral.com/building-a-blog-application-with-django/) post 'Building a blog application with django'. I then adapted the code to fit with my project.

- The memberships subscription logic was built with help from the [TestDriven](https://testdriven.io/blog/django-stripe-subscriptions/) tutorial on integrating stripe subscription services.

- I took the code for the dropdowns in the wireframes section of the readme from [Joyrexus](https://gist.github.com/joyrexus/16041f2426450e73f5df9391f7f7ae5f).

#### Media
[ClubHouse](https://www.clubhousegolf.co.uk/)
- Used for all product images, details and descriptions

[StAndrews](https://www.standrews.com/play/the-home-of-golf/blog)
- Used for all blog Contents

[AllSquareGolf](https://www.allsquaregolf.com/golf-courses/england/wrottesley-golf-club)
- Used for hero image on site

[Unsplash](https://unsplash.com/s/photos/golf)
- Used for stock images of golf courses used on blogs, memberships and homepage

#### Thanks
- I would like to thank [CodeInstitute](https://codeinstitute.net/) for providing the lessons on full stack frameworks and the tutorials on how to set up a store. Also, a big thankyou to the tutor support team, who not only helped with this project, but also throughout the last year.

- A big thank you also to my mentor Gbenga, whose encouragement and support has helped me through this project and throughtout my time on the course.
