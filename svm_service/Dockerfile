FROM python:3.9-slim-buster

WORKDIR ./

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY /app/svm-classification-model.h5 /app/svm-classification-model.h5

COPY . .

EXPOSE 8000

CMD ["python", "/app/app.py"]
