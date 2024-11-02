FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the default command to run the app
# CMD ["streamlit", "run", "app.py", "--server.port=8501"]
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
