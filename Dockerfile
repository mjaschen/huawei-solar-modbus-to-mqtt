FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY .env.docker /app/.env
COPY modbus_energy_meter /app/modbus_energy_meter
COPY huawei2mqtt.py /app

CMD ["python", "-u", "huawei2mqtt.py"]
