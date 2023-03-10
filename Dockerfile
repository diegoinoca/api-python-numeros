FROM python

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip3 install -r requirements.txt

ENTRYPOINT python main.py