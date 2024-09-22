#!/usr/bin/env bash

# Run this file by running `bash install_sublime.sh`.

# Update all software.
sudo dnf update -y
# Add the GPG keys.
sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg

# Add the repo to your repos.d folder.
sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo

# Install sublime.
sudo dnf install sublime-text -y

# Launch sublime from the terminal.
subl
