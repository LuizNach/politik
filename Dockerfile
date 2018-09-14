# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

ADD . /politik

WORKDIR /politik

RUN pip install -r dependencies

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]