# Use the a Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the source code and data to the working directory
COPY src src

# Install build dependencies
RUN apt-get update

# Set up a virtual environment
RUN python -m venv venv

# Install dependencies
RUN venv/bin/python -m pip install --default-timeout=1000 --index-url https://pypi.org/simple/ --upgrade pip && \
    venv/bin/python -m pip install --index-url https://pypi.org/simple/ -r src/requirements.txt

# Command to run on container start
CMD ["venv/bin/python", "./src/main.py"]
