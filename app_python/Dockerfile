# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

RUN pip3 install requests

COPY . .

HEALTHCHECK --interval=5s --timeout=2s \
  CMD python3 -c "import sys; import requests;\
  r = requests.get('http://localhost:5000');\
  c = (0 if r.status_code == 200 else 1); sys.exit(c)"
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]