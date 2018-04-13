# SSW-695 Project

[logo]: https://github.com/MaryamAlMansour/695-CodeIn/blob/master/codein_server/Documentation/Maktab%207ukomi%20logo.png

## CodeIn
Platform for coders to network and freelance. 

## To install the required Python packages...

* At the command prompt: pip install -r requirements.txt

## Commands:

* At the command prompt: python manage.py [command], where command is one of the following:

command | function
------------ | -------------
makemigrations | Makes the migrations to create the SQL tables.
migrate | Runs the migrations, tells you what changed in your tables, ex new table.
runserver | Runs the app.
createsuperuser | Create superuser to manage the app.


## Main views of Django adminstartion:

* Add the designated url after the local host, http://127.0.0.1:8000/[URL]

URL | view
------------ | -------------
/admin | Welcome page that has all the apps of codein project. 
/admin/server/user/ | Create users page.
/admin/platforms/portfolio/ | Create portfolio for users page.
/admin/platforms/project/ | Add projects for users page. 
/admin/platforms/contact/ | Create connections between two users,Follow or Unfollow. 

## API URL views:

* Use Postman to test the designated urls. 


URL | Method | Headers | Body | View
------------ | ------------- | ------------ | ------------- | ------------
/rest-auth/login/| Post | - | keys + values: username and password |  Shows JWT Token and other information
/rest-auth/registration/ | Post | - | keys + values: username, pass1, pass2, email | Shows JWT Token and other information
/platform/portfolio/ | Get | key:Autherization, value:JWT [TOKEN] | - | Shows all users portfolios
/platform/portfolio_write/ | Post| - | keys + values:user id and image file | shows the posted portfolio
/platform/project/ | Get | key:Autherization, value:JWT [TOKEN] | - | shows all projects
/platform/project_write/ | Post | - | keys: user, name, description | shows the created project
/platform/project/get_search_proj/?search_proj_name=[proj name] | Get | key:Autherization, value:JWT [TOKEN] | - | filter projects for the given name
/platform/project/get_search_proj/?search_user_projs=[username] | Get | key:Autherization, value:JWT [TOKEN] | - | filter projects to include only the specified user projects. 
/server/user/get_search_user/?search_user_name=[username] | Get | key:Autherization, value:JWT [TOKEN] | - | filter specified user by username
/server/users/get_search_user/?search_email=[email] | Get | key:Autherization, value:JWT [TOKEN] | - | filter the specified user by email
/platform/followers/| Get | key:Autherization, value:JWT [TOKEN] | - | shows all followers. 






