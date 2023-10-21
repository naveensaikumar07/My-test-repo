# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for the database connection
ENV DB_HOST=postgres
ENV DB_NAME=mydatabase
ENV DB_USER=myuser
ENV DB_PASSWORD=mypassword

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Create and set the working directory
WORKDIR /app

# Install psycopg2 for PostgreSQL connectivity
RUN pip install psycopg2-binary

# Copy the application code to the container
COPY app.py /app/
COPY templates /app/templates

# Expose the web application port
EXPOSE 5000

# Run the Flask web application
CMD ["python", "app.py"]

