FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["python", "main.py"]