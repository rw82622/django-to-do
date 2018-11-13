# Todo List
====================

In this challenge, we're going to create a basic CRUD app with just a single
record type, so that you can focus on practicing the basic actions for a CRUDdy
controller.

We'll build a basic TODO app that lets us manipulate a list of tasks that we
want to complete. To make things a bit easier, we'll provide the test
descriptions for each section of the app. Feel free to look back at the lesson
for the day to refresh your memory as well.

There are many ways we could implement a TODO app. For our purposes, we'll stick
to the seven basic actions we learned:

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

`python3 -m venv venv source venv/bin/activate`

Once you have your virtual environment up and running you can tell pip to download all the requirements for this app by running `pip install -r requirements.txt`. Make sure you are in the main directory of the repo (the one with the readme in it).

Next set up the database `djangotodolist` by running `createdb djangotodolist`.

Then run the migrations with `python3 manage.py migrate`


The model and migration for this activity have already been created for you.
Take a look at `my_site/todos/models.py`, and in the `my_site/migrations/` directory. Our Task
model is pretty simple, with just a title and description attribute to worry
about. This model doesn't have any real behavior, so we haven't created a test
in `todos/tests.py` for it yet, but if you add any behavior to the model you'll
want to create that file.


## Release 1: New / Create

Since we need a way to get records into our system, we'll start with the routes
to create new records. 


  If the user makes a GET request to `/todos/new` they should: 
    -see a form with the required form fields. 

  Submitting the form makes a POST request to `/todos`
    -it should create the new Task record in the database. 
    -after the new task is created, the user should be redirected to view that Task. 
    
Remember that we can write the code to redirect to the Task before we even
implement the route to actually show the Task. We only want to think about one
part of the system at a time, so just verify that the user is redirected to the
correct URL when a new record is created, and don't worry that for the moment
that route returns a 404 error.

## Release 2: Show / List

Next we need to be able to view records. Let's start with the show action since
it's currently broken when we create a new Task. Here are the requirements:


  A GET request to `/todos/<id>` (where id will be a number corresponding to id of the record you want to view), will:
    -show the title and description of the Task 
    -show a link to edit the existing Task
  

  A GET request to `/todos` should: 
    -show a list of all tasks that exist
    -show links to each task individually
    -show a link to create a new Task
 
## Release 3: Edit / Update

Now that we can list records, let's build the functionality to manipulate those
records.

  
  A GET to `/todos/edit/<id>`:
    -displays a form with the current title and description already filled out in each form field 
  

  Submitting the form: 
    -updates the existing task with the new provided values
    -redirects you back to the show page
  
  

## Release 4: Destroy

Finally, let's give users the ability to destroy an existing task. Since we haven't
really modeled a way to mark a task as complete, we'll use this to complete tasks
for the moment.

  A POST request to `/todos/delete/<id>`:
    -deletes the existing task
    -redirects you to the list page
  
  
