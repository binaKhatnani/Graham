FROM selenium/standalone-firefox:85.0
FROM python:3
RUN pip install selenium
WORKDIR .