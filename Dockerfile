FROM python

MAINTAINER Slava Chebotarev "slavik3g@gmail.com"

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]