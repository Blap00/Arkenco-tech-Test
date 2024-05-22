# Use an official Python runtime as a parent image
FROM python:3.12.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Install dependencies
COPY ./requeriments.txt .
RUN pip install -r requeriments.txt

# Copy the project code into the container
COPY . .



# Expose the port
EXPOSE 8000

CMD ["python","manage.py","makemigrations","python","manage.py","migrate","python","manage.py","runserver"]