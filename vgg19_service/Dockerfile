FROM python:3.9-slim-buster

WORKDIR ./

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY /app/vgg-classification-model.h5 /app/vgg-classification-model.h5

COPY . .

EXPOSE 9000

CMD ["python", "/app/app.py"]
