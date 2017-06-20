FROM alpine:latest
LABEL mantainer "me@cprieto.com"

RUN apk update && apk upgrade \
    && apk add --no-cache wget openjdk8-jre \
    && mkdir -p /opt/dynamodb \
    && wget -O- https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz | tar -xzf - -C /opt/dynamodb \
    && apk del wget \
    && rm -rf /var/cache/apk/* 

ENV LANG C.UTF-8
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk

WORKDIR /opt/dynamodb

EXPOSE 8000
ENTRYPOINT ["java", "-Djava.library.path=/opt/dynamodb/DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar"]
