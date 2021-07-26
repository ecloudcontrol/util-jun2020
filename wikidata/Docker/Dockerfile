FROM python:3.7-alpine
WORKDIR /wiki
ENV FLASK_APP=wikiApp.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -vvv
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
