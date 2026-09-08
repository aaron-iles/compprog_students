# VM Setup
## Goals
1. Access Guacamole
2. Confirm your ability to log into your VM
3. Configure your VM to your liking

## Description
For this assignment you will log into Guacamole (a clientless remote desktop gateway) to access your own personal virtual machine on which all of your work in this clas will be performed. You are exempt from this assignment if you meet either of the following criteria:
1. You already have a laptop running a Linux distribution.
2. You have a laptop and plan to install and configure your own level 2 hypervisor running a Linux VM.

## Instructions
### Confirm access
1. Navigate to [my homelab Guacamole instance](https://guacamole.m9e.dev)
2. Log in using the credentials sent to your student email account.
3. When prompted to allow Guacamole access to your clipboard, please grant it access.
4. After logging in you should see a login screen for your virtual machine. Enter your password and confirm that you can get into your VM.
5. Open Google Chrome and log into your Hope Academy email account. If you wish to log into your personal Chrome profile, that's okay too.
6. Open Google Chrome and navigate to [GitHub](https://github.com)

### Confirm sudoers
1. Open the application called "Terminal" and confirm that you can run the following command
```
sudo echo "hello world"
```

### Configure your VM
Now is your chance to change your wallpaper, theme, log into accounts, and whatever else you would like to do.
#### Set up GTE
The application `gnome-text-editor` is what you will use to edit your code. Open this application by opening the terminal and typing `gnome-text-editor` then pressing `Enter`.
In the upper right corner press the hamburger button then "preferences". Ensure your configuration looks like this

<img width="608" height="911" alt="image" src="https://github.com/user-attachments/assets/dc8d5c6b-6024-4be9-9c77-06d3c5131249" />
