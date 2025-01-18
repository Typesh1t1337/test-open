FROM python:3.12-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


COPY .env /usr/src/app/.env
COPY entrypoint.sh /usr/src/app/entrypoint.sh

RUN chmod +x /usr/src/app/entrypoint.sh
RUN pip install gunicorn

COPY . /usr/src/app/

CMD ["gunicorn", "webhook_project.wsgi:application", "--bind", "0.0.0.0:8000"]

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
