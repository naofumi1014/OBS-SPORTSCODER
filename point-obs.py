import asyncio
import websockets


async def point(websocket):
    file_path = 'point_data\\point.json'
    while True:
        with open(file_path,'r', encoding='utf-8_sig') as f:
            data_lines = f.read()

        await websocket.send(str(data_lines))
        await asyncio.sleep(0.1)


async def main():
    async with websockets.serve(point, "localhost", 2222):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
