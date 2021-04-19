FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /utj-be
WORKDIR /utj-be
RUN python -m venv env
RUN /bin/bash -c "source env/bin/activate"
ADD requirements.txt /utj-be/
RUN pip install -r requirements.txt
ADD . /utj-be/
EXPOSE 8000