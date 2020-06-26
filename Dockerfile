FROM i.harbor.dragonest.net/public/python:3.7

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt -i http://172.16.52.62:8081/repository/ly_pip_all/simple --trusted-host 172.16.52.62

COPY ./ /src/

WORKDIR /src

EXPOSE 5000

ENV FLASK_APP main.py

CMD ["python","-m","flask","run","--host=0.0.0.0"]
