# Use a lightweight Alpine-based Python image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Install dependencies (including Flask)  
# Alpine uses 'apk' for package management, and we need some build dependencies
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

# Copy the requirements file and install dependencies  
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask project into the container
COPY . .

# Copy the scores.txt file inside the container
COPY scores.txt /app/scores.txt

# Expose the Flask default port (if using Flask)
EXPOSE 5000

# Set environment variable to avoid the need for FLASK_APP
ENV FLASK_APP=app.py

# Run Flask as the command
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]