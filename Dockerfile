FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate; python manage.py runserver 0.0.0.0:8000"]