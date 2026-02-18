# Start with slim Python 3.13 image
#FROM python:3.13.10-slim

# Copy uv binary from official uv image (multi-stage build pattern)
#COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
#WORKDIR /app

# Add virtual environment to PATH so we can use installed packages
#ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
# Copy dependency files first
#COPY pyproject.toml ./

# install deps
#RUN uv sync --locked

# copy app code
#COPY pipeline.py main.py ./

#CMD ["python", "pipeline.py"]

# Copy application code
#COPY pipeline.py .

# Set entry point
#ENTRYPOINT [ "python", "pipeline.py"]

FROM python:3.10

WORKDIR /app

# copy dependency list
COPY requirements.txt requirements.txt

# install dependencies explicitly
RUN pip install --no-cache-dir -r requirements.txt

# copy code and data
COPY pipeline.py pipeline.py
COPY data data

CMD ["python", "pipeline.py"]

