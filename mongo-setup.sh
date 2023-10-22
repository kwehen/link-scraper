#!/bin/bash

# Import the public GPG key
sudo apt-get update
sudo apt-get install gnupg curl -y
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor

# Create a list file for MongoDB
# Adjust the list file based on your Ubuntu version (Jammy in this example)
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# Reload local package database
sudo apt-get update

# Install MongoDB packages
sudo apt-get install -y mongodb-org

# Pin MongoDB packages to prevent unintended upgrades
#echo "mongodb-org hold" | sudo dpkg --set-selections
#echo "mongodb-org-database hold" | sudo dpkg --set-selections
#echo "mongodb-org-server hold" | sudo dpkg --set-selections
#echo "mongodb-mongosh hold" | sudo dpkg --set-selections
#echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
#echo "mongodb-org-tools hold" | sudo dpkg --set-selections

# Start MongoDB and enable it to start on boot
sudo systemctl start mongod
sudo systemctl enable mongod

# Verify that MongoDB has started
sudo systemctl status mongod