# cookiecutter_django
This is a Cookie Cutter template for creating Django Projects with pre-configurations and tools built in.

## CookieCutter
A command-line utility that creates projects from cookiecutters (project templates).
[https://github.com/cookiecutter/cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Tutorial
Install Cookie Cutter:
```
pip install --user cookiecutter
```

Init project creation:
```
cookiecutter https://github.com/enricorobazza/cookiecutter_django
```

Then just answer the questions for the features you want.

## Features
### Default:
- Static URL and Static Root setup
- Compress sass setup
- PyLint
- Timezone and language to Sao Paulo and Portuguese (BR)
- .gitignore Django
- Admin customizations example
- FontAwesome included

### Optional:
- Heroku Config
- Bootstrap Config
  - DataTables
  - BootstrapSelect
  - MomentJS
  - JQuery
  - Bootstrap customization with SASS
- Custom Accounts (custom User model with login by e-mail)
  - Urls, views and templates for: login, logout, password reset and signup.
- Login Required Middleware (block unauthorized access to all pages except listed) 
  - Only works if custom_accounts is enabled
- Extras App (app with custom components and widgets)
  - Only works if bootstrap is enabled
  - BaseView: component that takes a Model and a Form and create fully functional views for inserting, deleting, listing, updating...
  - DataTable: uses DataTable.js to create a listing view with loading via ajax (includes search, order...)
  - FilterWidget: widget for select inputs that must be filtered by another select input.
  - InsertWidget: widget for select inputs that must have a popup for inserting another options (take a Form as parameter)
- Extras Example:
  - Only works if extras_app is enabled
  - Includes an example of extras_app being used.
- React:
  - React integration with Django via Webpack and Babel
  - Webpack dev server for hot reloading
  - EsLint
  - Prettier
  - PropTypes
- API:
  - Django_rest_framework configured
  

