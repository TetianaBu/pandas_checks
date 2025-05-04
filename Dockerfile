FROM python:3.10-slim

# Install dependencies
RUN pip install --no-cache-dir pandas pyarrow nbconvert jupyter

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Set the command to run your notebook
CMD ["python", "run_notebook.py"]
