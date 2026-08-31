from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


# def task():
#     time.sleep(3)
#     return 'Done'

# async def task():
#     await asyncio.sleep(3)
#     return 'Done'

@app.get('/')
async def home():
    await asyncio.sleep(3)
    return {
        'message': "Async API"
    }