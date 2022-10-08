FROM python:3.10.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c","docker/gunicorn/conf.py","--bind",":8000","--chdir","config.wsgi:application"]