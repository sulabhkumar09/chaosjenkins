FROM python:3.9
ENV VIRTUAL_ENV=env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY app.py .
EXPOSE 5002
CMD ["python", "app.py"]