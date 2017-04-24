FROM python:3.5
ENV PYTHONUNBUFFERED 1

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true


# copy source code
COPY . /flask-celery
WORKDIR /flask-celery

# install requirements
RUN pip install -r requirements.txt
RUN groupadd -r celery && useradd -r -g celery celery

USER celery
# run the worker
#ENTRYPOINT ['celery']
#CMD ['-A','tasks', 'worker','--loglevel=info']
ENTRYPOINT celery -A tasks worker --loglevel=info
