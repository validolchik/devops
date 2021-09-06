# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
LABEL mainrtainer='r.valeev@innopolis.university'

WORKDIR /app_python
RUN adduser --disabled-password user && chown -R user /app_python
USER user

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

RUN pip3 install requests==2.26.0

COPY time_app/__init__.py /app_python/time_app/__init__.py

EXPOSE 5000

ENV FLASK_APP=time_app
ENV FLASK_ENV=development

HEALTHCHECK --interval=20s --timeout=3s \
  CMD python3 -c "import sys; import requests;\
  r = requests.get('http://localhost:5000');\
  c = (0 if r.status_code == 200 else 1); sys.exit(c)"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]