FROM python:3-alpine3.15

WORKDIR ./

COPY . .

ENV STATIC_URL /static
ENV STATIC_PATH /app/static


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 3000

CMD ["python", "/app/app.py"]
