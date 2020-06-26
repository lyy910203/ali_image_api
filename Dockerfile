FROM python:3.7

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

COPY ./ /src/

WORKDIR /src

EXPOSE 5000

ENV FLASK_APP main.py

CMD ["python","-m","flask","run","--host=0.0.0.0"]
