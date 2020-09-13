import requests
import json
from pyzabbix import ZabbixAPI
from fastapi import APIRouter

router = APIRouter()

url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
user = "shenping"
password = "password@123"
zb = ZabbixAPI(url)


@router.get("/zabbix/token/")
def login():
    zb.login(user,password)
    return zb.auth


def hosts_all():
    login()
    hosts = zb.host.get(output=["hostid", "host"], selectInterfaces=["ip"])
    return hosts[0]


def cpu_usage(hostid="10184"):
    login()
    data = zb.item.get(output="extend", hostids=hostid, search={"key_":"system.cpu.util[,idle]"})
    if len(data):
        return(data[0]["lastvalue"]+' %')
    else:
        return data


def memory_usage(hostid="10184"):
    login()
    data = zb.item.get(output="extend", hostids=hostid, search={"key_":"vm.memory.size[available]"})
    if len(data):
        return('{:.2f} GB'.format(float(data[0]["lastvalue"])/1024/1024/1024))
    else:
        return data


def net_in(hostid="10184"):
    login()
    data = zb.item.get(output="extend", hostids=hostid, search={"key_":"net.if.in[eth0]"})
    if len(data):
        return('{:.2f} Kbps'.format(float(data[0]["lastvalue"])/1000))
    else:
        return data


def net_out(hostid="10184"):
    login()
    data = zb.item.get(output="extend", hostids=hostid, search={"key_":"net.if.out[eth0]"})
    if len(data):
        return('{:.2f} Kbps'.format(float(data[0]["lastvalue"])/1000))
    else:
        return data


if __name__ == "__main__":
    print(login())
    print(hosts_all())
    print(cpu_usage())
    print(memory_usage())
    print(net_in())
    print(net_out())
