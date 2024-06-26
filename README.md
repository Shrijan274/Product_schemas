"""
    Introduction-

    Product Schema Generator-

    This application allows user to create,read,update and delete the properties of products.
    The user can define schemas for each product.
    This application has a formm based interface for data entry and management.

    Input : Properties of a product
    Output: A form displaying schemas of the product, a page enabling edit and delete of the product
    
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

        USE_CASE_2 =
       *goal - User wants to edit schemas of a desktop

       *pre conditions- 
       - User has access to website
       - User has already entered details of desktop previously

       *mainflow-
        - User goes to productschema web application and enters login page.
        - if user is registered, by entering credentials, user is able to login into productschema page
        - if user is not registered, user access the sign up page to register themselves
        - user clicks on "view-entries" opening a view page
        - user selects the edit button of a product which they want to edit
        - user is redirected to productschema page with the data of product already filled in.
        - user can edit the data like 
            eg- if user wants to add a new property(size) , user clicks add row button which gives a new and user enters the properties of size
                (24 in,28 in,32 in) 
        - user clicks preview button and sees the size property added in form.
        - user clicks update button which updates the data of product.
        - if user wants to log out, they can click the log out button which logs out the user.

        *post conditions-
        - User has updated the schemas of the desktop.
        - User can view the update form of desktop product.


