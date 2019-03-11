To Start the Server
'''''''''''''''''''
If you are using Ubuntu Terminal, go to the path the file is located in and type
             python3 main.py

You can also use any IDE that is capable of running Python Programs

Prerequisite
''''''''''''
Flask Python Package
Sqlite3 Python Package

Note: You should have flask package installed to run the code. It can be installed using command
pip install flask

Details of Files
''''''''''''''''
main.py - It is the file that contains the server code
table_schema.py - It contains the various queries that I used to create the tables
udaandb.db - This is the actual database file
templates folder - It contains the various HTML Files that I have used

Note
''''
1) I have used Flask a micro-web framework based on Python
2) I have used SQLite because it comes builtin with Python and we need not install anything.
3) Given the time constraints, I have gone lite on UI. I would have done better, have I had some more time
4) I have implemented all the backend features. I have used the exact URLs as specified in the problem statement
5) I have assumed my own schema, since none was explicitly specified
6) I have imposed foreign key constraint. So make sure the dependencies are satisfied.


