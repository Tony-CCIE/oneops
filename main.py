from typing import Optional

from fastapi import FastAPI
from Lib import zabbix_info, redis_info

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/zabbix/host/list")
def host_list():
    return zabbix_info.host_ip()

@app.get("/zabbix/{hostid}/cpu/")
def cpu_uasge(hostid: int):
    return zabbix_info.cpu_usage(hostid)

@app.get("/zabbix/{hostid}/memory/")
def memory_uasge(hostid: int):
    return zabbix_info.memory_usage(hostid)

@app.get("/zabbix/{hostid}/net_in/")
def net_in(hostid: int):
    return zabbix_info.net_in(hostid)

@app.get("/zabbix/{hostid}/net_out/")
def net_out(hostid: int):
    return zabbix_info.net_out(hostid)

@app.get("/zabbix/{hostid}/items")
def host_items(hostid: int):
    cpu = zabbix_info.cpu_usage(hostid)
    memory = zabbix_info.memory_usage(hostid)
    net_in = zabbix_info.net_in(hostid)
    net_out = zabbix_info.net_out(hostid)
    items = {"cpu": cpu, "memory": memory, "net_in": net_in, "net_out": net_out}
    return items


@app.get("/redis/slowlog")
def slowlog():
    return redis_info.slowlog_get()
