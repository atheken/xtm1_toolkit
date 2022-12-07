FROM --platform=arm64 python:3.11
RUN mkdir /app
COPY ./src /app
WORKDIR /app
RUN pip install -r ./requirements.txt
EXPOSE 2323
ENV XTM1_RELAY_ADDRESS=0.0.0.0:2323
ENV XTM1_IP=201.234.3.1

ENTRYPOINT ["./LightBurnAdapter.py"]