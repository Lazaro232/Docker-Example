# Base Python image
FROM python:3.10-slim
# Selecting working directory
WORKDIR /app
# Copying requirementes.txt file
COPY requirements.txt requirements.txt
# Install psycopg2 dependencies (need to be installed separately)
RUN apt-get update
RUN apt-get -y install libpq-dev gcc && pip3 install psycopg2
# Installing dependencies using pip
RUN pip3 install -r requirements.txt
# Copying current directory
COPY . .
# Running Flask server
CMD [ "python3", "app.py"]