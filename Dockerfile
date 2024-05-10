FROM python:3.11-slim

WORKDIR /projects/basic2

COPY . /projects/basic2

RUN pip install --no-cache-dir --upgrade pip setuptools

RUN pip install --no-cache-dir -r /projects/basic2/requirements.txt

CMD ["python", "/projects/basic2/scripts/main.py"]
