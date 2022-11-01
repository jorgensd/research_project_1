# We choose ubuntu 22.04 as our base docker image
FROM ubuntu:22.04

# Modifiable argument that can be pased in through command line
ARG REPO_BRANCH="main"

# Environment variable for correct usage of setuptools on ubuntu 22.04, see
# https://github.com/pypa/setuptools/issues/3269#issuecomment-1254507377
ENV DEB_PYTHON_INSTALL_LAYOUT=deb_system

# Install pip and git with apt
RUN apt-get update && \
    apt-get install -y python3-pip git

# We upgrade pip and setuptools
RUN python3 -m pip install pip setuptools --upgrade

# We set the working directory to install docker dependencies
WORKDIR /tmp/

# Install the Python-module
RUN git clone --branch ${REPO_BRANCH} --single-branch https://github.com/jorgensd/research_project_1
RUN python3 -m pip install ./research_project_1[all]


# We remove the contents of the temporary directory to minimize the size of the image
RUN rm -rf /tmp

