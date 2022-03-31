FROM alpine:3.8

RUN apk add --no-cache curl python3 py3-pip && \
    pip3 install --upgrade pip && \
    pip3 install pytz

RUN adduser -S -D py
RUN mkdir /app
COPY app.py /app
RUN chown -R py: /app
#python with nonroot user wont accpet request from 0.0.0.0 (im dont know python, i dont know the solution) 
#USER py
EXPOSE 8080
WORKDIR /app
CMD ["python3", "app.py"]
