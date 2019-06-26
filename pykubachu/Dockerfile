FROM python:3.7.3-alpine3.9

WORKDIR /app
EXPOSE 8080
CMD [ "./app.py" ]

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY images/ ./images

COPY app.py .
