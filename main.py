from fastapi import FastAPI
import uvicorn
from resources import zabbix, redis

app = FastAPI()
app.include_router(zabbix.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/zabbix/host/list")
def host_list():
    return zabbix.host_ip()

@app.get("/zabbix/{hostid}/cpu/")
def cpu_uasge(hostid: int):
    return zabbix.cpu_usage(hostid)

@app.get("/zabbix/{hostid}/memory/")
def memory_uasge(hostid: int):
    return zabbix.memory_usage(hostid)

@app.get("/zabbix/{hostid}/net_in/")
def net_in(hostid: int):
    return zabbix.net_in(hostid)

@app.get("/zabbix/{hostid}/net_out/")
def net_out(hostid: int):
    return zabbix.net_out(hostid)

@app.get("/zabbix/{hostid}/items")
def host_items(hostid: int):
    items = {"cpu": zabbix.cpu_usage(hostid), "memory": zabbix.memory_usage(hostid),
             "net_in": zabbix.net_in(hostid), "net_out": zabbix.net_out(hostid)}
    return items

@app.get("/redis/slowlog")
def slowlog():
    return redis.slowlog_get()

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=9099, reload=True, debug=True)