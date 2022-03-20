## Servers & Desktops, Files & Dicrectories 

Here we will see what we mean by DevOps and its core components:  
#### Learning Objectives
- List different services by Linux OS
- Web servers available in Linux
- Database servers available in Linux
- Start and Stop different services

#### Linux Server & Services 
- When a linux server runs a background process continually is is called a **Deamon** e.g., mysqld deamon process for mysql. 
- Linux server provide services for File Server, Web Server, DB Server, Mail, Print etc.
- Web Servers - Listen to port 80 or 443 (e.g., Apache, nginx, httpd) 
- Init or systemd is the parent process for every process. Manage services with Systemd - ``` sudo systemctl start or stop, enable, disable, restart, reload, status [application.server]``` all of these will to manage different services. 
- Which init to see PID

#### Files & Directories 
- Refer to ss64.com for all Linux commands [SS64](https://ss64.com/bash/)
  
- • **pwd** – returns the path of the current working directory
- **cd** – change directory
- cd .. (with two dots) to move one directory up
- cd to go straight to the home folder
- **cd-** (with a hyphen) to move to your previous directory
- **ls** - view the contents of a directory
- ls -R will list all the files in the sub-directories as well
- ls -a will show the hidden files
- ls -al will list the files and directories with detailed
information like the permissions, size, owner, etc.

#### Common Commands (part II)
- cat – list the contents of a file on the
standard output, without opening the file. It can show contents of single or multiple files. 
- cat > filename creates a new file
- cat filename1 filename2>filename3 joins two
files and stores the output of them in a new file. Use >> to add new line in the existing file. cat >>filename3
- cp – copy files
- mv – move or rename files
- mkdir – create a new directory in the
current directory
- rm – remove file and directories
- rm –r to remove directory and all files inside

#### Common Commands (part III)


---

[Next: Day 0](00-day00.md)  
[Previous: Intro](02-LinuxIntro.md)  
[Home](../index.md)  
[Top](03-LinuxServers.md)



