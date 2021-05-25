# this is an official Python runtime, used as the parent image
# for ubuntu
FROM python:3.9-slim 
# for mac

# FROM python:3.7.2-stretch

WORKDIR /app

ADD  .  /app

RUN set -x && pip install -r requirements.txt

EXPOSE 5000

ENV EMAIL_USER=YOUR_EMAIL
ENV EMAIL_PASS=YOUR_EMAIL_PASSWORD
# ENV SCERET_KEY=0
ENV SQL_DB_URL=sqlite:///site.db
ENV MAIL_SERVER=smtp.googlemail.com

CMD ["python", "app.py"]