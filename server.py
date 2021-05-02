import psutil
import time
from time import localtime, strftime
import json
import asyncio
import websockets

def get_cpu_reading():
	cpu = {} #we will store the cpu readings here
	cpu_readings = psutil.cpu_percent(interval=1, percpu=True)

	#{"cpu0": 52.5, "cpu1": 33.0, "cpu2": 54.5, "cpu3": 35.0}
	for i in range(0,len(cpu_readings)):
		cpu['cpu'+str(i)] = cpu_readings[i] 

	return cpu


async def hello(websocket, path):
    name = await websocket.recv()
    time.sleep(1)#sleep for 1 second
    reading_time = strftime("%H:%M:%S", localtime())
    send_obj = json.dumps({"time":reading_time, "cpu":get_cpu_reading()})

    await websocket.send(send_obj)
    print(send_obj)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()