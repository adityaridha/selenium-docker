FROM python:3

ENV REM_DRIVER="http://0.0.0.0:4444/wd/hub"

RUN mkdir /tests
COPY . /tests

WORKDIR /tests

RUN pip install -r requirements.txt

CMD [ "python", "test_homepage.py"]