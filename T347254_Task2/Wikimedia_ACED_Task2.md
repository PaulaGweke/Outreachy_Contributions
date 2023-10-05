# Assist Capacity Exchange Development - Task 2

This task is a continuation of Task 1 in Folder [T347253](https://github.com/PaulaGweke/Outreachy_Contributions/tree/main/T347253/T347253_Django_Bug_Redo) 
## Objective of the task: Structure a SQLite database and create a django model for the Bug app.

Steps:
* Read the second part of the Writing your first Django app tutorial.
* Create a Bug model with the following fields: "description", "bug_type", "report_date", "status", representing, respectively, the textual description of the bug, the type of the bug (e.g. error, new feature etc), the date in which the bug is being registered and the status of resolution of the bug (e.g. to do, in progress, done, etc).
* Structure the database as described in the tutorial and create at least one bug through Django Admin.

# Observations in Contribution
1. Since the tutorial was using a different app type. I found it difficult to use the API shell as this is my introduction to django (which uses Python environment that I am familiar with).
2. In the shell however, a created a variable q from `Bug.objects.all()` and got a `QuerySet [<Bug: ERROR>]>` using `q = Bug(title="ERROR", report_date=datetime.date.today())` . However, I did not see it in the site (not sure what to do after that as the tutorial guides like `'choice_set'` were not defined in the tutorial.
3. I was able to launch the site to the admin page but the `mysite` tab gave me error. I repeated the task 4 times but still could not comprehend the error message about the url of my Bug and admin (which I created using the polls.urls sample in the tutorial).
