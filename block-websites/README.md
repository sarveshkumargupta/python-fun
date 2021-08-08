# Block websites using python

In this program no need to download any dependencies, I am only using python's inbuid libraries.
This program blocks the specific wesite present inside the programs website_list using windows host
file. Here we are using python's file handling so that we can write and delete some lines on host
file.

Steps:
1. Importing the libraries
2. Adding the list of websites to be block, also took out host file path into variable so that we
   can access easily.
3. variable redirect is the IP address of local machine.
4. We are declaring the time so that in between user can not access blocked websites.
5. Now we will create while loop with always true so that program can run every time.
6. Finally we have if else condition, So if your are using your machine in blocked time that means
   your if condition is ture. When you are not in blocked time then you can access all your blocked 
   websites that means your else block is true.
7. Concept - We are only addind our websites in host file to redirect those sites to local IP. 
