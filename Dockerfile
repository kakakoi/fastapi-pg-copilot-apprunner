FROM tiangolo/uvicorn-gunicorn:python3.8

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./backend /app