FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /utj-backend
WORKDIR /utj-backend
RUN python -m venv env
RUN /bin/bash -c "source env/bin/activate"
ADD requirements.txt /utj-be/
RUN pip install -r requirements.txt
ADD . /utj-backend/
EXPOSE 8000
