FROM alpine:latest
LABEL mantainer "me@cprieto.com"

RUN apk update && apk upgrade \
  && apk add --no-cache python ca-certificates wget \
  && update-ca-certificates \
  && wget https://bootstrap.pypa.io/get-pip.py -O  - | python

ADD whoami /opt/whoami
WORKDIR /opt/whoami
RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["app.py"]
