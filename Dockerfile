FROM python:3

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code/

CMD python manage.py runserver 0.0.0.0:8000

EXPOSE 8000