"""
    Introduction-

    Prerequisites-
    
    Django
    datatables
    redis
    drf

    connect to redis server before running the application.

    Product Schema Generator-

    This application allows user to create,read,update and delete the properties of products.
    The user can define schemas for each product.
    This application has a form based interface for data entry and management.

    Input : Properties of a product
    Output: A form displaying schemas of the product, a page enabling edit and delete of the product

    Features - 

    User Authentication - 
    - Login: Allows registered users to log in with their credentials.(Email, Password)
    - Signup: New users can register by providing personal details.(Email, Firstname, Lastname, Password, confirm password)
    - Password Reset: Users can reset their password by entering their email(Email, password, confirm password)

    Product Schema Management
    - Create: Users can create new product schemas by entering product schemas in product schemas page
    - Read: Users can view the schemas they have created in CRUDview
    - Update: Users can edit existing product schemas and update the schema of property
    - Delete: Users can delete existing product schema

    Understanding the web application-


    Product Schema page -

    This page is used to create a new product schema.

    "View Entries" = link redirecting to page showing the product entries (CRUDview)
    "log out" = logs out the user from product schema page
    "Schema name" = name of the product to be entered
    "Field name" = name of property/Schema to be entered
    "data type" = if value is characters then String , if value are numbers then number
    "lenght" = if string is selected , describe the lenght of each value, if number is selected, no need to enter any lenght
    "is required" = if the property is mandatory then check it, if not mandatory then no need to check it
    "look up"= the values of property to be entered
    "css" = any styles to be reflected in form for specified property is entered here
    "note" = description of property is to be entered
    "preview" = this button displays a action type form of schemas of the product
    "add row" = this button generates a new row in table for additional properties to be entered.

    CRUDview -

    This page is used to view the entries of products

    "add new schema" = this link redirects to Product schema page to create a new product schema
    "Table" = the table has 5 columns Sr.no, Product Name(name of the products), Is Active(true is product is active, false if product is not active), Pencil Icon(Edit button to edit the schema),
        Trash Icon(Delete button to delete the schema)
    "search" = search bar to search for a particular product.
    - Paging to browse through the products.

    Home Page - 
    
    This page is used to login into Product Schema page
    - Email and password field to login
    "sign up" = A new user to register themselves
    "forgot password" = A way to recover a forgotten password

    Sign Up Index - 
    
    This page is used to register a new user
    - (Email, Firstname , Last name, Password, Confirm password fields) required credentials to sign up a new user.
    "Login" = Login page link

    Forgot password index - 
    - Email field which checks if email exists
    - If email exists "Reset Password" button redirects to "reset password" page

    Reset Password -
    - (Email, New password, Confirm new password) fields to reset the password of a email id.
    "Back to login page" = link which redirects to login page.


    Workflow:

    - User goes to productschema web application and enters login page.
    - if user is registered, by entering credentials, user is able to login into productschema page
    - user enters name of product and sees a table where user can enter the properties of product
    - there is a "preview" button which displays a form.
    - by using "save" button saves the data of product.
    - at the top of the same page there is a link "View Entries" which displays all the products entered
        -there user can delete the data of a product
        -there user can edit the data which redirects to product schemas page with the data of product already filled in,here user can edit and update it. 	
    - the other "log out" button which logouts the user 

    - if user wants to register themself, there is a link in "login" page redirecting to a "signup" page where user can enter personal details and register
        themselves.
    - incase user forgets their password, there is a "reset password" link to reset their password, where user enters their email, if email exists user can 
        enter their new password.
    
    CREATE page-
    - this page is accessible after user is able to login into the product schema application
    - a input field appears which accepts the name of product
    - after ging input and entering, a table appears displaying 7 columns(property name,data type, lenght, checkbox, values to be entered, css is needed, description)
    - user may enter 1 property in that field, if user wants to enter another property , by clicking on "add row" button a new row is generated where another property details can be filled
    - after entering all properties, by clicking on preview button a action-type form is displayed to see how the properties of product appear
    - if a property has only 1 value a simple input field appears, if property has multiple values they appear as a drop down box.
    - by clicking on "config save" button, the product schema is saved successfully.
        (If a property has multiple values, values must be seperated by comma(,) 
            example: values are black blue red , they must be entered as black,blue,red)

    VIEW page-
    - if user wants to view the entries of the products, a link "view-entries" exist in product schemas page
    - Clicking on that redirects to view page 
    - A table appears displaying the products describing "product name" and "status" of product with 2 options beside each product to edit or delete it
    - To edit any product user may click on pencil button , redirecting them to product schema page with the product data already filled in
    - user may change or add new properties and update the product schema
    - To delete any product user may click on delete button, a pop-up window appears , after confirming it the product is successfully deleted.

    Usecases: 
        USE_CASE_1 =
        *goal - User wants to enter schemas of a mobile phone

        *pre conditions - 
        - User has access to website
        - User knows the properties of mobile phone 

        *mainflow-
        - User goes to productschema web application and enters login page.
        - if user is registered, by entering credentials, user is able to login into productschema page
        - if user is not registered, user access the sign up page to register themselves
        - user enters name of product and sees a table where user can enter the properties of product
        - for a mobile phone , user enters model,storage,colour,Price,RAM,Display type,size,Weight,Brand,Battery,Charging type,Cameras, Resolution of camera,Speakers,Connectivity,OS,Features,Warranty,Availability etc
        - User clicks on preview button which shows them an action type form displaying the schema of the product.
        - User clicks on save button which saves the data of product.
        - if user wants to logout, they can click on logout button which is on top right of page which logs out the user.

        *post conditions-
        - User has schemas of the products saved.
        - user can view the action type form of properties of their products
-----------------------------------------------------------------------------
        USE_CASE_2 =
        *goal - User wants to edit schemas of a desktop

        *pre conditions- 
        - User has access to website
        - User has already entered details of desktop previously
        - User knows the properties they want to add.

        *mainflow-
        - User goes to productschema web application and enters login page.
        - by entering correct credentials, user is able to login into productschema page
        - user clicks on "view-entries" opening a view page
        - user selects the edit button of a product which they want to edit
        - user is redirected to productschema page with the data of product already filled in.
        - user can edit the data like 
            eg- if user wants to add a new property(size) , user clicks add row button which gives a new and user enters the properties of size
                (24 in,28 in,32 in) 
        - user clicks preview button and sees the size property added in form.
        - user can see the properties as a drop down menu displaying 24 in, 28 in, 32 in as schema.
        - user clicks update button which updates the data of product.
        - if user wants to log out, they can click the log out button which logs out the user.

        *post conditions-
        - User has updated the schemas of the desktop.
        - User can view the update form of desktop product.
----------------------------------------------------------------------------------------
        USE_CASE_3 =
        *goal - User wants to delete schemas of a laptop

        *pre conditions- 
        - User has access to website
        - User has already entered details of laptop previously

        *mainflow -
        - User goes to productschema web application and enters login page.
        - by entering correct credentials, user is able to login into productschema page
        - user clicks on "view-entries" button which opens the view page
        - user selects the product(select) they want to delete 
        - user clicks on delete button which gives a alert message to user
        - as user confirms the alert message the product is removed from view table and data base

        *post conditions-
        - User has deleted the schemas of the laptop.
-----------------------------------------------------------------------------------------

"""