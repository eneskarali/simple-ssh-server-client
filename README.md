# COMMAND SERVER PROJECT

## About 
There are 2 application, server to receive and execute incoming command requests and client to send commands to server and receive their output from server.

İt's developed with Python and communication between client and server is provided by TCP sockets. There are no extra modules or libraries, only build-in python modules used in this project (except dotenv).

To simplify the project, the selectors module or libraries providing ssh connection were not used. Code layout, project structure, and error handling are not perfect due to time constraints.

## Note

- All development and testing was done on Ubuntu 20.04.1 LTS.

- It was also designed to run windows terminal commands, but could not be tested due to time constraints.

## Working Logic
The client application can be started multiple times and used by more than one person. Each user instantly has its own directory. A directory is kept on the client application for each session and they are not affected by each other. All commands are run in the active directory of each session. All users can see the result of other users after processes such as creating new files.

## Installation

### Start Scripts

There are 2 main python scripts for client and server.

Firstly, you should start server script and thus the server starts listening for client requests.

- But before this, you can edit .env file for ip address and port configs. 

    You can find .env files under the commandServer/server/server and  commandServer/client/client directories.

     
- And then if the dotenv python library is not installed, you can install it by running the command below under the commandServer/ 

```sh
pip install -r requirements.txt
```
- Go to the server directory
```sh
cd commandServer/server/server
```
- Run the server script.

```sh
python server.py
```
- You should see an output like the following.

```sh
socket binded to port 2222
Command Server Started! Socket is listening...
```
- Go to the client directory

```sh
cd commandServer/client/client
```
- Run the client script. You can run the client script multiple times in different terminal windows for multiple sessions.

```sh
python client.py
```

- it will ask for a username, you can enter any username you want.

```sh
username: enes
```

- And ready to use. You can use all simple terminal commands with their parameters.

```sh
enes:~/home/enes/Desktop/simple-ssh-server-client/server/server$ ls
helpers.py
__pycache__
server.py
terminalService.py
enes:~/home/enes/Desktop/simple-ssh-server-client/server$ cd ..
enes:~/home/enes/Desktop/simple-ssh-server-client/server$ ls
server
test
enes:~/home/enes/Desktop/simple-ssh-server-client/server$
```
