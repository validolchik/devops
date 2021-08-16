# Practices used
* `python:3.8-slim-buster` - just because it is small enough and works fine with this app.
* `COPY` - project is small, so copying is not long. Also, I wanted to keep resources of this app separated from other containers.
* `requirements.txt` - to easily install needed packages (core libraries and linters)