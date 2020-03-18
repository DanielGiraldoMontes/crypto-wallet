# base image
FROM python:3.7.2

# install dependencies
RUN apt update && \
    apt install -y netcat-openbsd

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# add executed permission
RUN chmod +x /usr/src/app/entrypoint.sh

# run server
CMD ["/bin/bash", "/usr/src/app/entrypoint.sh"]
