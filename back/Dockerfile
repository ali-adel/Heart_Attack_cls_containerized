# Use the official Python image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


FROM tensorflow/tensorflow:2.15.0

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install dependencies
RUN pip install --no-cache-dir fastapi "uvicorn"

# Expose the port that Uvicorn will listen on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]