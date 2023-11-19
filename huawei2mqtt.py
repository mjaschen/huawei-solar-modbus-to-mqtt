import asyncio
import logging
import time

from huawei_solar import HuaweiSolarBridge
from dotenv import load_dotenv
import os
from modbus_energy_meter.mqtt import publish_data as mqtt_publish_data
from modbus_energy_meter.transform import transform_result


def init():
    load_dotenv()

    loglevel = logging.INFO
    if os.environ.get('HUAWEI_MODBUS_DEBUG') == 'yes':
        loglevel = logging.DEBUG

    logging.basicConfig(
        filename='huawei-modbus.log',
        level=loglevel,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S%z',
    )


async def main(inverter='primary'):
    if inverter != 'primary' and inverter != 'secondary':
        raise ValueError(f"Invalid inverter: {inverter}")

    modbus_slave_id = int(os.environ.get(f'HUAWEI_MODBUS_DEVICE_ID_{inverter.upper()}'))

    bridge = await HuaweiSolarBridge.create(
        os.environ.get('HUAWEI_MODBUS_HOST'),
        int(os.environ.get('HUAWEI_MODBUS_PORT')),
        slave_id=modbus_slave_id,
    )

    data = await bridge.update()
    mqtt_data = transform_result(data)

    mqtt_publish_data(mqtt_data, os.environ.get(f'HUAWEI_MODBUS_MQTT_TOPIC_{inverter.upper()}'))


if __name__ == "__main__":
    init()
    last_run = 0
    wait = 60
    while True:
        if last_run > 0 and (time.time() - last_run < wait):
            sleep_time = max(2, int(wait - (time.time() - last_run)))
            logging.debug("Sleeping for %d seconds", sleep_time)
            time.sleep(sleep_time)
        last_run = time.time()
        asyncio.run(main(inverter='primary'))
        time.sleep(2)
        asyncio.run(main(inverter='secondary'))
