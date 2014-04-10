FROM ubuntu
MAINTAINER matthew.parlette@gmail.com

# use the precise (12.04) repository
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update

# install required packages
RUN apt-get install -q -y nodejs

# create a user
# RUN adduser --disabled-password --home=/user --gecos "" user

# copy a directory
# ADD host-dir container-dir

# modify permissions on added directory
# RUN chown -R user:user container-dir

# copy and execute setup script
# ADD scripts/setup /setup
# RUN /setup

# copy the start script
# ADD scripts/start /start

# expose a port
# EXPOSE 3000

# run as a user
# USER rails

# define a command for this container
# CMD /start