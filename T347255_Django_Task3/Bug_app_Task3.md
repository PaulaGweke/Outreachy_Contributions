# Assist Capacity Exchange Development - Task 3

### This objective of this task is to reate views and templates to 1) `register and view a bug` and 2) `list all bugs registered`.

## Steps
1. Read the third and fourth parts of the Writing your first Django app tutorial.
2. Create one view to register a bug into the database.
3. Create a html template with a simple form to add the bug to database.
4. Create another view to view the fields of the bug.
5. Create a html template with a simple list of the fields of the bug.
6. And finally, create a view to list all the bugs in the database.
7. Create a html template with a simple list with links to the detail page of each bug.

# My Contribution
Following the tutorial steps, as recorded in task 2. I used the API Shell to define a single bug, `ERROR`
2. I created the templates for registered bug, `register_bug`, bug view `view_bug` and bug lists `list_bug`. 
3. I was able to view it on my django site, although using http://127.0.0.1:8000/ gave me an error message. Using http://127.0.0.1:8000/admin/Bug/ however worked as shown is pictures below.
[Image!](https://github.com/PaulaGweke/Outreachy_Contributions/blob/main/T347255_Django_Task3/bug_pic1_app_page.png)

[Image!](https://github.com/PaulaGweke/Outreachy_Contributions/blob/main/T347255_Django_Task3/bug_pic2_details.png)

4. The bug was initially created yesterday in Task 2. However, when I called q in the API terminal, It returned error even though Bug.ojects.all() was displaying a query of the bug. Since I am new to django, I reran the `q =Bug.objects.get(pk=1)` just to be on the safe side.
5. There is the option to add other bugs from the admin login. 
