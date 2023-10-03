# T347259
## Addressing the Lusophone technological wishlist proposals - Task 2 
## `Description`
`IMPORTANT:` Make sure to read the Outreachy participant instructions and communication guidelines thoroughly before commenting on this task. This space is for project-specific questions, so avoid asking questions about getting started, setting up Gerrit, etc. When in doubt, ask your question on Zulip first!
This is the second task for `T347259:` Addressing the Lusophone technological wishlist proposals.

Objective of the task: Create a Python script to get and print the status code of the response of a list of URLs from a .csv file.
Steps:

You should create an account in Github, if you don't already have one. You can do so at https://github.com/signup.
You should download this CSV input file: 
Based on the input provided, create and write your python code.
Your python code needs to get the urls from the file and print their status code in the following format:
`(STATUS CODE) URL`
e.g. `(200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-sissi-of-brazil-has-right-stuff-with-left-foot.html`
Commit your Python file to GitHub and send us a link to it (by email, on our talk page, or replying to this tickect, as you prefer).
Make sure to also register it as a contribution on the Outreachy website! We'll send you a reply to say whether it is accepted or not.


## `Observation`
* `Data Structure:` The data is a 2-D dataframe. No data cleaning was done on the data because the target was to write a script to give an output as close as the example.
Status codes 200 (meaning Okay), 403 (forbidden page), 404 (meaning page not found), Errors from Exceptions were output from the script
* An option for write was also added to the script
* It was observeed that some of the rows url were contained im more than 1 column of the csv file and so may be the cause of some of the 404 error. 

