# Dockerfile for Uniflow application
FROM python:3.9

# Set the working directory
WORKDIR /app

COPY . /app

# Install the dependencies
RUN pip install poetry
RUN poetry install --no-root

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "exam/server_client.py"]
