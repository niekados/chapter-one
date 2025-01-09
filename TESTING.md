# Testing

## Index

- [Validation](#validation)
    - [HTML Validation](#html-Validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [PEP8 Validation](#pep8-validation)
    - [Lighthouse Testing](#lighthouse-testing)
- [Testing User Stories](#testing-user-stories)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Known Bugs](#known-bugs)

## Validation

### HTML Validation

The HTML code for the Journey app was validated using the [W3C Markup Validation Service](https://validator.w3.org/). 

- **Validation Method**:
  - URI validation was employed for all pages that did not require user login.
  - Direct input validation was used for pages that required a login. The HTML code was extracted by viewing the page's source directly. 

#### Warnings:
- The `type` attribute is unnecessary for JavaScript resources. This warning appeared multiple times in the code but was left unchanged as it is not critical and does not impact functionality.

| Page                 | Warnings                          | Errors                         |
|----------------------|-----------------------------------|--------------------------------|
| index                | JS type attribute                 | None                           |
| add author           | JS type attribute                 | None                           |
| authors list         | JS type attribute                 | None                           |
| confirm author delete | JS type attribute                 | None                           |
| edit author          | JS type attribute                 | None                           |
| manage authors       | JS type attribute                 | None                           |
| add book             | JS type attribute                 | None                           |
| book detail          | JS type attribute                 | None                           |
| books list           | JS type attribute                 | None                           |
| confirm book delete  | JS type attribute                 | None                           |
| edit book            | JS type attribute                 | None                           |
| manage books         | JS type attribute                 | None                           |
| shopping cart        | JS type attribute                 | None                           |
| checkout             | JS type att, empty heading        | None                           |
| checkout success     | JS type attribute                 | None                           |
| my library           | JS type attribute                 | None                           |
| profile              | JS type attribute                 | None                           |
| sign in              | JS type attribute                 | None                           |
| sign out             | JS type attribute                 | None                           |
| sign up              | JS type attribute                 | None                           |

### CSS Validation

The CSS files were validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) with the **Direct Input** method.

#### Validation Results

| CSS File       | Warnings                        | Errors                          |
|----------------|---------------------------------|---------------------------------|
| base.css       | None                            | None                            |
| checkout.css   | None                            | None                            |
| profiles.css   | None                            | None                            |

### JavaScript Validation

The JavaScript files were validated using the [Esprima JavaScript Validator](https://esprima.org/demo/validate.html).

#### Validation Results

| JavaScript File          | Warnings                         | Errors                          |
|--------------------------|----------------------------------|---------------------------------|
| elements.js              | None                             | None                            |
| base.html script section | None                             | None                            |

### PEP8 Validation

All Python files were validated using the [Code Institute PEP8 Validation Tool](https://pep8ci.herokuapp.com/). The results are summarized below:

| File Name                      | Errors          |
|--------------------------------|-----------------|
| **Authors App**                |                 |
| admin.py                       | None            |
| forms.py                       | None            |
| models.py                      | None            |
| urls.py                        | None            |
| views.py                       | None            |
| **Books App**                  |                 |
| admin.py                       | None            |
| forms.py                       | None            |
| models.py                      | None            |
| urls.py                        | None            |
| views.py                       | None            |
| **Cart App**                   |                 |
| context.py                     | None            |
| urls.py                        | None            |
| views.py                       | None            |
| **Chapter One Project**        |                 |
| urls.py                        | None            |
| views.py                       | None            |
| **Checkout App**               |                 |
| admin.py                       | None            |
| forms.py                       | None            |
| models.py                      | None            |
| signals.py                     | None            |
| urls.py                        | None            |
| views.py                       | None            |
| webhook_handler.py             | None            |
| webhooks.py                    | None            |
| **Home App**                   |                 |
| admin.py                       | None            |
| forms.py                       | None            |
| models.py                      | None            |
| urls.py                        | None            |
| views.py                       | None            |
| **Library App**                |                 |
| admin.py                       | None            |
| models.py                      | None            |
| urls.py                        | None            |
| views.py                       | None            |
| **Profiles App**               |                 |
| forms.py                       | None            |
| models.py                      | None            |
| urls.py                        | None            |
| views.py                       | None            |

### Lighthouse Testing

## Testing User Stories

### **Visitor User Stories**

- **As a visitor**, I can view the site’s home page so that I can understand its purpose and intentions. 
<img src="documentation/screenshots/about-us.png" alt="About Us" style="width:50%;">

- **As a visitor**, I can use the navigation bar to explore different sections of the site so that I can easily access the content I need.  
<img src="documentation/screenshots/navbar.png" alt="Navbar" style="width:50%;">

- **As a visitor**, I can click on links in the footer so that I can access additional information, such as the privacy policy and social media links.  
<img src="documentation/screenshots/footer.png" alt="Footer" style="width:50%;">

- **As a visitor**, I can enter text into the search bar so that I can quickly find books.
<img src="documentation/screenshots/navbar.png" alt="Search" style="width:50%;">

- **As a visitor**, I can view a list of all available books so that I can browse through them.  
<img src="documentation/screenshots/books.png" alt="Books" style="width:50%;">

- **As a visitor**, I can filter books by genre so that I can easily find books that match my interests.
<img src="documentation/screenshots/books.png" alt="Books" style="width:50%;">

- **As a visitor**, I can view detailed information about a book so that I can make an informed purchase decision.
<img src="documentation/screenshots/book-details.png" alt="Books Detail" style="width:50%;">

### **User Authentication User Stories**

- **As a user**, I can register for an account so that I can access personalized features like purchasing books and managing my library.  
<img src="documentation/screenshots/sign-up.png" alt="Sign Up" style="width:50%;">

- **As a user**, I can log in to my account so that I can access my profile and purchased books. 
<img src="documentation/screenshots/sign-in.png" alt="Sign In" style="width:50%;">

- **As a user**, I can log out of my account so that I can prevent unauthorised access.
<img src="documentation/screenshots/sign-out.png" alt="Sign Out" style="width:50%;">

- **As a user**, I can edit my profile details so that I can keep my personal and billing information up to date. 
<img src="documentation/screenshots/my-profile.png" alt="Profile" style="width:50%;">


### **Shopping Cart and Checkout User Stories**

- **As a user**, I can add books to my cart so that I can purchase items.  
<img src="documentation/screenshots/add-to-cart-button.png" alt="Add to cart" style="width:50%;">

- **As a user**, I can view the contents of my cart so that I can see which books I plan to purchase and their total cost.
<img src="documentation/screenshots/shopping-cart.png" alt="Cart" style="width:50%;">

- **As a user**, I can remove books from my cart so that I can adjust my selections before checkout.
<img src="documentation/screenshots/shopping-cart.png" alt="Cart" style="width:50%;">

- **As a user**, I can complete my purchase using a secure payment method so that I can download my books immediately.
<img src="documentation/screenshots/check-out.png" alt="Checkout" style="width:50%;">

- **As a user**, I can receive a confirmation email after completing a purchase so that I have a record of my order details.
<img src="documentation/screenshots/email-confirmation.png" alt="Email Confirmation" style="width:50%;">

### **User Library User Stories**

- **As a user**, I can view my purchased books in a library so that I can keep track of my collection.  
<img src="documentation/screenshots/my-library.png" alt="My Library" style="width:50%;">

- **As a user**, I can download my purchased books so that I can read them.
<img src="documentation/screenshots/download-button.png" alt="Download Button" style="width:50%;">

### **Author Profiles User Stories**

- **As a user**, I can view a list of all authors on a dedicated page so that I can explore their profiles.
<img src="documentation/screenshots/authors-list.png" alt="Authors" style="width:50%;">

### **Admin Content Management User Stories**

- **As an admin**, I can add new books to the catalog so that they are available for users to browse and purchase.
<img src="documentation/screenshots/add-book.png" alt="Add Book" style="width:50%;">

- **As an admin**, I can edit existing books so that I can update their details or pricing when needed.
<img src="documentation/screenshots/edit-book.png" alt="Edit Book" style="width:50%;"> 

- **As an admin**, I can delete books from the catalog so that I can remove outdated or incorrect listings. 
<img src="documentation/screenshots/confirm-book-delete.png" alt="Delete Book" style="width:50%;">

- **As an admin**, I can add new authors so that I can feature them in the catalog and link their books. 
<img src="documentation/screenshots/add-author.png" alt="Add Author" style="width:50%;">

- **As an admin**, I can edit author profiles so that I can update their information.
<img src="documentation/screenshots/edit-author.png" alt="Edit Author" style="width:50%;">

- **As an admin**, I can delete authors so that I can remove profiles if needed.
<img src="documentation/screenshots/confirm-delete-author.png" alt="Delete Author" style="width:50%;">

## Manual Testing



## Bugs

## Known Bugs