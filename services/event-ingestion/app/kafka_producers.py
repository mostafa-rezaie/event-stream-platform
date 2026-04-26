from aiokafka import AIOKafkaProducer
import json

producer = None

async def start_producer():
    global producer
    # producer = AIOKafkaProducer(
    #     bootstrap_servers="localhost:9092"
    # )
    # await producer.start()
    print('Kafka started ...')

async def stop_producer():
    await producer.stop()

async def send_event(topic, event):
    # await producer.send_and_wait(
    #     topic,
    #     json.dumps(event).encode("utf-8")
    # )
    print('received and event' ,event)
