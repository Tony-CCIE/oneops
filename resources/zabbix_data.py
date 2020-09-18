from fastapi import APIRouter
from api.zabbix_api import Zabbix
import json


router = APIRouter()

zb = Zabbix(url='http://10.157.27.56/zabbix/api_jsonrpc.php', user="shenping", password="password@123")


@router.get("/zabbix/host/list/", tags=["zabbix"])
def host_all():
    return zb.hosts_all()


@router.get("/zabbix/{host_id}/info/", tags=["zabbix"])
def host_info(host_id):
    info = {
            "hostname": zb.host(host_id), "ip": zb.ip(host_id),
            "cpu_idle": zb.cpu_idle(host_id), "memory": zb.memory_usage(host_id),
            "net_in": zb.net_in(host_id), "net_out": zb.net_out(host_id)
            }
    return info


@router.get("/zabbix/ip_cpu/", tags=["zabbix"])
def ip_cpu():
    ip_list = []
    cpu_list = []
    for i in zb.id_list():
        ip_list.append(zb.ip(i))
        cpu_list.append(zb.cpu_idle(i))
    ip_cpu_dict = dict(zip(ip_list, cpu_list))
    ip_cpu_sort = dict_sort(ip_cpu_dict, 5)
    return ip_cpu_sort


def dict_sort(dict_n, n):
    dict_not_null = dict((key, value) for key, value in dict_n.items() if value != "null")
    dict_value_sort = dict(sorted(dict_not_null.items(), key=lambda x: x[1], reverse=True)[:n])
    return dict_value_sort
