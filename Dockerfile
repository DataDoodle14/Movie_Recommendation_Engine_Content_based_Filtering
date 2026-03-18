
# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for some sklearn/nltk builds)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies first (layer caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data (if you use tokenizers/stopwords in your app)
RUN python -m nltk.downloader stopwords punkt

# Copy the rest of the application code
COPY app.py .
COPY model/ ./model/

# Expose Streamlit's default port
EXPOSE 8501

# Healthcheck so Docker knows when the app is ready
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]