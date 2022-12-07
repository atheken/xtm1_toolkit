FROM python:3.11-alpine
RUN mkdir /app
COPY ./src /app
WORKDIR /app
RUN apk add bash
RUN pip install -r ./requirements.txt
EXPOSE 2323
ENV XTM1_RELAY_ADDRESS=0.0.0.0:2323
ENV XTM1_IP=201.234.3.1

ENTRYPOINT ["./LightBurnAdapter.py"]