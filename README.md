## CPSC471 - Computer Communication
### Programming Assignment 
FTP Server and Client applications

<br>

### Team Members
1.  Danny Tzoc - dannytzoc@csu.fullerton.edu
2.  Garrett Reeve - Garrett.reeve@csu.fullerton.edu
3.  Nafis Chowdhury - nafis195@csu.fullerton.edu
4.  Asad Jafri - asad.jafri460@csu.fullerton.edu

<br>

### Programming Language
Python

<br>

### Execution Process
1. Please check python version is up to date 3.6 or higher. To check that use the "python --version" command in the terminal.
2. Open one terminal and run the server that will listen for connections.
3. Run the server.py program in terminal, "python <server.py> <.PORT>". Example: "python home_serv.py 1234"
4. Open another terminal and run the home_client.py program, "<home_client.py> <.SERVER-MACHINE> <.PORT>". Example: "python home_client.py localhost 1234"
5. From there we will have a list of commands for the client.py
    * ftp> get FILE NAME : (downloads file FILE NAME from the server)
    * ftp> put FILE NAME : (uploads file FILE NAME to the server)
    * ftp> ls : (lists files on the server)
    * ftp> quit : (disconnects from the server and exits)

<br>

### Other Notes
None
