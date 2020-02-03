FROM jupyter/datascience-notebook:latest

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv lock --requirements >> requirements.txt
RUN pip install -r requirements.txt

RUN rm -r Pipfile Pipfile.lock requirements.txt work

ENTRYPOINT ["jupyter","notebook","--ip=0.0.0.0","--port=8888"]
