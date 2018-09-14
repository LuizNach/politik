FROM django

EXPOSE 8000

ADD . /politik

WORKDIR /politik

RUN sh manage-dependencies.sh

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]