from pyzabbix import ZabbixAPI
import time
import asyncio
import aiohttp

class Zabbix:
    def __init__(self, url, user, password):
        self.zb = ZabbixAPI(url)
        self.zb.login(user, password)

    def get_token(self):
        # auth = self.zb.login(user, password)
        return self.zb.auth

    def hosts_all(self):
        data = self.zb.host.get(output=["hostid", "host"], selectInterfaces=["ip"])
        return data

    def id_list(self):
        id_list = []
        for i in range(len(self.hosts_all())):
            id_list.append(self.hosts_all()[i]["hostid"])
        return id_list

    def host(self, host_id):
        data = self.zb.host.get(output=["host"], hostids=host_id)
        return data[0]['host']

    # def ip(self, host_id):
    #     data = self.zb.host.get(output=["ip"], hostids=host_id, selectInterfaces=["ip"])
    #     return data[0]["interfaces"][0]["ip"]

    def items(self):
        key_list = ["system.cpu.util[,idle]", "vm.memory.size[available]", "net.if.in[eth0]", "net.if.out[eth0]"]
        data = self.zb.item.get(output=["host", "ip", "key_", "lastvalue"], hostids=self.id_list(), selectInterfaces=["ip"], filter={"key_": key_list})
        items_list = []
        for i in range(0, len(data), 4):
            items_list.append(data[i:i+4])
        return items_list

    def ip_list(self):
        ip_list = []
        for i in self.items():
            ip_list.append(i[0]['interfaces'][0]['ip'])
        return ip_list

    def netin_list(self):
        netin_list = []
        for i in self.items():
            netin_list.append(i[0]['lastvalue'])
        return netin_list

    def netout_list(self):
        netout_list = []
        for i in self.items():
            netout_list.append(i[1]['lastvalue'])
        return netout_list

    def cpu_idle_list(self):
        cpu_idle_list = []
        for i in self.items():
            cpu_idle_list.append(i[2]['lastvalue'])
        return cpu_idle_list

    # def cpu_idle(self, host_id):
    #     data = self.zb.item.get(output=["host", "key_", "lastvalue"], hostids=host_id, filter={"key_": ["system.cpu.util[,idle]", "vm.memory.size[available]"]})
    #     if len(data):
    #         return (data)
    #     else:
    #         return "null"
    #
    # def memory_usage(self, host_id):
    #     data = self.zb.item.get(output="extend", hostids=host_id, search={"key_": "vm.memory.size[available]"})
    #     if len(data):
    #         return ('{:.2f} GB'.format(float(data[0]["lastvalue"]) / 1024 / 1024 / 1024))
    #     else:
    #         return "null"
    #
    # def net_in(self, host_id):
    #     data = self.zb.item.get(output="extend", hostids=host_id, search={"key_": "net.if.in[eth0]"})
    #     if len(data):
    #         return ('{:.2f} Kbps'.format(float(data[0]["lastvalue"]) / 1000))
    #     else:
    #         return "null"
    #
    # def net_out(self, host_id):
    #     data = self.zb.item.get(output="extend", hostids=host_id, search={"key_": "net.if.out[eth0]"})
    #     if len(data):
    #         return ('{:.2f} Kbps'.format(float(data[0]["lastvalue"]) / 1000))
    #     else:
    #         return "null"


if __name__ == "__main__":
    z1 = Zabbix(url='http://10.157.27.56/zabbix/api_jsonrpc.php', user="shenping", password="password@123")
    # print(z1.items())
    print((z1.ip_list()))
    # print((z1.netout_list()))
    # print(z1.hosts_all())
    # print(z1.hostid())
    # print((z1.id_list()))
    # print(z1.ip())
    # print(z1.cpu_idle("10209"))
    # print(z1.memory_usage("10209"))
    # print(z1.net_in())
    # print(z1.net_out())

