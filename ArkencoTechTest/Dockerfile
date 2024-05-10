# Use an official Python runtime as a parent image
FROM python:3.12.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR .

# Install dependencies
COPY requirements.txt . 
# There I got failed to solve: failed to compute cache key: failed to calculate checksum of ref 28552fa7-6e0b-4be9-b170-d691089a4e40::ombhzk8emlo9rnkomm7rnjt1e: "/requirements.txt": not found
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . .