# Copyright (c) 2017 Alex Pliutau

FROM python:3

ADD . /

RUN pip install slackclient

CMD [ "python", "./mysql-bot.py" ]