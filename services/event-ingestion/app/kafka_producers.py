from aiokafka import AIOKafkaProducer
import json

producer = None

async def start_producer():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v:json.dumps(v).encode('utf-8')
    )
    await producer.start()
    print('Kafka started ...')

async def stop_producer():
    await producer.stop()

async def send_event(topic, event):
    await producer.send_and_wait(
        topic,
        event
    )
    print('received and event' ,event)
