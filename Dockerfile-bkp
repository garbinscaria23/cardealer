FROM python:3.10



# Set the working directory in the container

WORKDIR /app



# Copy the requirements file into the container at /app

COPY requirement.txt .



# Install any needed packages specified in requirement.txt

RUN pip install -r requirement.txt



# Copy the current directory contents into the container at /app

COPY . /app



# Expose port 8000

EXPOSE 8000



# Define the command to run on container start

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


