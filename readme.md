# Todo List

In this challenge we're going to create a basic CRUD app with just a single record type so that you can focus on practicing the basic actions for CRUD.

We'll build a basic TODO app that lets us manipulate a list of Todos that we want to complete. To make things a bit easier, we'll provide the some descriptions for each section of the app. Feel free to look back at the lesson for the day to refresh your memory as well.

This challenge is empty for you to practice building something from scratch. There are many ways we could implement a TODO app. For our purposes, we'll stick to the seven basic actions we learned:

  ```text
  GET list
  GET show
  GET new
  POST create
  GET edit
  PUT update
  DELETE destroy
  ```

## Release 0: Getting Ready

Start by creating a new virtual environment and then activate it. 

`python -m venv venv source venv/bin/activate`
`source venv/bin/activate`

Once you have your virtual environment up and running you can tell pip to download all the requirements for this app by running `pip install -r requirements.txt`. Make sure you are in the main directory of the repo (the one with the readme in it).

Create your project, app, models and get started! Let's say a `Todo` item has a title and description. Feel free to add anything else you feel is crucial for a `Todo` to have. Next, let's start CRUD!

## Release 1: Create
Since we need a way to get records into our system, we'll start with the routes to create new records.

If the user makes a GET request to `/todos/new` they should: 
  * See a form with the required form fields to create a `Todo` objet

Submitting the form makes a POST request to `/todos`:
  * It should create the new Todo record in the database. 
  * After the new Todo is created, the user should be redirected to view that Todo.

## Release 2: Read
Next we need to be able to read Todo records. Let's start with the `show` action - here are the requirements:

A GET request to `/todos/<id>` (where id will be a number corresponding to id of the record you want to view) will:
  * Show the title and description of the Todo 
  * Show a link to edit the existing Todo
  
A GET request to `/todos` should: 
  * Show a list of all Todos that exist
  * Show links to each Todo individually
  * Show a link to create a new Todo
 
## Release 3: Update

Now that we can list records, let's build the functionality to manipulate those records.
A GET to `/todos/<id>/edit`:
  * Displays a form with the current title and description already filled out in each form field 
  
Submitting the form: 
  * Updates the existing Todo with the new provided values
  * Redirects you back to the show page

## Release 4: Destroy

Finally, let's give users the ability to destroy an existing Todo. Since we haven't really modeled a way to mark a Todo as complete, we'll use this to complete Todos for the moment.

A POST request to `/todos/<id>/delete`:
  * Deletes the existing Todo
  * Redirects you to the list page
