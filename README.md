<h1>AirBnB clone - The console</h1>

Description
this project consists of recreating our own airbnb console.

##Repository contain
-[console.py] File with the console.
-[AUTHORS] Here are the authors of the project.
-[README.md] This is the readme for this project.
-[models] Folder that contain the functions for the console.
-[tests] Folder for testing the functions.

Execution
Your shell should work like this in interactive mode:
´´´
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
´´´
But also in non-interactive mode: (like the Shell project in C)
´´´
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
´´´

##Clone Repository
-git clone https://github.com/gastonperego/holbertonschool-AirBnB_clone.git

##Commands
´´´
Commands wich you can use are the following:
´´´
-help 
-quit
-create 
-show
-destroy
-update
´´´