import asyncio
import httpx
import uuid
import random
import time
from datetime import datetime, timezone

API_URL = "http://localhost:8000/events"   # your ingestion API endpoint
EVENTS_PER_SEC = 2000
BATCH_SIZE = 200
BATCHES_PER_SEC = EVENTS_PER_SEC // BATCH_SIZE


PAGES = [
    "/",
    "/home",
    "/products",
    "/products/123",
    "/search",
    "/pricing",
    "/about"
]

EVENT_TYPES = [
    "page_view",
    "click",
    "scroll",
    "search",
    "purchase"
]


def create_event():
    """Create a single fake event."""
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": random.randint(1, 10_000),
        "event_type": random.choice(EVENT_TYPES),
        "page": random.choice(PAGES),
        "metadata": {},
        "ts": datetime.now(timezone.utc).isoformat()
    }


async def send_batch(client, batch):
    """Send one batch to the ingestion API."""
    try:
        await client.post(API_URL, json=batch, timeout=1.0)
    except Exception as e:
        print("Send error:", e)


async def run_generator():
    """Main loop: generate events at ~2000/sec."""
    async with httpx.AsyncClient() as client:
        while True:
            start = time.time()

            # Generate batches
            batches = []
            for _ in range(BATCHES_PER_SEC):
                batch = [create_event() for _ in range(BATCH_SIZE)]
                batches.append(batch)

            # Send all batches concurrently
            await asyncio.gather(*[
                send_batch(client, batch)
                for batch in batches
            ])

            elapsed = time.time() - start
            remaining = 1.0 - elapsed

            print(f"Generated & sent {EVENTS_PER_SEC} events in {elapsed:.3f}s")

            # Maintain ~2000/sec rate
            if remaining > 0:
                await asyncio.sleep(remaining)


