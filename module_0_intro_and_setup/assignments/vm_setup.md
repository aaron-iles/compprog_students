# VM Setup
**Goals:**
1. Access Guacamole
2. Confirm your ability to log into your VM
3. Configure your VM to your liking

**Description:** For this assignment you will log into Guacamole (a clientless remote desktop gateway) to access your own personal virtual machine on which all of your work in this clas will be performed. You are exempt from this assignment if you meet either of the following criteria:
1. You already have a laptop running a Linux distribution.
2. You have a laptop and plan to install and configure your own level 2 hypervisor running a Linux VM.

## Instructions
### Confirm access
1. Navigate to [my homelab Guacamole instance](https://guacamole.m9e.dev)
2. Log in using the credentials sent to your student email account.
3. Confirm that you see a connection called "\<your name\> (RDP)".
4. Click the connection and ensure that you are able to log into the VM.
5. Open Google Chrome and navigate to [GitHub](https://github.com)

### Confirm sudoers
1. Open the application called "Terminal" and confirm that you can run the following command
```
sudo echo "hello world"
```

### Update your bash profile
There are a number of scripts that run when you log in that change how your environment behaves. We are going to inject some commands to make it a bit better by using a file called `.bash_profile`. 
1. Copy the file [.bash_profile](../resources/.bash_profile) into your home directory in your VM. ==NOTE:== the file must be named `.bash_profile` not `bash_profile`! 
2. Log out of your VM.
3. Log back into your VM, open a terminal, and run the following command:
```
testme
```
4. Did you see a message get printed to the screen saying "it worked!"?
