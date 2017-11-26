# Copyright (c) 2017 Alex Pliutau

FROM python:3

ADD . /

RUN pip install slackclient rasa_nlu scipy scikit-learn sklearn-crfsuite numpy spacy wolframalpha wikipedia
RUN python -m spacy download en

CMD [ "python", "./bot.py" ]