FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY ./src/ /app

ENTRYPOINT ["python3"]
CMD ["app.py"]


