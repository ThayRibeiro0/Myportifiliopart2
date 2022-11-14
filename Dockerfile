FROM python:3.8-slim-buster
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python app.py