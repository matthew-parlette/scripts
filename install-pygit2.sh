#!/bin/bash
cd /usr/local
echo "downloading libgit2..."
sudo wget https://github.com/libgit2/libgit2/archive/v0.21.2.tar.gz
echo "enter to proceed..."
read -n1 go
sudo tar xzf v0.21.2.tar.gz
echo "enter to proceed..."
read -n1 go
cd libgit2-0.21.2/
echo "running cmake..."
sudo cmake .
echo "enter to proceed..."
read -n1 go
echo "running make..."
sudo make
echo "enter to proceed..."
read -n1 go
echo "installing libgit2..."
sudo make install
echo "enter to proceed..."
read -n1 go
echo "installing pygit2..."
sudo pip install pygit2
echo "enter to proceed..."
read -n1 go
echo "testing pygit2..."
python -c 'import pygit2'
echo "done, exiting..."
