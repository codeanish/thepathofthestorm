FROM python:3.9-slim-buster

RUN pip install pipenv
COPY Pipfile /usr/src/Pipfile
WORKDIR /usr/src

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY web_scraper /usr/src/app

VOLUME [ "/data" ]

CMD ["python", "app/web_scrape_noaa.py"]