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
