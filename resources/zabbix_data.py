from fastapi import APIRouter
from api.zabbix_api import Zabbix
from queue import Queue
import threading
import time
import asyncio


router = APIRouter()

zb = Zabbix(url='http://10.157.27.56/zabbix/api_jsonrpc.php', user="shenping", password="password@123")


@router.get("/zabbix/host/list/", tags=["zabbix"])
def host_all():
    return zb.hosts_all()


@router.get("/zabbix/{host_id}/info/", tags=["zabbix"])
def host_info(host_id):
    start = time.time()
    info = {
            "hostname": zb.host(host_id), "ip": zb.ip(host_id),
            "cpu_idle": zb.cpu_idle(host_id), "memory": zb.memory_usage(host_id),
            "net_in": zb.net_in(host_id), "net_out": zb.net_out(host_id)
            }
    end = time.time()
    print(end-start)
    return info


@router.get("/zabbix/ip_cpu/", tags=["zabbix"])
def ip_cpu():
    ip_cpu_dict = dict(zip(zb.ip_list(), zb.cpu_idle_list()))
    ip_cpu_sort = (dict_sort(ip_cpu_dict, 5))
    new_ip_cpu = [{'ip': i[0], 'cpu': i[1]} for i in ip_cpu_sort.items()]
    return new_ip_cpu


def dict_sort(dict_n, n):
    dict_not_null = dict((key, value) for key, value in dict_n.items() if value != "null")
    dict_value_sort = dict(sorted(dict_not_null.items(), key=lambda x: x[1], reverse=True)[:n])
    return dict_value_sort
