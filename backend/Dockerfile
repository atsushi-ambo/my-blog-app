# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL=mysql+pymysql://root:my-secret-pw@db:3306/mydb

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    default-mysql-client

# Install dependencies
RUN pip install --upgrade pip && pip install -vvv -r requirements.txt

# Copy wait-for script
COPY wait-for.sh /app/
RUN chmod +x /app/wait-for.sh
ADD --chmod=755 wait-for.sh /app/

# Run the command to start uWSGI
CMD /app/wait-for.sh db:3306 -- uwsgi --ini app.ini
