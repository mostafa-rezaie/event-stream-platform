from fastapi import FastAPI
from typing import List
from app.models import Event
from app.kafka_producers import start_producer, stop_producer, send_event

app = FastAPI()

KAFKA_TOPIC = "user-events"


@app.on_event("startup")
async def startup():
    await start_producer()


@app.on_event("shutdown")
async def shutdown():
    await stop_producer()


@app.post("/events")
async def ingest_event(event: Event):
    await send_event(KAFKA_TOPIC, event.model_dump())
    return {"status": "accepted"}


@app.post("/events/batch")
async def ingest_events(events: List[Event]):
    # TODO: can be optimized via async 
    await asyncio.gather(*[
        send_event(KAFKA_TOPIC, event.model_dump())
        for event in events
    ])

    return {"received": len(events)}
