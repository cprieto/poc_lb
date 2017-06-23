FROM alpine:latest
LABEL mantainer "me@cprieto.com"

RUN apk update && apk upgrade \
  && apk add --no-cache python ca-certificates wget curl \
  && update-ca-certificates \
  && wget https://bootstrap.pypa.io/get-pip.py -O  - | python \
  && apk del wget \
  && rm -rf /var/cache/apk/*

ADD whoami /opt/whoami
WORKDIR /opt/whoami
RUN pip install -r requirements.txt

EXPOSE 80
EXPOSE 2323

HEALTHCHECK --timeout=5s --interval=30s --retries=1 \
    CMD curl --fail http://localhost/health || exit 1

ENTRYPOINT ["python"]
CMD ["app.py"]
