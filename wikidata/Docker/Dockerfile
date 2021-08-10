FROM python:3

RUN mkdir /wikiApp1/

WORKDIR /wikiApp1/

COPY ./requirements.txt /wikiApp1/requirements.txt
RUN pip install -r requirements.txt -v

COPY ./ /wikiApp1/

ENV FLASK_APP=wiki-app.py
CMD flask run -h 0.0.0 -p 5000
