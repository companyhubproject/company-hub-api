FROM python:3.9.10
LABEL mantainer="Helena Magaldi <helenamagaldi@gmail.com>"

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /opt/companyhub/

COPY ./companyhub/ ./

CMD ["python","manage.py", "runserver", "8888"]