FROM python:3

ADD test_homepage.py /

CMD [ "python", "./test_homepage.py"]